import glob
import os
import pandas as pd

files = sorted(glob.glob("data/raw/*.csv"))
print("Number of CSV files:", len(files))

results = []

for file in files:
    df = pd.read_csv(file, sep=";")

    print("\nFile name:", os.path.basename(file))
    print("Number of rows and columns:", df.shape)
    print("Column names:", df.columns.tolist())

    print("Missing values:")
    print(df.isna().sum())

    print("Duplicate rows:", df.duplicated().sum())

    print("Data types before conversion:")
    print(df.dtypes)

    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    time_diffs = df["time"].sort_values().diff().dropna()

    print("Time interval summary:")
    print(time_diffs.describe())

    print("Most common time intervals:")
    print(time_diffs.value_counts().head(10))

    print("Duplicated timestamps", df["time"].duplicated().sum())

    print("Invalid timestamps:", df["time"].isna().sum())

    print("Numeric summary:")
    print(df.describe().T.to_string())

    results.append({
        "file": os.path.basename(file),
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_timestamps": int(df["time"].duplicated().sum()),
        "invalid_timestamps": int(df["time"].isna().sum()),
        "min_interval": str(time_diffs.min()),
        "max_interval": str(time_diffs.max())
    })

results_df = pd.DataFrame(results)

print("\nValidation summary:")
print(results_df.to_string(index=False))

os.makedirs("data/processed", exist_ok=True)

results_df.to_csv(
    "data/processed/validation_summary.csv",
    index=False
)

print("Validation symmary saved.")