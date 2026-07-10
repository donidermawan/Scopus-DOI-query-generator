#!/usr/bin/env python3
"""
===============================================================
Generate Scopus Search Queries from DOI List
===============================================================

Supported input:
    - TXT
    - XLSX
    - CSV

Output:
    output_queries/
        query_001.txt
        query_002.txt
        ...
        summary.csv

Author: Doni Dermawan
===============================================================
"""

import os
import math
import pandas as pd

# ===============================================================
# USER SETTINGS
# ===============================================================

# Input file
INPUT_FILE = "doi_list.xlsx"

# Number of DOIs per Scopus query
DOIS_PER_QUERY = 2000

# Output directory
OUTPUT_DIR = "output_queries"

# ===============================================================
# CREATE OUTPUT DIRECTORY
# ===============================================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===============================================================
# READ INPUT FILE
# ===============================================================

extension = os.path.splitext(INPUT_FILE)[1].lower()

print("=" * 70)
print("Reading DOI file...")
print("=" * 70)

if extension == ".txt":

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        doi_list = [line.strip() for line in f.readlines()]

elif extension == ".xlsx":

    df = pd.read_excel(INPUT_FILE)

    doi_column = None

    for col in df.columns:
        if "doi" in col.lower():
            doi_column = col
            break

    if doi_column is None:
        doi_column = df.columns[0]

    doi_list = df[doi_column].astype(str).tolist()

elif extension == ".csv":

    df = pd.read_csv(INPUT_FILE)

    doi_column = None

    for col in df.columns:
        if "doi" in col.lower():
            doi_column = col
            break

    if doi_column is None:
        doi_column = df.columns[0]

    doi_list = df[doi_column].astype(str).tolist()

else:
    raise Exception("Unsupported file format!")

# ===============================================================
# CLEAN DOI LIST
# ===============================================================

cleaned = []

for doi in doi_list:

    doi = str(doi).strip()

    if doi == "":
        continue

    if doi.lower() == "nan":
        continue

    cleaned.append(doi)

# Remove duplicates while preserving order
cleaned = list(dict.fromkeys(cleaned))

print(f"Total valid DOIs : {len(cleaned):,}")

# ===============================================================
# SPLIT INTO BATCHES
# ===============================================================

num_batches = math.ceil(len(cleaned) / DOIS_PER_QUERY)

print(f"Batch size       : {DOIS_PER_QUERY:,}")
print(f"Total batches    : {num_batches}")
print()

summary = []

# ===============================================================
# GENERATE QUERIES
# ===============================================================

for batch_number in range(num_batches):

    start = batch_number * DOIS_PER_QUERY
    end = min(start + DOIS_PER_QUERY, len(cleaned))

    batch = cleaned[start:end]

    query = " OR ".join(
        [f'DOI("{doi}")' for doi in batch]
    )

    filename = f"query_{batch_number + 1:03d}.txt"

    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(query)

    summary.append({
        "Batch": batch_number + 1,
        "Filename": filename,
        "Start DOI": start + 1,
        "End DOI": end,
        "DOIs": len(batch)
    })

    print(f"Created {filename:<18} ({len(batch)} DOIs)")

# ===============================================================
# SAVE SUMMARY
# ===============================================================

summary_df = pd.DataFrame(summary)

summary_file = os.path.join(OUTPUT_DIR, "summary.csv")

summary_df.to_csv(summary_file, index=False)

# ===============================================================
# FINISHED
# ===============================================================

print()
print("=" * 70)
print("Completed Successfully")
print("=" * 70)

print(f"Total DOIs      : {len(cleaned):,}")
print(f"Total batches   : {num_batches}")
print(f"Output folder   : {os.path.abspath(OUTPUT_DIR)}")
print(f"Summary file    : {summary_file}")
print("=" * 70)