# Assignment Date: 27/03/2026
# Assignment Name: Semantic Meaning
# Description: Find 5 word pairs and explain semantic similarity.
#
# We use TF-IDF on short "definitions" of each word as a simple way of
# measuring semantic similarity without needing a large pre-trained model.

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Each word mapped to a short meaning/context sentence.
word_context = {
    "king":   "a male ruler of a country, royalty, monarch with a crown",
    "queen":  "a female ruler of a country, royalty, monarch with a crown",
    "car":    "a vehicle with four wheels and an engine used for driving on roads",
    "bike":   "a two-wheeled vehicle powered by an engine or pedals used on roads",
    "happy":  "feeling joy, pleasure and positive emotions",
    "sad":    "feeling sorrow, unhappiness and negative emotions",
    "apple":  "a round red or green fruit that grows on trees",
    "orange": "a round orange citrus fruit that grows on trees",
    "computer": "an electronic machine that processes data and runs software",
    "laptop":   "a portable personal computer that you can carry and use anywhere",
}


pairs = [
    ("king", "queen"),
    ("car", "bike"),
    ("happy", "sad"),
    ("apple", "orange"),
    ("computer", "laptop"),
]


def main() -> None:
    words = list(word_context.keys())
    docs = [word_context[w] for w in words]

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(docs)
    sim = cosine_similarity(matrix)
    sim_df = pd.DataFrame(sim, index=words, columns=words).round(3)

    print("--- Cosine similarity matrix ---")
    print(sim_df)

    print("\n--- 5 Word Pairs ---")
    explanations = {
        ("king", "queen"):       "Royal pair - same role, different gender.",
        ("car", "bike"):         "Both are road vehicles but differ in size and wheels.",
        ("happy", "sad"):        "Antonyms - opposite emotions (low similarity expected).",
        ("apple", "orange"):     "Both are fruits (related) but taste and color differ.",
        ("computer", "laptop"):  "Laptop is a type of computer (hyponym/hypernym).",
    }

    for a, b in pairs:
        score = sim_df.loc[a, b]
        print(f"{a:<10} <-> {b:<10} similarity = {score:.3f}")
        print(f"            {explanations[(a, b)]}")

    print("\n--- Note ---")
    print(
        "TF-IDF over short definitions captures *lexical overlap* more than\n"
        "true semantic meaning. Production NLP uses pre-trained embeddings\n"
        "(Word2Vec, GloVe, BERT) which understand that 'king' and 'queen'\n"
        "are similar even without shared words."
    )


if __name__ == "__main__":
    main()
