import pandas as pd
import os


def load_data():
    """Load profiles.csv safely."""
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "..", "Data", "profiles.csv")

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")

    df = pd.read_csv(csv_path)

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    return df.drop_duplicates()


def calculate_categorical_stats(df: pd.DataFrame, column: str):
    """
    Calculate min, max, mean counts and unique value count
    for a categorical column.
    """

    if column not in df.columns:
        raise ValueError(
            f"Column '{column}' not found. Available columns: {list(df.columns)}"
        )

    df = remove_duplicates(df)

    counts = df[column].dropna().value_counts()

    if counts.empty:
        raise ValueError(f"No valid data found in column '{column}'.")

    return (
        counts.min(),
        counts.max(),
        counts.mean(),
        counts.size,
    )


def main():
    df = load_data()

    # 🔴 CHANGE THIS IF YOU WANT TO ANALYZE SOMETHING ELSE
    target_column = "seniority_level"

    min_c, max_c, mean_c, unique_c = calculate_categorical_stats(
        df, target_column
    )

    print(f"Column analyzed        : {target_column}")
    print(f"Minimum count          : {min_c}")
    print(f"Maximum count          : {max_c}")
    print(f"Mean count             : {mean_c}")
    print(f"Unique values          : {unique_c}")


if __name__ == "__main__":
    main()
