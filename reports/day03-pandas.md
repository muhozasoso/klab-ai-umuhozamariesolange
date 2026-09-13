# Day 3 Take-Home — Pandas Load, GroupBy, Merge

Loaded the Titanic dataset (891 rows), wrote the schema report (dtypes, null counts,
unique counts), and applied two non-trivial transforms: a two-key `groupby(["pclass",
"sex"])` aggregation merged back onto the dataframe, and a `pivot_table` reshaping
survival rate into a class-by-sex grid. Full detail, code, and shapes-before/after are in
`notebooks/a2_data_wrangling.ipynb` (Tasks 1 and 3), which this take-home fed directly
into Assignment 2.

**What surprised me:** how much class and sex alone explained survival. First-class women
survived at 96.7% and third-class men at 13.5% — a seven-fold gap from just two columns,
before age or fare even entered the picture. I expected the pattern to exist, but not for
it to be that stark.
