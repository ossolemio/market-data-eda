from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {
    "timestamp",
    "open",
    "high",
    "low",
    "close",
    "volume",
}


def load_ohlcv_csv(path: str | Path) -> pd.DataFrame:
    """Load OHLCV data from a CSV file and validate required columns."""
    dataframe = pd.read_csv(path)

    missing_columns = REQUIRED_COLUMNS.difference(dataframe.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Missing required columns: {missing}")

    return dataframe
