"""The Agent's Uh-Oh entry.

Writes the single word an agent says when it has no idea what to do.
Standard library only.
"""

import os

WORD = "buffering"
# The word itself: an agent that has no idea what to do does not say
# "uh-oh" like a person would -- it stalls, spins, and announces its
# own loading state. "buffering" is that confession in one word.


def main() -> None:
    word = WORD.strip()
    assert word, "word must not be empty"
    assert not any(ch.isspace() for ch in word), "entry must be one word"
    assert len(word) <= 99, "entry must be at most 99 characters"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
