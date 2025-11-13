from pandas import DataFrame
from pathlib import Path
import pandas as pd
import logging
from src.config.constants import CUSTOMERS_RAW_PATH, TRANSACTIONS_RAW_PATH, MERGED_DF_DEFAULT_PATH


logger = logging.getLogger(__name__)

def _safe_read_csv(path: Path | str) -> DataFrame:
    try:
        logger.info(f"Loading {path}")
        return pd.read_csv(path)
    except FileNotFoundError:
        logger.error(f"File not found: {path}. Returning empty DataFrame.")
        return pd.DataFrame()

def load_datasets(
    customers_path: Path | str = CUSTOMERS_RAW_PATH,
    transactions_path: Path | str = TRANSACTIONS_RAW_PATH
) -> tuple[DataFrame, DataFrame]:
    """
    Load customer and transaction data with optional paths.
    Assumes that the raw data is in data/raw/.
    """
    customers = _safe_read_csv(customers_path)
    transactions = _safe_read_csv(transactions_path)

    return customers, transactions

def merge_dataframes(customers_df: DataFrame, transactions_df: DataFrame) -> DataFrame:
    try:
        return pd.merge(transactions_df,  customers_df, on="cust_id")
    except KeyError:
        logger.error(
            "Merge failed because 'cust_id' is missing.\n"
            f"customers_df columns: {list(customers_df.columns)}\n"
            f"transactions_df columns: {list(transactions_df.columns)}"
        )
        return pd.DataFrame()
    
def save_merged_df(merged_df: DataFrame, save_path: Path | str = MERGED_DF_DEFAULT_PATH) -> None:
    merged_df.to_csv(save_path, index=False)
    logger.info(f"Saved merged dataframe to {save_path}")

def load_merged_df(merged_df_path: Path | str = MERGED_DF_DEFAULT_PATH) -> DataFrame:
    return _safe_read_csv(merged_df_path)