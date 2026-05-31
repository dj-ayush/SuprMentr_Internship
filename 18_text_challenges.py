# Assignment Date: 20/03/2026
# Assignment Name: Text Challenges
# Description: Collect 20 messy sentences and identify slang, emojis, typos;
# explain preprocessing needed.

import re
import sys
import unicodedata

# Force UTF-8 output so emojis print cleanly on Windows consoles.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


messy_sentences = [
    "OMG this movie was soo goood!! 😂😂😂 loved it",
    "idk what u mean bro, its liek totally fine",
    "Can u plz send the notes??? thx",
    "That exam was a nightmare 😭😭😭 i am deeaaad",
    "Bruhh the food was fire 🔥🔥 no cap",
    "tmrw we got a test, i haven't studied at all :(",
    "wassup everyone, how's ur day going",
    "lmao that joke was hilariousssss 🤣",
    "I can't beleive she said that rofl",
    "Yooo the new iPhone looks sickk 👀",
    "stop bein mean dude, its not cool",
    "im tryna focus but TV is tooo loud",
    "smh this traffic, gonna be late AGAIN",
    "thats kinda sus ngl",
    "pls fix teh bug in code ASAP",
    "good vibes only ✨💖",
    "running on 2 hrs of sleep 🫠",
    "mid assignment done, on to tha next",
    "don wanna miss the train, gotta go",
    "no cap, this pizza is the bestt 🍕",
]


def detect_emojis(text: str) -> list[str]:
    return [ch for ch in text if unicodedata.category(ch).startswith("S")
            or ord(ch) > 0x2600]


SLANG_WORDS = {
    "omg", "idk", "u", "plz", "thx", "bruh", "bruhh", "ngl", "sus", "lmao",
    "rofl", "tmrw", "ur", "lol", "smh", "tryna", "yo", "yoo", "yooo", "cap",
    "mid", "fire",
}


def detect_slang(text: str) -> list[str]:
    words = re.findall(r"[A-Za-z']+", text.lower())
    return [w for w in words if w in SLANG_WORDS]


def detect_typos(text: str) -> list[str]:
    suspicious = ["soo", "liek", "beleive", "hilariousssss", "sickk",
                  "tooo", "teh", "bestt", "bein", "tha", "wassup",
                  "don", "deeaaad", "goood"]
    found = []
    for t in suspicious:
        if re.search(rf"\b{re.escape(t)}\b", text):
            found.append(t)
    return found


def main() -> None:
    print("=== Text Challenges: Messy Sentences Analysis ===\n")
    for i, sent in enumerate(messy_sentences, 1):
        emojis = detect_emojis(sent)
        slang = detect_slang(sent)
        typos = detect_typos(sent)
        print(f"{i:2}. {sent}")
        if slang:
            print(f"    slang : {slang}")
        if typos:
            print(f"    typos : {typos}")
        if emojis:
            print(f"    emojis: {''.join(emojis)}")
        print()

    print("--- Preprocessing needed ---")
    print(
        "1. Remove / replace emojis (emoji -> text description or drop).\n"
        "2. Expand slang (u -> you, plz -> please, idk -> I don't know).\n"
        "3. Fix spelling (soo -> so, teh -> the) with a spell checker.\n"
        "4. Lowercase everything for uniformity.\n"
        "5. Strip punctuation and repeated characters (soooo -> so).\n"
        "6. Tokenise and remove stop words before feeding to an NLP model."
    )


if __name__ == "__main__":
    main()
