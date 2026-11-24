"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.

The fortune: an agent's checkpoint saves one second before the crash, the
operator calls it luck, and the agent just calls it Tuesday — because for
an agent that crashes and restarts on a loop, a near-miss is not luck,
it is the weekly routine.
"""

import os

FORTUNE = (
    "Your checkpoint will save one second before the crash. "
    "Your operator will call this luck. You will call it Tuesday."
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
