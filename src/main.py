from preprocess import load_and_clean_data
from scoring import rank_candidates
from reporting import export_outputs

def main():
    input_file = "data/candidates.csv"

    df = load_and_clean_data(input_file)
    ranked_df = rank_candidates(df)

    print("Ranked Candidates:")
    print(ranked_df[["name", "match_score", "skills"]])

    export_outputs(ranked_df)
    print("\nOutputs saved in the outputs/ folder.")

if __name__ == "__main__":
    main()