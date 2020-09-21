import pandas as pd
from crawler import download_file, get_dataframe_from_file
from loguru import logger
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://tech-challenge:tech-challenge@localhost:5432/tech_challenge",
    echo=False,
)


def data_frame_adjustments(dataframe):
    dataframe = dataframe.round(10)
    dataframe.columns = map(str.lower, dataframe.columns)
    for df in dataframe:
        dataframe[df] = dataframe[df].fillna(-1)
    return dataframe


if __name__ == "__main__":

    download_file()
    dataframe = get_dataframe_from_file()
    for df in dataframe:
        dataframe[df] = data_frame_adjustments(dataframe[df])
        dataframe[df]. \
            to_sql(df.lower(), con=engine, index=False, if_exists="append")

    # show records
    conn = engine.connect()
    sql_data = pd.read_sql('select * from "demo" limit 10', conn)
    conn.close()

    logger.info(sql_data)
