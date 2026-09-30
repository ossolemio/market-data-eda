# Data Contract

## Expected columns

- `timestamp`: Observation timestamp in ISO 8601 format.
- `open`: Opening price.
- `high`: Highest observed price in the interval.
- `low`: Lowest observed price in the interval.
- `close`: Closing price.
- `volume`: Traded volume when available.

## Assumptions

- Each row represents one completed bar.
- Timestamps must be unique after cleaning.
- Prices must be strictly positive.
- OHLC relationships must be valid:
  - high >= open, close, low
  - low <= open, close, high

## Scope

The initial analysis uses one instrument and one daily frequency.
