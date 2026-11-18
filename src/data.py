from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
OUT_DIR = ROOT / "data" / "processed"

STEP = pd.Timedelta(minutes=5)


def read_file(path):
    df = pd.read_csv(path, sep=";")
    df["time"] = pd.to_datetime(df["time"])
    df["patient_id"] = path.stem.removesuffix("P")
    return df


def build_dataset():
    files = sorted(RAW_DIR.glob("*.csv"))
    print("Files found:", len(files))

    parts = []
    for path in files:
        df = read_file(path)
        parts.append(df)
        print(f"  {path.name}: {len(df)} rows")

    data = pd.concat(parts, ignore_index=True)
    data = data.sort_values(["patient_id", "time"]).reset_index(drop=True)
    return data


def check(data):
    print("\n--- Checks ---")
    print("Rows:", len(data))
    print("Patients:", data["patient_id"].nunique())
    print("Missing values:", data.isna().sum().sum())
    print("Duplicate patient+time rows:", data.duplicated(subset=["patient_id", "time"]).sum())

    for patient_id, group in data.groupby("patient_id"):
        step_sizes = group["time"].diff().dropna()
        if not (step_sizes.min() == step_sizes.max() == STEP):
            print("!! irregular sampling for", patient_id, step_sizes.min(), step_sizes.max())


def save_coverage(data):
    coverage = data.groupby("patient_id")["time"].agg(["min", "max", "size"])
    coverage.columns = ["start", "end", "rows"]
    coverage["days"] = (coverage["end"] - coverage["start"]).dt.days
    coverage.to_csv(OUT_DIR / "coverage.csv")
    return coverage


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    data = build_dataset()
    check(data)

    data.to_parquet(OUT_DIR / "patients.parquet", index=False)
    coverage = save_coverage(data)

    print("\n--- Coverage (first 5 rows) ---")
    print(coverage.head())
    print("\nSaved:", OUT_DIR / "patients.parquet")


if __name__ == "__main__":
    main()