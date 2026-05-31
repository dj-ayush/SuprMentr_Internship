# Assignment Date: 21/03/2026
# Assignment Name: Build a Text Cleaner
# Description: Write code to remove punctuation, lowercase text, remove
# stopwords and test it.

import re
import string


# Small hand-picked English stopwords list so the script works without
# downloading NLTK corpora.
STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "else", "of", "in",
    "on", "at", "to", "for", "with", "without", "by", "is", "are", "was",
    "were", "be", "been", "being", "am", "do", "does", "did", "have", "has",
    "had", "i", "you", "he", "she", "it", "we", "they", "them", "us", "me",
    "my", "your", "his", "her", "their", "our", "this", "that", "these",
    "those", "as", "from", "so", "too", "very", "can", "will", "just", "not",
    "no", "yes", "than", "because", "about", "over", "under", "again", "out",
    "up", "down", "also",
}


def clean_text(text: str) -> str:
    # 1. Lowercase
    text = text.lower()
    # 2. Remove URLs
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    # 3. Remove numbers
    text = re.sub(r"\d+", " ", text)
    # 4. Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # 5. Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    # 6. Remove stopwords
    tokens = [w for w in text.split() if w not in STOPWORDS]
    return " ".join(tokens)


def main() -> None:
    samples = [
        "Hello WORLD!! Visit https://example.com for more info. It's amazing.",
        "I have 3 apples and 5 oranges in my BAG.",
        "The quick brown fox jumps over the lazy dog.",
        "NLP is one of the most exciting areas in AI!!!",
        "Don't forget to buy milk, eggs, and bread tomorrow.",
    ]

    print("=== Text Cleaner Demo ===\n")
    for i, s in enumerate(samples, 1):
        cleaned = clean_text(s)
        print(f"{i}. Original : {s}")
        print(f"   Cleaned  : {cleaned}\n")


if __name__ == "__main__":
    main()
