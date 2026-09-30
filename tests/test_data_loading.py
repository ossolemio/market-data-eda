import pandas as pd
import pytest

from src.market_data_eda.data_loading import load_ohlcv_csv


def test_load_ohlcv_csv_returns_dataframe(tmp_path):
    # Create a temporary CSV file with valid OHLCV data
    csv_file = tmp_path / "valid_ohlcv.csv"
    csv_file.write_text(
        "timestamp,open,high,low,close,volume\n2026-09-28,100,106,98,104,250000\n",
        encoding="utf-8",
    )
    result = load_ohlcv_csv(csv_file)
    # Check if the result is a DataFrame and has the correct columns
    assert isinstance(result, pd.DataFrame)


def test_load_ohlcv_csv_missing_columns(tmp_path):

    # Create a temporary CSV file with missing required columns
    csv_file = tmp_path / "missing_columns.csv"
    csv_file.write_text(
        "timestamp,open,high,low,close\n2026-09-28,100,106,98,104\n",
        encoding="utf-8",
    )

    # Expect a ValueError due to missing 'volume' column
    with pytest.raises(
        ValueError, match="Missing required columns: volume"
    ) as exc_info:
        load_ohlcv_csv(csv_file)

    assert "Missing required columns: volume" in str(exc_info.value)
