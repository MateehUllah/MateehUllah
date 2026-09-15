#!/usr/bin/env python3
"""Find useful GitHub issues while keeping PR creation human-approved."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


def gh(*args: str) -> Any:
    result = subprocess.run(["gh", *args], check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def score(issue: dict[str, Any], config: dict[str, Any]) -> int:
    title = issue["title"].lower()
    if any(term in title for term in config["blocked_terms"]):
        return -100
    labels = {label["name"].lower() for label in issue.get("labels", [])}
    value = 2 if "help wanted" in labels or "good first issue" in labels else 0
    value += min(3, sum(term in title for term in config["preferred_terms"]))
    value += 1 if issue.get("commentsCount", 0) <= 5 else 0
    value += 1 if 20 <= len(title) <= 100 else 0
    return value


def discover(config: dict[str, Any]) -> list[dict[str, Any]]:
    unique: dict[str, dict[str, Any]] = {}
    fields = "repository,number,title,url,labels,commentsCount,updatedAt"
    for query in config["searches"]:
        for issue in gh("search", "issues", query, "--limit", "50", "--json", fields):
            issue["score"] = score(issue, config)
            issue["repo"] = issue.pop("repository")["nameWithOwner"]
            if issue["score"] >= config["minimum_score"]:
                unique[issue["url"]] = issue
    return sorted(
        unique.values(),
        key=lambda item: (-item["score"], item["commentsCount"], item["updatedAt"]),
    )[: config["max_candidates"]]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=str(Path(__file__).with_name("config.json")))
    parser.add_argument("--output", default="github-agent-candidates.json")
    args = parser.parse_args()
    config = json.loads(Path(args.config).read_text())
    candidates = discover(config)
    Path(args.output).write_text(json.dumps(candidates, indent=2) + "\n")
    for item in candidates:
        print(f'[{item["score"]}] {item["repo"]}#{item["number"]}: {item["title"]}')
        print(f'    {item["url"]}')
    print("\nNo branch, commit, push, or PR was created. Review one candidate manually.")


if __name__ == "__main__":
    main()
