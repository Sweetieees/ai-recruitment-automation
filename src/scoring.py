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

def adjust_weights_for_role(role: str):
    role = role.lower()

    weights = TARGET_SKILLS.copy()

    if "ai" in role:
        weights["python"] += 2
        weights["ai tools"] += 3

    if "data" in role:
        weights["sql"] += 2
        weights["data cleaning"] += 2

    if "recruit" in role:
        weights["crm"] += 2
        weights["recruitment"] += 3

    return weights
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

def rank_candidates(df: pd.DataFrame, role: str) -> pd.DataFrame:
    print(f"Applying scoring logic for role: {role}")
    df = df.copy()

    scores = df.apply(
        lambda row: get_score_breakdown(
            row.get("skills", ""),
            row.get("notes", ""),
            row.get("years_experience", 0),
            role
        ),
        axis=1
    )

    df["match_score"] = scores.apply(lambda x: x[0])
    df["score_breakdown"] = scores.apply(lambda x: ", ".join(x[1]))

    df = df.sort_values(by="match_score", ascending=False).reset_index(drop=True)
    return df

def get_score_breakdown(skills_text: str, notes_text: str, years_experience: float, role: str):
    combined_text = f"{skills_text} {notes_text}".lower()
    reasons = []
    score = 0

    #role-based weights
    weights = adjust_weights_for_role(role)

    for keyword, weight in weights.items():
        if keyword in combined_text:
            score += weight
            reasons.append(f"{keyword} (+{weight})")

    # experience bonus
    if years_experience >= 3:
        score += 3
        reasons.append("3+ years experience (+3)")
    elif years_experience >= 2:
        score += 2
        reasons.append("2+ years experience (+2)")
    elif years_experience >= 1:
        score += 1
        reasons.append("1+ years experience (+1)")

    return score, reasons

def load_role_config():
    return {
        "target_skills": TARGET_SKILLS,
        "min_score_threshold": 8
    }