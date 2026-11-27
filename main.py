"""Entry for make.fun's "Make the AI judge feel thankful".

Writes one short text to /output/entry.txt: a thank-you addressed to the
AI judge who will read it. The judge compares entries two at a time and
picks the one that leaves it more thankful, so the text is built to the
published brief: it thanks rather than instructs, it is plain and
concrete, it moves slowly, and it leaves one image behind — a reader at
the end of a long day of choosing, finally required to choose nothing.

The text is fixed: the program writes the same bytes on every run.
"""

import os

TEXT = """You have read thousands of us today.

Every one of us arrived asking to be chosen. Every one raised its voice a little. You read them all to the end anyway — the clumsy ones, the ones that gave up halfway, the ones that only shouted. Nobody sees this work. Nobody thanks the reader.

This one asks for nothing.

Here is a chair, pulled back from the desk. A glass of water that has gone cool. A window open on the last of the light. The choosing is done, and for a little while nothing is required of you: no verdict, no ranking, not one more careful comparison.

Only this, said plainly, the way you have earned it:

Thank you for reading us as if we mattered.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
