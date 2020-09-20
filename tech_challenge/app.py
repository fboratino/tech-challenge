import pandas as pd
from crawler import download_file, get_dataframe_from_file
from loguru import logger
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://tech-challenge:tech-challenge@localhost:5432/tech_challenge",
    echo=True,
)

def fillna(dataframe):
    for df in dataframe:
        dataframe[df] = dataframe.fillna(-1)

if __name__ == "__main__":

    download_file()
    df = get_dataframe_from_file()
    fillna(df)
    
    # logger.info(df)

    # for df in dataframes:
        
    df['DEMO'].to_sql("demographics", con=engine, index=False, if_exists="replace")
    df['DR1IFF'].to_sql("dietry_individual_foods_first_day", con=engine, index=False, if_exists="replace")

    # # show records
    # conn = engine.connect()
    # # dataFrame = pd.read_sql('select * from "customers"', conn)
    # dataFrame = pd.read_sql_table("customers", engine)
    # conn.close()

    # logger.info(dataFrame)
