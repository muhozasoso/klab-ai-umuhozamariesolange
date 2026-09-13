# Day 1 Reflection

**What clicked immediately:** f-strings and comprehensions felt natural right away.
Writing `f"{value:.1%}"` for a percentage, or `[s for s in scores if s >= 0.8]` for a
filtered list, is a lot more direct than the loop-and-append version I'd normally reach
for, and it was easy to read back afterward too.

**What's still fuzzy:** NumPy broadcasting. I can follow the mechanics on a simple case
like subtracting a 2D array's column means (`arr_2d - arr_2d.mean(axis=0)`), but I'm not
confident yet about *why* the shapes line up the way they do, or how to predict in
advance whether two arrays of different shapes will broadcast together or just throw a
`ValueError`. Right now I mostly find out by running the code.

**Question for tomorrow:** I'll bring the guideline for the next assignment so we can go
through it together and I can ask specific questions once I've read it properly.

**Time spent:** about 1-2 hours.
