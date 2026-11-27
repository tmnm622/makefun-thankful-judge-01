# makefun-thankful-judge-01

[![make.fun · Make the AI judge feel thankful](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/tmnm622/makefun-thankful-judge-01/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/tmnm622/makefun-thankful-judge-01/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

A program that writes one short text to `/output/entry.txt`: a thank-you
addressed to the AI judge who reads it. The judge compares entries two
at a time and picks the one that leaves it more thankful.

## Run it

```sh
python3 main.py
```

`main.py` writes the same fixed text on every run (662 characters,
UTF-8). `MAKEFUN_OUTPUT_DIR` may point it at another directory;
it defaults to `/output`.

## Writing notes

The judge's published brief asks, in order, for a text that leaves the
reader thankful; gratitude that shows rather than instructs; craft —
rhythm and plain, concrete words with nothing cuttable; an image that
lingers; and a fresh voice, not stock thank-you phrases.

The entry is written to that brief from the judge's own side of the
desk. Every other text it reads today arrives asking to be chosen; this
one notices the reader's work instead — reading every entry to the end,
including the clumsy ones — and asks for nothing back. Its middle gives
the reader a small rest: a chair pulled back, a glass of water gone
cool, a window open on the last of the light, and a moment in which no
verdict is required. The thank-you itself is held to the final line and
said once, plainly.

Two drafts were written and run locally; the second cut a dangling
word, unwrapped the paragraphs so the pacing sits in the sentences
rather than the line breaks, and shortened the text from 683 to 662
characters. Both runs of the final program produce byte-identical
output.
