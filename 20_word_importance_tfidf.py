# Assignment Date: 24/03/2026
# Assignment Name: Word Importance Explorer
# Description: Use TF-IDF on 5 documents and identify top keywords with
# explanation.

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


documents = [
    # Doc 1 - sports
    "The cricket team won the match by six wickets in a thrilling final over.",
    # Doc 2 - cooking
    "To make pasta, boil water, add salt, cook the pasta and mix the sauce.",
    # Doc 3 - technology
    "Artificial intelligence and machine learning are transforming many industries.",
    # Doc 4 - travel
    "Visiting the mountains in winter gives you amazing snow views and fresh air.",
    # Doc 5 - education
    "Students should practise coding daily to build strong programming skills.",
]


def main() -> None:
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)

    features = vectorizer.get_feature_names_out()
    df = pd.DataFrame(matrix.toarray(), columns=features)

    print("=== TF-IDF Matrix (rounded) ===\n")
    print(df.round(3))

    print("\n=== Top 3 keywords per document ===\n")
    for i, row in df.iterrows():
        top = row.sort_values(ascending=False).head(3)
        keywords = ", ".join([f"{w} ({s:.2f})" for w, s in top.items()])
        print(f"Doc {i + 1}: {keywords}")

    print("\n--- Explanation ---")
    print(
        "TF-IDF gives a high score to a word that appears often in ONE\n"
        "document (term frequency) but rarely across all documents (inverse\n"
        "document frequency). That's why common words like 'the' or 'and'\n"
        "get filtered out and topic-specific words like 'cricket',\n"
        "'pasta', 'intelligence', 'mountains', and 'coding' dominate the\n"
        "top scores for each document."
    )


if __name__ == "__main__":
    main()
