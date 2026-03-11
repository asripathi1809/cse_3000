import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    merged = pd.merge(
        anon_df,
        aux_df,
        on=["age", "gender", "zip3"],
        how="inner"
    )

match_counts = merged.groupby("anon_id").size()

unique_ids = match_counts[match_counts == 1].index
unique_matches = merged[merged["anon_id"].isin(unique_ids)]

matches_df = unique.matches[["anon_id", "name"]].rename(
    columns={"name": "matched_name"}
)

    return matches_df


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    matched = matches_df["anon_id"].nunique()
    total = anon_df["anon_id"].nunique()

    return matched / total
