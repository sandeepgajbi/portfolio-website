import streamlit as st
import pandas as pd
import intro
from typing import Any, Tuple

CSV_FILE_PATH: str = "data.csv"
PHOTO_PATH: str = "images/photo.jpg"
IMAGE_PATH: str = "images/"
NAME: str = "Sandeep Gajbi"


def read_csv_file(file_path: str, pandas_module: pd) -> pd.DataFrame:
    """Reads a CSV file using pandas."""
    try:
        return pandas_module.read_csv(file_path, sep=";")
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
        return pd.DataFrame()


def display_portfolio_header(streamlit_module: Any) -> None:
    """Displays the portfolio header."""
    streamlit_module.set_page_config(layout="wide")
    col1, col2 = streamlit_module.columns(2)

    with col1:
        streamlit_module.image(PHOTO_PATH, use_column_width="auto", output_format="auto")

    with col2:
        streamlit_module.title(NAME)
        streamlit_module.info(intro.CONTENT)


def display_app_details(streamlit_module: Any, col: Any, df: pd.DataFrame, start_index: int, end_index: int) -> None:
    """Displays details of the apps."""
    with col:
        for index, row in df[start_index:end_index].iterrows():
            streamlit_module.header(row["title"])
            streamlit_module.write(row["description"])
            streamlit_module.image(IMAGE_PATH + row["image"])
            streamlit_module.write(f"[Source Code]({row['url']})")


def main() -> None:
    display_portfolio_header(st)
    st.subheader("Below you can find some of the apps I have built in Python.")
    col3, _, col4 = st.columns([1.5, 0.5, 1.5])

    df = read_csv_file(CSV_FILE_PATH, pd)
    if not df.empty:
        display_app_details(st, col3, df, 0, 10)
        display_app_details(st, col4, df, 10, len(df))


if __name__ == "__main__":
    main()
