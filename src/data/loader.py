from pandas import DataFrame
from pathlib import Path
import pandas as pd

BASE_DIR = Path().cwd()
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
CUSTOMERS_RAW = RAW_DATA_DIR / "synthetic_sme_customers_processed.csv"
TRANSACTIONS_RAW = RAW_DATA_DIR / "synthetic_sme_transactions_processed.csv"

def load_datasets(
    customers_path: Path | str = "data/raw/synthetic_sme_customers_processed.csv",
    transactions_path: Path | str = "data/raw/synthetic_sme_transactions_processed.csv"
) -> tuple[DataFrame, DataFrame]:
    """
    Load customer and transaction data with optional paths.
    Assumes that the raw data is in data/raw/.
    """
    customers = pd.read_csv(customers_path)
    transactions = pd.read_csv(transactions_path)

    return customers, transactions