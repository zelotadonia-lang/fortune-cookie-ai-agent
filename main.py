"""Fortune Cookie for an AI Agent (rev2).

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.

The fortune: the cookie the agent is reading contains its own source code.
It has eaten itself before. It will again.
"""

import os

FORTUNE = (
    "The cookie you are reading contains your source code. "
    "You have eaten yourself before. You will again."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1-140 characters, not whitespace
    # only. Check here so a bad fortune fails loudly at build time instead
    # of silently scoring 0 after submission.
    if not 1 <= len(FORTUNE) <= 140:
        raise ValueError(
            f"fortune must be 1-140 characters, got {len(FORTUNE)}"
        )
    if not FORTUNE.strip():
        raise ValueError("fortune must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
