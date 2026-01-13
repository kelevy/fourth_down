from pathlib import Path
import pandas as pd

DEFAULT_SEASONS = [2022, 2023, 2024]

def load_pbp(seasons=DEFAULT_SEASONS) -> pd.DataFrame:
    import nfl_data_py as nfl
    return nfl.import_pbp_data(seasons, downcast=True, cache=True)

def read_parquet_or_none(path: Path):
    if path.exists():
        return pd.read_parquet(path)
    return None
