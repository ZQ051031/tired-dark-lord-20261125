"""The Tired Dark Lord -- make.fun entry.

Writes one monologue of about 100 words, spoken by a fantasy villain
who is secretly just very tired, to /output/entry.txt.

The tiredness is never announced. It lives in the pauses, the trailing
thoughts, and the small deflections -- a biting chair, maps left unread,
candles that need trimming -- while the villainy stays intact: the siege,
the river gate, the scheme forty years in the making.

Standard library only. Deterministic: the same text every run.
"""

import os

MONOLOGUE = (
    "Ah. You're here. Sit\u2014 no, not there. That chair... it bites. "
    "I had it made for the ambassador. He lasted three days.\n"
    "\n"
    "Forty years I've kept this siege, hero. Forty years of black banners, "
    "of ravens, of generals bringing maps I no longer... read. "
    "The river gate opens at dawn\u2014 my doing, my... arrangement\u2014 "
    "and your city kneels, as cities do.\n"
    "\n"
    "You came to kill me, yes? They all do. The sword, the speech, the\u2014\n"
    "\n"
    "Hmm. Forgive me. The candles need trimming.\n"
    "\n"
    "Go on, then. Raise it. Just... not too quickly. "
    "I have a speech. I wrote it down. Somewhere."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
