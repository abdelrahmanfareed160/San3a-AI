import pandas as pd

class FunctionsMap():

    PANDAS_MAP = {
        "text/csv" : pd.read_csv,
        "application/vnd.ms-excel" : pd.read_excel,
        "application/json": pd.read_json
    }
