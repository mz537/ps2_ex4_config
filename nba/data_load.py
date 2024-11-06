import pandas as pd
from pathlib import Path


def load_csv(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)


if __name__ == "__main__":
    # TODO: fix this data path using the pathlib library
    data_path =Path(__file__).parent.parent / "data" / "game.csv" #changed the code based on the notes
    df = load_csv(data_path)
    print(data_path)
    print(df.head) #added this to show that the data_path code actually worked
