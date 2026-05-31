# Assignment Date: 18/03/2026
# Assignment Name: Customer Segmentation
# Description: Perform K-Means clustering on a mall dataset and describe
# customer groups.
#
# This revision adds an "elbow plot" to choose the best k and also looks at
# age in addition to income and spending score.
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


def elbow_plot(X, out_path: str) -> None:
    inertias = []
    ks = range(1, 11)
    for k in ks:
        km = KMeans(n_clusters=k, n_init=10, random_state=42)
        km.fit(X)
        inertias.append(km.inertia_)

    plt.figure(figsize=(6, 4))
    plt.plot(list(ks), inertias, "o-")
    plt.title("Elbow Method for Optimal k")
    plt.xlabel("k")
    plt.ylabel("Inertia")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def main() -> None:
    df = pd.read_csv(CSV_PATH)
    if "Genre" in df.columns:
        df = df.rename(columns={"Genre": "Gender"})
    print(f"Loaded Mall_Customers.csv  shape={df.shape}")

    features = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]
    X = StandardScaler().fit_transform(features)

    elbow_plot(X, os.path.join(HERE, "16_elbow.png"))
    print("Saved elbow plot to 16_elbow.png")

    kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X)

    print("\n--- Cluster profile ---")
    print(df.groupby("Cluster")[
        ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
    ].mean().round(1))

    plt.figure(figsize=(7, 5))
    for c in sorted(df["Cluster"].unique()):
        sub = df[df["Cluster"] == c]
        plt.scatter(sub["Annual Income (k$)"],
                    sub["Spending Score (1-100)"],
                    label=f"Cluster {c}")
    plt.title("Customer Segments (k=5)")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(HERE, "16_clusters.png"))
    plt.close()

    print("\nCustomer groups generally split into:")
    print(" 1. Young high-income, high spenders - VIP target group.")
    print(" 2. Young low-income, high spenders  - enthusiastic bargain-hunters.")
    print(" 3. Older high-income, low spenders  - conservative & loyal.")
    print(" 4. Older low-income, low spenders   - essentials only.")
    print(" 5. Middle-aged mainstream shoppers  - bread-and-butter customers.")


if __name__ == "__main__":
    main()
