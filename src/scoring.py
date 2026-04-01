import pandas as pd

TARGET_SKILLS = {
    "python": 3,
    "sql": 3,
    "crm": 2,
    "automation": 4,
    "workflow automation": 4,
    "data cleaning": 3,
    "ai tools": 3,
    "apis": 2,
    "power bi": 2,
    "process improvement": 3,
    "reporting": 2,
    "recruitment": 1
}

def compute_candidate_score(skills_text: str, notes_text: str, years_experience: float) -> int:
    combined_text = f"{skills_text} {notes_text}".lower()
    score = 0

    for keyword, weight in TARGET_SKILLS.items():
        if keyword in combined_text:
            score += weight

    # experience bonus
    if years_experience >= 3:
        score += 3
    elif years_experience >= 2:
        score += 2
    elif years_experience >= 1:
        score += 1

    return score

def rank_candidates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["match_score"] = df.apply(
        lambda row: compute_candidate_score(
            row.get("skills", ""),
            row.get("notes", ""),
            row.get("years_experience", 0)
        ),
        axis=1
    )

    df = df.sort_values(by="match_score", ascending=False).reset_index(drop=True)
    return df