import pandas as pd
import requests
from bs4 import BeautifulSoup

website = "https://wwwn.cdc.gov"

files = {
    "DEMO_J.XPT": "https://wwwn.cdc.gov/nchs/nhanes/Search/DataPage.aspx?\
Component=Demographics&CycleBeginYear=2017",
    "DR1IFF_J.XPT": "https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?\
Component=Dietary&CycleBeginYear=2017",
}


def get_webpage_data(url) -> str:
    return requests.get(url).text


def parse_webpage_data(url) -> "class":
    parsed_webpage = BeautifulSoup(get_webpage_data(url), "html.parser")
    return parsed_webpage


def get_filepath_from_webpage(filename, url) -> str:
    for link in parse_webpage_data(url).find_all("a"):
        if filename in link.get("href"):
            filepath = website + link.get("href")
    return filepath


def get_all_filepaths() -> dict:
    filepaths = {}
    for filename, url in files.items():
        filepaths[filename] = get_filepath_from_webpage(filename, url)
    return filepaths


def download_file():
    for filename, filepath in get_all_filepaths().items():
        file = requests.get(filepath, allow_redirects=True)
        open(filename, "wb").write(file.content)


def get_dataframe_from_file() -> dict:
    dataframes = {}
    for filename in files:
        dataframes[filename.split("_")[0]] = pd.read_sas(filename)
    return dataframes
