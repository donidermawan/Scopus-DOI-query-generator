# Scopus DOI Query Generator

Automatically generate **Scopus Advanced Search** queries from a list of DOI numbers.

This utility converts DOI lists stored in **TXT**, **CSV**, or **Excel (XLSX)** files into Scopus-compatible search queries that can be pasted directly into the Scopus Advanced Search interface.

The script automatically:

- Reads DOI lists from multiple file formats
- Detects the DOI column automatically
- Removes empty values
- Removes duplicate DOIs
- Splits large DOI collections into configurable batches
- Generates Scopus-ready query files
- Creates a summary report for all generated batches

---

## Features

- Supports **TXT**, **CSV**, and **XLSX** input files
- Automatic DOI column detection
- Duplicate DOI removal
- Preserves original DOI order
- Configurable batch size
- Generates multiple query files automatically
- Produces a CSV summary report
- Lightweight and easy to use

---

## Requirements

- Python 3.8+
- pandas

Install dependencies:

```bash
pip install pandas openpyxl
```

---

## Input Formats

### Excel (.xlsx)

Example:

| DOI |
|-----|
| 10.1016/j.caeo.2025.100292 |
| 10.1145/3767695.3769671 |
| 10.5130/AJCEB.v25i3/4.9847 |

---

### CSV

```text
DOI
10.1016/j.caeo.2025.100292
10.1145/3767695.3769671
10.5130/AJCEB.v25i3/4.9847
```

---

### TXT

```text
10.1016/j.caeo.2025.100292
10.1145/3767695.3769671
10.5130/AJCEB.v25i3/4.9847
```

---

## Configuration

Modify the following parameters inside the script:

```python
INPUT_FILE = "doi_list.xlsx"

DOIS_PER_QUERY = 2000

OUTPUT_DIR = "output_queries"
```

Parameter | Description
----------|------------
`INPUT_FILE` | Input DOI file
`DOIS_PER_QUERY` | Maximum number of DOIs per Scopus query
`OUTPUT_DIR` | Output directory

---

## Usage

Run the script:

```bash
python generate_scopus_queries.py
```

Example output:

```
======================================================================
Reading DOI file...
======================================================================
Total valid DOIs : 4,532
Batch size       : 2,000
Total batches    : 3

Created query_001.txt (2000 DOIs)
Created query_002.txt (2000 DOIs)
Created query_003.txt (532 DOIs)

======================================================================
Completed Successfully
======================================================================
```

---

## Output Structure

```
output_queries/
│
├── query_001.txt
├── query_002.txt
├── query_003.txt
└── summary.csv
```

---

## Example Generated Query

```text
DOI("10.1016/j.caeo.2025.100292") OR DOI("10.1145/3767695.3769671") OR DOI("10.5130/AJCEB.v25i3/4.9847")
```

Simply copy and paste the generated query into the **Scopus Advanced Search** page.

---

## Summary Report

The generated `summary.csv` contains:

| Batch | Filename | Start DOI | End DOI | DOIs |
|-------|----------|-----------|---------|------|
| 1 | query_001.txt | 1 | 2000 | 2000 |
| 2 | query_002.txt | 2001 | 4000 | 2000 |
| 3 | query_003.txt | 4001 | 4532 | 532 |

---

## Typical Workflow

```
DOI List
      │
      ▼
Read Input File
      │
      ▼
Clean DOI List
      │
      ▼
Remove Duplicates
      │
      ▼
Split into Batches
      │
      ▼
Generate Scopus Queries
      │
      ▼
Export Query Files
      │
      ▼
summary.csv
```

---

## Use Cases

This script is useful for:

- Bibliometric analysis
- Systematic literature reviews
- Evidence synthesis
- Scopus record retrieval
- Bibliometrix/Biblioshiny workflows
- Large-scale DOI-based searches
- Research data collection

---

## License

MIT License

---

## Author

**Doni Dermawan**

If this project helps your research, consider giving it a ⭐ on GitHub.
