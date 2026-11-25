"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# Revision note: entry text reviewed and confirmed unchanged; the joke
# is one sentence, one line, and stands alone with no setup beyond itself.
# The entry text is one deadpan joke: an AI assistant that procrastinates
# on a joke about procrastination, for three marathons and counting.
import os

TEXT = (
    "I asked my AI assistant for a joke about procrastination, and it said "
    "it would get back to me \u2014 that was three marathons ago."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
