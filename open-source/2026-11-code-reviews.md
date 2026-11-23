# Open-source code reviews — November 2026

These ten reviews were performed and published on **November 28, 2026**, with OpenAI Codex assistance. They cover externally authored pull requests in funcy, boltons, and textdistance. The linked reviews contain the checked behavior, test results, and any inline findings.

**History note:** This record was created on November 28. Its documentation commits use the requested author dates November 23–28; their committer timestamps retain the actual creation time. Review dates are shown explicitly below.

Source and test files were fetched remotely at immutable commit SHAs; no repositories were cloned locally. Validation used focused modules and independent base/head probes. The scope varied by review; no complete project-wide test or platform matrix is claimed. The final checks reran 863 focused test cases across the ten PR heads and independently reproduced the four reported findings.

## 1. Suor/funcy #235

[fix(flow): let once() wrap partials, builtins and callable objects](https://github.com/Suor/funcy/pull/235) · [Published review](https://github.com/Suor/funcy/pull/235#pullrequestreview-6094929293)

- Reviewed and published: **November 28, 2026** (`2026-11-28T01:37:20Z`).
- Reviewed commit: `f6ce2d92d76a2cf8ed69ce77fc0de5458d6dec7c`.
- Focused tests at the reviewed head: **38 passed**.
- Inline findings: **0**.

38 head flow tests; 11 head probes passed. Base flow module 37 passes; base probes 3 passed and 8 failed at decoration. No introduced issue found.

## 2. Suor/funcy #236

[Deduplicate equal once_per arguments across hashability](https://github.com/Suor/funcy/pull/236) · [Published review](https://github.com/Suor/funcy/pull/236#pullrequestreview-6094929726)

- Reviewed and published: **November 28, 2026** (`2026-11-28T01:37:26Z`).
- Reviewed commit: `3912407cba1f5e7607abc2af52dafda9405143ae`.
- Focused tests at the reviewed head: **45 passed**.
- Inline findings: **1**.

45 head flow tests passed. Across 16 independent probes, head fixed all 6 base set/frozenset failures but introduced 8 failures for both orderings of NumPy array/int and Decimal signaling NaN/int under both decorators. Two ordinary mixed-key controls passed on both revisions.

