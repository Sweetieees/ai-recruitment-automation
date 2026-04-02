from preprocess import load_and_clean_data
from scoring import rank_candidates
from reporting import export_outputs

def main():
    print("\n=== AI Recruitment Automation System ===\n")
    role = input("Enter role (e.g. AI Intern): ")
    print(f"Screening candidates for: {role}")
    
    input_file = "data/candidates.csv"

    df = load_and_clean_data(input_file)
    ranked_df = rank_candidates(df, role)

    print("Ranked Candidates:")
    print(ranked_df[["name", "match_score", "score_breakdown"]])
    
    print("\nTop Candidates (Shortlist):")
    shortlist = ranked_df[ranked_df["match_score"] >= 8]
    print(shortlist[["name", "match_score"]])

    export_outputs(ranked_df)
    print("\nOutputs saved in the outputs/ folder.")

if __name__ == "__main__":
    main()