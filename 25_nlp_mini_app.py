# Assignment Date: 03/04/2026
# Assignment Name: NLP Mini App
# Description: Build a chatbot, fake news detector, or keyword extractor.
#
# Here we build a simple rule-based chatbot + TF-IDF keyword extractor.

import re
import random
from sklearn.feature_extraction.text import TfidfVectorizer


# ------------------ Chatbot ------------------

INTENTS = [
    {
        "name": "greeting",
        "patterns": [r"\bhi\b", r"\bhello\b", r"\bhey\b", r"good (morning|evening)"],
        "responses": ["Hello!", "Hi there, how can I help you today?", "Hey!"]
    },
    {
        "name": "name",
        "patterns": [r"what.*your name", r"who are you"],
        "responses": ["I'm MentorBot - your friendly NLP assistant."],
    },
    {
        "name": "weather",
        "patterns": [r"weather", r"is it (hot|cold|raining)"],
        "responses": ["I can't check live weather, but you can try Google.",
                      "I'm not connected to the internet!"],
    },
    {
        "name": "thanks",
        "patterns": [r"\bthanks\b", r"thank you", r"thx"],
        "responses": ["You're welcome!", "Happy to help."],
    },
    {
        "name": "bye",
        "patterns": [r"\bbye\b", r"goodbye", r"see you"],
        "responses": ["Bye! Have a great day.", "See you later!"],
    },
]

FALLBACK = ["I'm not sure I understand, could you rephrase?",
            "Can you tell me more?", "Hmm, I'll need to learn that."]


def chatbot_reply(message: str) -> str:
    msg = message.lower()
    for intent in INTENTS:
        for pattern in intent["patterns"]:
            if re.search(pattern, msg):
                return random.choice(intent["responses"])
    return random.choice(FALLBACK)


# ------------------ Keyword Extractor ------------------

def extract_keywords(text: str, top_n: int = 5) -> list:
    vectorizer = TfidfVectorizer(stop_words="english")
    vectorizer.fit([text])
    scores = zip(vectorizer.get_feature_names_out(),
                 vectorizer.transform([text]).toarray()[0])
    ranked = sorted(scores, key=lambda x: x[1], reverse=True)
    return [w for w, _ in ranked[:top_n]]


# ------------------ Demo ------------------

def demo_chatbot() -> None:
    print("=== Chatbot Demo (rule-based) ===")
    sample_messages = [
        "Hello",
        "What is your name?",
        "How's the weather today?",
        "Thanks a lot!",
        "Tell me a joke",
        "Goodbye",
    ]
    for msg in sample_messages:
        print(f"User : {msg}")
        print(f"Bot  : {chatbot_reply(msg)}\n")


def demo_keywords() -> None:
    print("=== Keyword Extractor Demo ===")
    article = (
        "Machine Learning is a subset of Artificial Intelligence that allows "
        "software applications to become more accurate at predicting outcomes "
        "without being explicitly programmed. Machine learning algorithms use "
        "historical data as input to predict new output values. Common use "
        "cases include fraud detection, recommendation systems, and natural "
        "language processing."
    )
    print("Article:\n", article)
    print("\nTop keywords:", extract_keywords(article, top_n=7))


def main() -> None:
    random.seed(0)
    demo_chatbot()
    demo_keywords()


if __name__ == "__main__":
    main()
