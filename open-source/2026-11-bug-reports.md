# Open-source bug reports

Ten reproduced reports in the MIT-licensed fnc and pydash projects. This record was prepared on November 16, 2026 (Asia/Karachi).

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

## Reproduction evidence

- fnc source: `b474d32d47feab0aa56e25f53c0cf24487aaa977` (0.5.3).
- pydash source: `195d3dbcd0a274dc14c1dc22a18069723c07f5b6` (8.1.0).
- Environment: macOS 26.6.2 and CPython 3.11.15.
- Existing unit tests and doctests: 366 passed for fnc; 3,359 passed for pydash.
- New regression expectations: ten reproduced failures and ten passing controls against the unmodified source.

The reports include reproductions, expected and actual results, and source links. They were investigated, tested, and drafted with OpenAI Codex. These are bug reports; this record does not claim that fixes have been implemented or merged.
