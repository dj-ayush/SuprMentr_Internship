# Assignment Date: 11/03/2026
# Assignment Name: Customer Segmentation
# Description: Perform K-Means clustering on a mall dataset and describe
# customer groups.
#
# Dataset: Mall_Customers.csv (200 rows).

import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "Mall_Customers.csv")


def main() -> None:
    df = pd.read_csv(CSV_PATH)
    # Some versions of this file call it 'Genre' instead of 'Gender'.
    if "Genre" in df.columns:
        df = df.rename(columns={"Genre": "Gender"})
    print(f"Loaded Mall_Customers.csv  shape={df.shape}")
    print(df.head())

    features = df[["Annual Income (k$)", "Spending Score (1-100)"]]
    X = StandardScaler().fit_transform(features)

    kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X)

    print("\n--- Cluster sizes ---")
    print(df["Cluster"].value_counts().sort_index())

    print("\n--- Cluster profile (mean values) ---")
    print(df.groupby("Cluster")[
        ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
    ].mean().round(1))

    out = os.path.join(HERE, "14_clusters.png")
    plt.figure(figsize=(7, 5))
    for c in sorted(df["Cluster"].unique()):
        sub = df[df["Cluster"] == c]
        plt.scatter(sub["Annual Income (k$)"],
                    sub["Spending Score (1-100)"],
                    label=f"Cluster {c}")
    plt.title("Mall Customer Segments (K-Means, k=5)")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
    print(f"\nCluster plot saved to: {out}")

    print("\n--- Customer Group Descriptions ---")
    print(" * High income & high spenders  -> 'Premium Shoppers' (target VIP).")
    print(" * High income & low spenders   -> 'Careful Rich'      (need offers).")
    print(" * Low  income & high spenders  -> 'Impulse Buyers'    (value-first).")
    print(" * Low  income & low spenders   -> 'Budget Customers'  (essentials).")
    print(" * Average everything           -> 'Average Customers' (mainstream).")


if __name__ == "__main__":
    main()
