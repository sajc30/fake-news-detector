#!/usr/bin/env python3
import os
import sys
import pandas as pd
from pathlib import Path

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------

# Directory containing your CSV/TSV files
DATA_DIR = Path(__file__).parent / "data"

# Explicit column names for the LIAR datasets (no header row)
LIAR_COLUMNS = [
    "id",
    "label",
    "statement",
    "subjects",
    "speaker",
    "speaker_job",
    "state_info",
    "party_affiliation",
    "count_pantsfire",
    "count_false",
    "count_barelytrue",
    "count_halftrue",
    "count_mostlytrue",
    "context",
]

# Define each dataset: filename, separator, and which cols to explore
DATASETS = {
    "liar_train":      {"filename": "train.tsv",            "sep": "\t", "text_col": "statement", "label_col": "label"},
    "liar_valid":      {"filename": "valid.tsv",            "sep": "\t", "text_col": "statement", "label_col": "label"},
    "liar_test":       {"filename": "test.tsv",             "sep": "\t", "text_col": "statement", "label_col": "label"},
    "true":            {"filename": "True.csv",             "sep": ",", "text_col": "text",      "label_col": "label"},
    "fake":            {"filename": "Fake.csv",             "sep": ",", "text_col": "text",      "label_col": "label"},
    "politifact_real": {"filename": "politifact_real.csv",  "sep": ",", "text_col": "text",      "label_col": "label"},
    "politifact_fake": {"filename": "politifact_fake.csv",  "sep": ",", "text_col": "text",      "label_col": "label"},
    "gossipcop_real":  {"filename": "gossipcop_real.csv",   "sep": ",", "text_col": "text",      "label_col": "label"},
    "gossipcop_fake":  {"filename": "gossipcop_fake.csv",   "sep": ",", "text_col": "text",      "label_col": "label"},
}

# -----------------------------------------------------------------------------
# EXPLORATION FUNCTION
# -----------------------------------------------------------------------------
def explore_dataframe(df: pd.DataFrame, name: str, cfg: dict):
    """
    Print basic info, sample text, label distribution, and missing-values for a DataFrame.
    """
    print(f"\n=== Exploring `{name}` ===")
    print("Columns:", df.columns.tolist())

    print("\n[Info]")
    df.info()

    print("\n[First 5 rows]")
    print(df.head())

    # Sample text
    txt_col = cfg["text_col"]
    if txt_col in df.columns:
        print(f"\n[Sample text ({txt_col})]")
        print(df[txt_col].iloc[0])
    else:
        print(f"⚠️ Missing text column: {txt_col}")

    # Label distribution
    lbl_col = cfg["label_col"]
    if lbl_col in df.columns:
        print(f"\n[Label distribution ({lbl_col})]")
        print(df[lbl_col].value_counts())
    else:
        print(f"⚠️ Missing label column: {lbl_col}")

    # Missing values
    print("\n[Missing values per column]")
    print(df.isnull().sum())

# -----------------------------------------------------------------------------
# MAIN ROUTINE
# -----------------------------------------------------------------------------
def main():
    print("Looking in data directory:", DATA_DIR)
    if not DATA_DIR.exists():
        print(f"❌ DATA_DIR not found: {DATA_DIR}")
        sys.exit(1)
    print(os.listdir(DATA_DIR))

    for name, cfg in DATASETS.items():
        fp = DATA_DIR / cfg["filename"]
        if not fp.exists():
            print(f"\n⚠️ File missing for `{name}`: {cfg['filename']}")
            continue

        print(f"\n--- Reading `{cfg['filename']}` for dataset `{name}` ---")
        try:
            if name.startswith("liar_"):
                # Force the LIAR files to use our column names
                df = pd.read_csv(
                    fp,
                    sep=cfg["sep"],
                    header=None,
                    names=LIAR_COLUMNS,
                    encoding="utf-8",
                )
            else:
                # Load CSVs with their own headers
                df = pd.read_csv(fp, sep=cfg["sep"], encoding="utf-8")

                # ─── SMALL FIX: inject a "label" column for the true/fake files ───
                if name == "true":
                    df["label"] = "real"
                elif name == "fake":
                    df["label"] = "fake"

            explore_dataframe(df, name, cfg)

        except Exception as e:
            print(f"❌ Error loading `{cfg['filename']}`: {e}")

if __name__ == "__main__":
    main()
