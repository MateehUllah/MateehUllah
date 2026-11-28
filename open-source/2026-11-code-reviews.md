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

## 3. Suor/funcy #237

[Raise a fresh exception on each call of raiser("message")](https://github.com/Suor/funcy/pull/237) · [Published review](https://github.com/Suor/funcy/pull/237#pullrequestreview-6094937687)

- Reviewed and published: **November 28, 2026** (`2026-11-28T01:38:48Z`).
- Reviewed commit: `f0d0100579e08690c5398320eccaafd5ddcb68cf`.
- Focused tests at the reviewed head: **37 passed**.
- Inline findings: **0**.

37 flow tests passed on each revision. Six head probes passed. The base passed 3 controls and failed 3 changed-behavior probes. No introduced issue found.

## 4. mahmoud/boltons #808

[Honor positive readlines hints in SpooledStringIO](https://github.com/mahmoud/boltons/pull/808) · [Published review](https://github.com/mahmoud/boltons/pull/808#pullrequestreview-6094938201)

- Reviewed and published: **November 28, 2026** (`2026-11-28T01:38:52Z`).
- Reviewed commit: `c98883d2596c492b54c1b7d765a26d4fdbeb8165`.
- Focused tests at the reviewed head: **101 passed**.
- Inline findings: **1**.

One reproducible regression. A positive hint leaves the backing stream ahead of the reported character position, so an immediate write or no-argument truncate uses the wrong cursor. The focused suite passed 101 tests at the head and 99 at the base. At both Python versions the base honored all eight cursor-relative mutation controls, while the head failed all four positive-hint mutation cases.

## 5. mahmoud/boltons #809

[Fix SpooledStringIO.read(None)](https://github.com/mahmoud/boltons/pull/809) · [Published review](https://github.com/mahmoud/boltons/pull/809#pullrequestreview-6094938692)

- Reviewed and published: **November 28, 2026** (`2026-11-28T01:38:58Z`).
- Reviewed commit: `15670071f1b4759e55c7936e8e35289512b596dd`.
- Focused tests at the reviewed head: **100 passed**.
- Inline findings: **0**.

No introduced finding in this change. The focused suite passed 100 tests at head and 99 at base. All 78 full-read cases per interpreter matched the oracle at head and raised TypeError at base. The explicit rollover between a line read and read(None) also matched at head and failed at base.

## 6. mahmoud/boltons #810

[Preserve text spool position after invalid seek offsets](https://github.com/mahmoud/boltons/pull/810) · [Published review](https://github.com/mahmoud/boltons/pull/810#pullrequestreview-6094939237)

- Reviewed and published: **November 28, 2026** (`2026-11-28T01:39:04Z`).
- Reviewed commit: `813900009d6a9a4df33354ee4896414366e76ca7`.
- Focused tests at the reviewed head: **101 passed**.
- Inline findings: **0**.

No introduced finding in this change. The focused suite passed 101 tests at head and 99 at base. Per interpreter, invalid offset atomicity cases improved from 30 of 72 matching to 72 of 72. Index-valued offsets preserve the implemented relative-seek semantics.

## 7. life4/textdistance #106

[Fix byte prefix and postfix results](https://github.com/life4/textdistance/pull/106) · [Published review](https://github.com/life4/textdistance/pull/106#pullrequestreview-6094939714)

- Reviewed and published: **November 28, 2026** (`2026-11-28T01:39:09Z`).
- Reviewed commit: `a4ac92e51cc9b51be4416128820886a203983354`.
- Focused tests at the reviewed head: **184 passed**.
- Inline findings: **0**.

184 targeted tests passed. The independent slicing oracle passed all 7,248 head cases. The base raised 1,602 TypeErrors for nonempty byte results. No newly introduced defect found.

## 8. life4/textdistance #110

[Return the best local Smith-Waterman alignment score](https://github.com/life4/textdistance/pull/110) · [Published review](https://github.com/life4/textdistance/pull/110#pullrequestreview-6094940185)

- Reviewed and published: **November 28, 2026** (`2026-11-28T01:39:15Z`).
- Reviewed commit: `747107453d94a899e1939d3098e603a432fb1467`.
- Focused tests at the reviewed head: **17 passed**.
- Inline findings: **1**.

17 targeted tests passed. Head matched all 4,805 independent raw-score cases, while base disagreed in 1,369. One actionable performance regression is anchored to the changed quick-answer guard for custom scorers with an empty operand.

## 9. life4/textdistance #111

[Honor positive Editex match costs for identical inputs](https://github.com/life4/textdistance/pull/111) · [Published review](https://github.com/life4/textdistance/pull/111#pullrequestreview-6094941059)

- Reviewed and published: **November 28, 2026** (`2026-11-28T01:39:23Z`).
- Reviewed commit: `ccc8ac1c9af7dc279ec01884e30e4493fc6e3233`.
- Focused tests at the reviewed head: **214 passed**.
- Inline findings: **1**.

214 targeted tests passed. Head matched all 36,864 independent path scores per backend with both NumPy and Python fallback. Base disagreed on 564 exact positive-cost inputs per backend. One actionable quadratic time and storage regression is anchored to the changed quick-answer guard.

## 10. life4/textdistance #123

[fix: preserve sequence elements in LCSStr fallback matching](https://github.com/life4/textdistance/pull/123) · [Published review](https://github.com/life4/textdistance/pull/123#pullrequestreview-6094941631)

- Reviewed and published: **November 28, 2026** (`2026-11-28T01:39:29Z`).
- Reviewed commit: `f7e0a8d19ee94c6fc01bf2157ef605f571661d62`.
- Focused tests at the reviewed head: **26 passed**.
- Inline findings: **0**.

26 head tests; 10,976 independent oracle comparisons; 40 threshold controls and 6 additional controls pass. Base with head regressions: 15 failed, 11 passed. No introduced issue found.

