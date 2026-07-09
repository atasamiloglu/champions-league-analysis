import pandas as pd

def load_matches():
    df = pd.read_excel(
        "data/ChampionsLeague/ucl_data.xlsx",
        sheet_name="matches"
    )
    return df