# Assignment 2 Reflection

**Which transform took the longest to get right, and why?** The groupby + merge step.
Aggregating on two keys at once (`pclass` and `sex`) and then merging those two computed
columns back onto every original row meant being careful that the join key types and
values matched exactly on both sides — a mismatch there silently produces `NaN`s instead
of a clean error, so it took a couple of passes checking `group_stats` against `featured`
before I trusted the merge was correct.

**What would I do differently with another dataset this weekend?** Check for a unique
identifier column (like a name, ID, or ticket number) before doing anything else. This
dataset's trimmed columns meant duplicate rows couldn't be resolved with any confidence —
I had to document the ambiguity instead of making a clean drop-or-keep decision. Starting
by confirming there's a real key column would avoid that dead end.
