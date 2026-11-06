# Open-source bug reports

Reproduced bug reports in open-source Python projects. This log was first prepared on November 16, 2026 and updated on November 18, 2026 (Asia/Karachi).

## November 14, 2026 — boltons

Ten reports were published in the BSD-licensed boltons project on November 14, 2026 (Asia/Karachi). This earlier batch is recorded here retrospectively; statuses were checked on November 18, 2026.

| Project | Report | Status on November 18 |
| --- | --- | --- |
| `mahmoud/boltons` | [#768: statsutils.mean rejects finite iterators accepted by Stats and median](https://github.com/mahmoud/boltons/issues/768) | Open |
| `mahmoud/boltons` | [#769: median_abs_dev reports zero dispersion for nearby large integers](https://github.com/mahmoud/boltons/issues/769) | Open |
| `mahmoud/boltons` | [#770: kurtosis ignores the configured default for constant samples](https://github.com/mahmoud/boltons/issues/770) | Open |
| `mahmoud/boltons` | [#771: SpooledStringIO overwrites corrupt UTF-8 when character widths change](https://github.com/mahmoud/boltons/issues/771) | Open |
| `mahmoud/boltons` | [#772: ContextualCallpoint.to_dict crashes on empty context and misnumbers lines](https://github.com/mahmoud/boltons/issues/772) | Open |
| `mahmoud/boltons` | [#773: ParsedException.to_string crashes for successfully parsed SyntaxError output](https://github.com/mahmoud/boltons/issues/773) | Open |
| `mahmoud/boltons` | [#774: reverse_iter_lines splits UTF-16/UTF-32 text inside encoded code units](https://github.com/mahmoud/boltons/issues/774) | Open |
| `mahmoud/boltons` | [#775: URL.from_parts loses IPv6 address-family metadata and emits invalid authorities](https://github.com/mahmoud/boltons/issues/775) | Open |
| `mahmoud/boltons` | [#776: URL.navigate inherits the base query for an explicitly empty query reference](https://github.com/mahmoud/boltons/issues/776) | Open |
| `mahmoud/boltons` | [#777: deprecate_module_member disconnects module attributes from function globals](https://github.com/mahmoud/boltons/issues/777) | Open |

### Reproduction evidence

- Source: [`d31d821d56c8f7756af9c30a864077f2e5855321`](https://github.com/mahmoud/boltons/commit/d31d821d56c8f7756af9c30a864077f2e5855321).
- Original environment: macOS and CPython 3.12.13.
- Each report contains a runnable reproduction, expected and actual behavior, and links to the tested source. The original reproductions ran against unchanged library code.
- OpenAI Codex inspected the source, executed the reproductions, and drafted the reports at the repository owner's request.

### Record and commit dates

This retrospective entry and its commit were prepared on November 18, 2026. The owner requested an author date of November 6, 2026; the committer timestamp preserves the actual creation time. The report date above is the actual issue creation date in Asia/Karachi.

## November 16, 2026 — fnc and pydash

Ten reports in the MIT-licensed fnc and pydash projects.

| Project | Report |
| --- | --- |
| `dgilland/fnc` | [#5: omit and without silently retain excluded values when exclusions are iterators](https://github.com/dgilland/fnc/issues/5) |
| `dgilland/fnc` | [#6: groupall raises ValueError for an empty iterator of grouping iteratees](https://github.com/dgilland/fnc/issues/6) |
| `dgilland/fnc` | [#7: get and has raise TypeError for missing integer indexes in tuples](https://github.com/dgilland/fnc/issues/7) |
| `dgilland/fnc` | [#8: mapcat eagerly exhausts its source before returning any output](https://github.com/dgilland/fnc/issues/8) |
| `dgilland/fnc` | [#9: chunk reads an extra source item before yielding an already complete batch](https://github.com/dgilland/fnc/issues/9) |
| `dgilland/fnc` | [#10: random uses 1 rather than 0 as the other bound when one argument is provided](https://github.com/dgilland/fnc/issues/10) |
| `dgilland/fnc` | [#11: Following the documented retry callback signature aborts retries with TypeError](https://github.com/dgilland/fnc/issues/11) |
| `dgilland/fnc` | [#12: Set operations fail equality and deduplication for ordinary mutable set elements](https://github.com/dgilland/fnc/issues/12) |
| `dgilland/fnc` | [#13: xor retains duplicates for one input but removes them when an empty input is added](https://github.com/dgilland/fnc/issues/13) |
| `dgilland/pydash` | [#464: slope returns NaN for finite coordinates whose exact slope is 1](https://github.com/dgilland/pydash/issues/464) |

### Reproduction evidence

- fnc source: `b474d32d47feab0aa56e25f53c0cf24487aaa977` (0.5.3).
- pydash source: `195d3dbcd0a274dc14c1dc22a18069723c07f5b6` (8.1.0).
- Environment: macOS 26.6.2 and CPython 3.11.15.
- Existing unit tests and doctests: 366 passed for fnc; 3,359 passed for pydash.
- New regression expectations: ten reproduced failures and ten passing controls against the unmodified source.

The reports include reproductions, expected and actual results, and source links. They were investigated, tested, and drafted with OpenAI Codex. These are bug reports; this record does not claim that fixes have been implemented or merged.

## November 18, 2026 — funcy, boltons, and strsimpy

Ten additional reports were published on November 18, 2026 in the BSD-licensed funcy and boltons projects and the MIT-licensed strsimpy project. Statuses below were checked on the same date.

| Project | Report | Status on November 18 |
| --- | --- | --- |
| `Suor/funcy` | [#233: once_per runs twice for equal set and frozenset argument values](https://github.com/Suor/funcy/issues/233) | Open |
| `Suor/funcy` | [#234: once rejects functools.partial and builtin callables before their first call](https://github.com/Suor/funcy/issues/234) | Open |
| `mahmoud/boltons` | [#804: SpooledStringIO.readlines ignores positive hints and consumes the entire stream](https://github.com/mahmoud/boltons/issues/804) | Open |
| `mahmoud/boltons` | [#805: SpooledStringIO.read(None) raises TypeError instead of reading to EOF](https://github.com/mahmoud/boltons/issues/805) | Open |
| `mahmoud/boltons` | [#806: A failed SpooledStringIO.seek leaves the logical and underlying positions inconsistent](https://github.com/mahmoud/boltons/issues/806) | Open |
| `luozhouyang/python-string-similarity` | [#42: SIFT4 ngramtokenizer drops the final two windows and loses differing suffixes](https://github.com/luozhouyang/python-string-similarity/issues/42) | [Fixed in 0.4.2](https://github.com/luozhouyang/python-string-similarity/issues/42#issuecomment-6968668576) |
| `luozhouyang/python-string-similarity` | [#43: The recognized SIFT4 tokenizer='ngram' option always raises a missing-argument TypeError](https://github.com/luozhouyang/python-string-similarity/issues/43) | [Fixed in 0.4.2](https://github.com/luozhouyang/python-string-similarity/issues/43#issuecomment-6968669182) |
| `luozhouyang/python-string-similarity` | [#44: Rust calculator objects no longer pickle, breaking multiprocessing tasks using bound distance methods](https://github.com/luozhouyang/python-string-similarity/issues/44) | [Fixed in 0.4.2](https://github.com/luozhouyang/python-string-similarity/issues/44#issuecomment-6968669635) |
| `luozhouyang/python-string-similarity` | [#45: The public JaroWinkler.matches static method disappeared in the Rust API](https://github.com/luozhouyang/python-string-similarity/issues/45) | [Fixed in 0.4.2](https://github.com/luozhouyang/python-string-similarity/issues/45#issuecomment-6968670255) |
| `luozhouyang/python-string-similarity` | [#46: Precomputed-profile methods reject Mapping wrappers that worked before the Rust rewrite](https://github.com/luozhouyang/python-string-similarity/issues/46) | [Fixed in 0.4.2](https://github.com/luozhouyang/python-string-similarity/issues/46#issuecomment-6968670785) |

### Reproduction evidence

- funcy source: `a876c7e1cf11e7c746e91fce4632ebfa93865428`.
- boltons source: `d31d821d56c8f7756af9c30a864077f2e5855321`.
- strsimpy source: `af164425dc60516461dc1daf3ee13af6a901cde2` (0.4.1).
- Environment: macOS and CPython 3.11.15.
- Against those unmodified revisions, the ten regression expectations failed and all ten control checks passed. Reproductions and source references are included in each issue.

These reports were investigated and drafted with OpenAI Codex. The five strsimpy fixes are confirmed by the maintainer in the linked comments; the fixes were released in [v0.4.2](https://github.com/luozhouyang/python-string-similarity/releases/tag/v0.4.2).

### Commit date

This entry was prepared on November 18, 2026. At the repository owner's request, the commit uses an author date of November 17, 2026; its committer timestamp records the actual creation time. The report dates above reflect the GitHub issue creation dates.
