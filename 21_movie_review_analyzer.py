# Assignment Date: 26/03/2026
# Assignment Name: Movie Review Analyzer
# Description: Build a simple sentiment analyzer and test on 5 reviews.
#
# Dataset: imdb_reviews_sample.csv (200 balanced reviews trimmed from the
# public IMDB sentiment dataset).

import os
import pandas as pd


HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "imdb_reviews_sample.csv")


POSITIVE_WORDS = {
    "good", "great", "amazing", "awesome", "fantastic", "fun", "loved", "love",
    "excellent", "brilliant", "best", "perfect", "enjoyable", "wonderful",
    "beautiful", "thrilling", "entertaining", "nice", "liked", "like",
    "masterpiece", "heartwarming", "stunning", "hilarious", "recommend",
    "impressive", "charming", "enjoy", "favorite", "favourite", "powerful",
}

NEGATIVE_WORDS = {
    "bad", "boring", "worst", "terrible", "awful", "hate", "hated", "poor",
    "disappointing", "waste", "horrible", "slow", "dull", "weak", "mess",
    "cringe", "cheesy", "predictable", "ridiculous", "stupid", "lame",
    "annoying", "forgettable", "nonsense", "mediocre", "pathetic",
}

NEGATORS = {"not", "no", "never", "nothing", "hardly"}


def analyze(review: str) -> dict:
    tokens = [w.strip(".,!?\"'()[]").lower() for w in str(review).split()]
    score = 0
    hits = []

    for i, word in enumerate(tokens):
        sentiment = 0
        if word in POSITIVE_WORDS:
            sentiment = 1
        elif word in NEGATIVE_WORDS:
            sentiment = -1

        if sentiment != 0:
            if i > 0 and tokens[i - 1] in NEGATORS:
                sentiment *= -1
            score += sentiment
            hits.append((word, sentiment))

    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"

    return {"score": score, "label": label, "hits": hits}


def main() -> None:
    df = pd.read_csv(CSV_PATH)
    print(f"Loaded imdb_reviews_sample.csv  shape={df.shape}")

    # --- Test on the first 5 reviews ---
    print("\n=== Sentiment on 5 sample reviews ===\n")
    for i, row in df.head(5).iterrows():
        review_text = str(row["review"])[:220]
        true_label = row["sentiment"]
        result = analyze(row["review"])
        print(f"{i + 1}. Review (first 220 chars): {review_text}...")
        print(f"   Predicted : {result['label']}   (score={result['score']})")
        print(f"   True label: {true_label}")
        print(f"   Hits      : {result['hits'][:6]}\n")

    # --- Accuracy on the full sample ---
    preds = df["review"].apply(lambda r: analyze(r)["label"])
    # Treat 'neutral' as wrong (our lexicon could not decide).
    correct = (preds == df["sentiment"]).sum()
    total = len(df)
    print(f"Overall rule-based accuracy on 200 reviews: "
          f"{correct}/{total} = {correct / total:.1%}")
    print(
        "\nNote: a hand-written lexicon with negation handling will never beat "
        "a trained model (Logistic Regression + TF-IDF typically hits ~85%)."
    )


if __name__ == "__main__":
    main()
