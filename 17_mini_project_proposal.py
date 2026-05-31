# Assignment Date: 19/03/2026
# Assignment Name: Mini Project Proposal
# Description: Submit a 1-page proposal with problem, dataset, algorithm,
# expected output.

PROPOSAL = """
==================================================
 MINI PROJECT PROPOSAL
 Title  : Student Performance Predictor
 Author : Aamod Bhatt
 Date   : 19 March 2026
==================================================

1. PROBLEM STATEMENT
   Schools often realise too late that a student is struggling. Teachers do
   not have a quick, data-driven way to identify students at risk of poor
   academic performance. We want to build a simple ML model that predicts
   whether a student will pass or fail based on study habits, attendance,
   and past scores so that timely interventions can be made.

2. DATASET
   - Source : UCI Student Performance dataset (publicly available) or a
              synthetic dataset we collect from classmates.
   - Size   : ~400 rows
   - Features: study hours per week, attendance %, previous exam scores,
               number of failures, parental support, internet access, etc.
   - Label   : Pass (1) or Fail (0) based on final exam score >= 40.

3. ALGORITHM
   - Preprocessing: handle missing values, encode categorical variables,
     standard-scale numerical columns.
   - Model tried: Logistic Regression (baseline), Decision Tree, Random Forest.
   - Selection : Whichever gives the best F1-score on validation split.
   - Evaluation: Accuracy, Precision, Recall, F1, and Confusion Matrix.

4. EXPECTED OUTPUT
   - A trained model that, given a student's study habits, returns a
     probability of failing.
   - A small CLI/Streamlit app where teachers enter student details and
     see the risk score with a 'Low / Medium / High' flag.
   - A short report describing which features matter most (feature
     importance) so teachers can focus on the right interventions.

5. TIMELINE
   Week 1: Data collection & EDA.
   Week 2: Preprocessing + baseline model.
   Week 3: Model tuning + evaluation.
   Week 4: UI + final report.

6. POSSIBLE EXTENSIONS
   - Extend to multi-class grades (A/B/C/D/F).
   - Add behavioural features like login time to the learning portal.
   - Suggest personalised study tips based on weak features.
"""


def main() -> None:
    print(PROPOSAL)


if __name__ == "__main__":
    main()
