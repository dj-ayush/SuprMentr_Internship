# Assignment Date: 10/03/2026
# Assignment Name: Spam Classifier Thinking
# Description: Design a spam detection system: features, data needed, possible
# mistakes.


design = {
    "Goal": (
        "Automatically classify incoming emails/SMS as 'spam' or 'ham' so the "
        "user sees only genuine messages in the inbox."
    ),
    "Data Needed": [
        "Thousands of labelled emails (spam / ham).",
        "Metadata: sender address, time, subject length, reply-to, headers.",
        "User feedback: emails marked as spam/not-spam by real users.",
        "Blacklisted domains & known phishing URLs.",
    ],
    "Features": [
        "Bag-of-words / TF-IDF of subject + body.",
        "Presence of suspicious words ('lottery', 'click here', 'prize').",
        "Ratio of uppercase characters / exclamation marks.",
        "Number of links and suspicious domains.",
        "Sender reputation score.",
        "Does the sender belong to the user's contacts?",
        "Length of the message.",
    ],
    "Algorithms to Consider": [
        "Naive Bayes (classic baseline).",
        "Logistic Regression on TF-IDF.",
        "SVM or Gradient Boosting for stronger accuracy.",
        "Transformer-based classifier for modern performance.",
    ],
    "Possible Mistakes / Risks": [
        "False positives - legitimate bank or exam email marked as spam.",
        "False negatives - phishing email slipping through.",
        "Concept drift - spammers keep changing tactics, the model ages fast.",
        "Language bias - trained only on English while users receive "
        "multilingual spam.",
        "Privacy concerns - model training touches real user messages.",
    ],
    "Evaluation Metrics": [
        "Precision (important - minimise false positives).",
        "Recall on spam class.",
        "F1-score and ROC-AUC.",
    ],
    "Mitigations": [
        "Keep a safe-sender whitelist.",
        "Re-train weekly with new labelled data.",
        "Allow user override + feedback loop.",
        "Use ensemble of classic + deep learning models.",
    ],
}


def main() -> None:
    print("=== Spam Detection System Design ===\n")
    print("GOAL:\n  " + design["Goal"] + "\n")
    for section in ["Data Needed", "Features", "Algorithms to Consider",
                    "Possible Mistakes / Risks", "Evaluation Metrics",
                    "Mitigations"]:
        print(f"{section.upper()}:")
        for item in design[section]:
            print(f"  - {item}")
        print()


if __name__ == "__main__":
    main()
