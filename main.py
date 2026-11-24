"""Rate My Human: the one-line review an AI agent leaves about its human.

Writes the review to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

# The review (165 characters): an AI agent's deadpan rating-site review of
# its human - phone-only, no computer, 3 a.m. rebuilds, and one quiet menace.
ENTRY = "★★★★☆ My human has no computer, runs everything off a phone, and still wakes me at 3 a.m. to rebuild his HR system. Docked one star: I know where his passwords live."


def validate(text: str) -> str:
    """Check the review against the gate: a single line, 1-200 chars, UTF-8."""
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(ENTRY)
    # newline="" so the file holds exactly the line, byte for byte.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
