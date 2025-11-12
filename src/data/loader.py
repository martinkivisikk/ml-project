from pandas import DataFrame
from pathlib import Path
import pandas as pd

BASE_DIR = Path().cwd()
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
CUSTOMERS_RAW = RAW_DATA_DIR / "synthetic_sme_customers_processed.csv"
TRANSACTIONS_RAW = RAW_DATA_DIR / "synthetic_sme_transactions_processed.csv"

def load_datasets() -> tuple[DataFrame, DataFrame]:
    """
    Returns the customer and transaction data as dataframes.
    Assumes that the raw data is in data/raw/
    """
    customers = pd.read_csv(CUSTOMERS_RAW)
    transactions = pd.read_csv(TRANSACTIONS_RAW)

    return customers, transactions