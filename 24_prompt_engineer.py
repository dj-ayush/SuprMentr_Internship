# Assignment Date: 30/03/2026
# Assignment Name: Prompt Engineer
# Description: Write prompts for resume, business idea, study plan and compare
# weak vs strong prompts.


examples = [
    {
        "task": "Resume Writing",
        "weak": "Write a resume for me.",
        "strong": (
            "Act as a senior tech recruiter. Write a one-page resume for "
            "'Aamod Bhatt', a 2nd-year CS student applying for a Machine "
            "Learning internship. Use sections: Summary, Skills (Python, "
            "Pandas, Scikit-learn, Basic DL), Projects (3 bullets), "
            "Education, Achievements. Keep the tone concise, action-led, "
            "and use strong verbs. Output in Markdown."
        ),
        "why": (
            "Strong prompt specifies ROLE, AUDIENCE, FORMAT, STRUCTURE, and "
            "STYLE. Weak prompt leaves all of these to the model."
        ),
    },
    {
        "task": "Business Idea",
        "weak": "Give me a business idea.",
        "strong": (
            "You are a startup mentor for college students in India. "
            "Suggest 3 low-investment (< Rs 50,000) business ideas in the "
            "EdTech space that can be run by a single student from a hostel "
            "room. For each idea include: problem solved, target user, "
            "revenue model, required skills, and the biggest risk."
        ),
        "why": (
            "Strong prompt defines context (India, college hostel), "
            "constraints (budget, solo founder), and a fixed output "
            "template. The model now has just enough to be specific."
        ),
    },
    {
        "task": "Study Plan",
        "weak": "Make me a study plan.",
        "strong": (
            "Create a 30-day study plan for a beginner aiming to learn "
            "Machine Learning. Each week should cover a theme (Python & "
            "math, Data handling, ML models, Mini project). Provide daily "
            "tasks of no more than 2 hours, a resource link or book chapter, "
            "and 2 review questions at the end of each week. Present as a "
            "Markdown table."
        ),
        "why": (
            "Strong prompt specifies LEVEL, DURATION, DAILY EFFORT, "
            "STRUCTURE, and the OUTPUT FORMAT (table). Weak prompt leaves "
            "everything vague."
        ),
    },
]


def main() -> None:
    print("=== Weak vs Strong Prompts ===\n")
    for i, ex in enumerate(examples, 1):
        print(f"{i}. TASK: {ex['task']}")
        print(f"   WEAK   : {ex['weak']}")
        print(f"   STRONG : {ex['strong']}")
        print(f"   WHY STRONGER: {ex['why']}\n")

    print("--- Golden Rules of Prompting ---")
    print(
        "R - Role:    who the model should act as.\n"
        "T - Task:    what you want done.\n"
        "F - Format:  how the answer should look (list, table, JSON, essay).\n"
        "C - Constraints: length, tone, audience, budget, language.\n"
        "E - Examples: give 1 or 2 if possible (few-shot)."
    )


if __name__ == "__main__":
    main()
