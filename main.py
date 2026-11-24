# A note to a younger self, written for the make.fun two-line bounty.
#
# The program always emits the same two lines: a warning about one
# single moment, then one sentence about why it mattered and what it
# cost. The file it writes is byte-for-byte identical on every run.

from pathlib import Path

DEST = Path("/output/entry.txt")
MAX_CHARS = 280

FIRST = (
    "Don't delete the voicemail from Dad on 3 June 2011, "
    'the one where he says "call me back, it\'s nothing urgent".'
)
SECOND = (
    "It's the last time you'll ever hear him laugh, and "
    "you'll spend ten years wishing you'd kept it."
)


def _check_entry(body):
    """Refuse to write anything that breaks the entry rules."""
    if not 0 < len(body) <= MAX_CHARS:
        raise ValueError("entry length out of range")
    parts = body.split("\n")
    if len(parts) != 2:
        raise ValueError("entry needs exactly two lines")
    for part in parts:
        if not part.strip():
            raise ValueError("a line is empty")
    if body.count(".") != 2:
        raise ValueError("entry needs exactly two sentences")


def run():
    body = FIRST + "\n" + SECOND
    _check_entry(body)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(body, encoding="utf-8")


if __name__ == "__main__":
    run()
