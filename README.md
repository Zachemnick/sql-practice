# sql-practice

# SQL Project

A project for importing, storing, and analyzing data using Python, SQLite, and SQL.

## Project Structure

```text
sql/
├── README.md
├── .gitignore
├── import_data.py
├── llm.db
└── sql/
    ├── prompts.csv
    └── passages.csv
```

## Technologies

- Python
- SQLite
- Pandas
- SQLTools for VS Code

## Installation

Install Pandas:

```bash
pip install pandas
```

## Import Data

Run the import script:

```bash
python import_data.py
```

This creates the SQLite database `llm.db` and imports two CSV files into:

- `prompts`
- `passages`

## Example SQL Query

Find the five passages with the highest cost:

```sql
SELECT label, n_words, cost
FROM passages
ORDER BY cost DESC
LIMIT 5;
```

## Database

The project uses SQLite for storing and querying data.

The database is generated locally from the CSV files.

## Requirements

- Python 3.x
- Pandas
- prompts.csv
- passages.csv

## License

For educational purposes.
