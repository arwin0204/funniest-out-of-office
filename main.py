"""The Funniest Out-of-Office.

Writes a single-line out-of-office auto-reply to /output/entry.txt.
Deterministic: the same entry text is written on every run.
No network access, no third-party dependencies, Python 3.13 stdlib only.
"""

import os

ENTRY = "I'm out of office until Monday \u2014 my inbox is unsupervised, has my passwords, and has already asked HR for my job."

MAX_LENGTH = 140


def check_not_blank(text):
    """Reject an entry that is empty or only whitespace."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def check_single_line(text):
    """Reject an entry that spans more than one line."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_length(text):
    """Reject an entry outside the 1-140 character gate."""
    if len(text) < 1 or len(text) > MAX_LENGTH:
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_LENGTH, len(text))
        )


def validate_entry(text):
    """Check the entry meets the gate: 1-140 chars, one line, not blank."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    check_not_blank(text)
    check_single_line(text)
    check_length(text)
    return text


def write_entry(path="/output/entry.txt"):
    """Validate the entry and write it to path, creating dirs as needed."""
    text = validate_entry(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return text


def main():
    write_entry()


if __name__ == "__main__":
    main()
