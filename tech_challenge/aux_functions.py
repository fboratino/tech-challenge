import numpy as np


def validate_int(dataframe):
    not_int = []
    for col in dataframe:
        if not np.array_equal(dataframe[col], dataframe[col].astype(int)):
            not_int.append(col)
    return not_int


def get_create_table_command(dataframe):
    not_int = validate_int(dataframe)
    for col in dataframe:
        if col not in not_int:
            print(f"{col} smallint,")
        if col in not_int and len(str(max(dataframe[col]))) > 10:
            print(f"{col} double precision,")
        elif col in not_int:
            print(f"{col} decimal,")
