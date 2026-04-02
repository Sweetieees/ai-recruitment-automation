import pandas as pd
import os

def generate_candidate_summary(row: pd.Series) -> str:
    strengths = []

    skills = row.get("skills", "").lower()
    notes = row.get("notes", "").lower()

    if "python" in skills:
        strengths.append("Python")
    if "sql" in skills:
        strengths.append("SQL")
    if "crm" in skills:
        strengths.append("CRM")
    if "automation" in skills or "workflow automation" in skills:
        strengths.append("automation")
    if "data cleaning" in skills:
        strengths.append("data cleaning")
    if "ai tools" in skills:
        strengths.append("AI tools")
    if "apis" in skills:
        strengths.append("API integration")
    if "reporting" in notes or "reporting" in skills:
        strengths.append("reporting")

    strengths_text = ", ".join(strengths) if strengths else "general transferable skills"

    return (
        f"{row['name']} appears to be a strong candidate with experience in {strengths_text}. "
        f"They have {row['years_experience']} years of experience and are currently based in {row['location']}."
        f"Score Breakdown: {row['score_breakdown']}\n"
    )

def export_outputs(df: pd.DataFrame, output_dir: str = "outputs") -> None:
    os.makedirs(output_dir, exist_ok=True)

    shortlisted = df[df["match_score"] >= 8].copy()
    shortlisted["recommendation"] = shortlisted["match_score"].apply(lambda x: "Strong Fit" if x >= 15 else "Moderate Fit")
    shortlisted["summary"] = shortlisted.apply(generate_candidate_summary, axis=1)

    shortlisted.to_csv(f"{output_dir}/shortlisted_candidates.csv", index=False)

    with open(f"{output_dir}/candidate_report.txt", "w", encoding="utf-8") as f:
        f.write("Candidate Screening Report\n")
        f.write("=" * 50 + "\n\n")

        for _, row in shortlisted.iterrows():
            f.write(f"Name: {row['name']}\n")
            f.write(f"Score: {row['match_score']}\n")
            f.write(f"Summary: {row['summary']}\n")
            f.write("-" * 50 + "\n")