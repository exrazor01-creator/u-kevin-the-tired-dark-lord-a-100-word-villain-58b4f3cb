"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes a single monologue of about 100 words to /output/entry.txt.

The speaker is a specific villain: a dark lord who won the crown,
lost his brother to it, and now rules an empire of unfiled reports.
His tiredness is never announced; it shows in the match he strikes
instead of the spell he used to cast, in the drawer where every
report lands, and in the way he waves the hero toward the crown
because filing one more thing is simply beyond him.
"""

import os

ENTRY = (
    "Come in. Mind the candles \u2014 I used to light them with a flick of "
    "my wrist, and now I use a match, like everyone else. The match, "
    "honestly, is more reliable. You came for the crown, I suppose. "
    "Everyone does. It sits there on the velvet, catching the draft. "
    "Three kingdoms bled for it. My brother bled for it. I keep meaning "
    "to polish it. The ravens bring reports, the spies bring whispers, "
    "and I file them. In the drawer. With the others. Do you know the "
    "hardest part of ruling the dark? The paperwork. So take the crown, "
    "hero. Or don't \u2014 the drawer is full."
)

# Gate from the competition kit: /output/entry.txt must be UTF-8 text
# of 1 to 600 characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 600
# The brief asks for a monologue of about 100 words.
TARGET_WORDS = 100
WORD_TOLERANCE = 15


def _validate(text):
    """Reject any text outside the competition gate.

    The monologue is one spoken block, so a newline would mean a second
    paragraph slipped in; the gate counts characters, so a stray newline
    would also eat the budget.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single paragraph, no newlines")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry is %d characters, outside the gate of %d to %d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    words = len(text.split())
    if abs(words - TARGET_WORDS) > WORD_TOLERANCE:
        raise ValueError(
            "entry is %d words, further than %d from the target of %d"
            % (words, WORD_TOLERANCE, TARGET_WORDS)
        )


def main():
    _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    words = len(ENTRY.split())
    print("wrote /output/entry.txt: %d characters, %d words" % (len(ENTRY), words))


if __name__ == "__main__":
    main()
