#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: main.py
Author: Keyan de Klerk
Email: keyan@deklerk.org.za
Description: Brief description of what the script does.
"""


from typing import Tuple

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


DATASET_DIRECTORY = "./input/"
BATTING_CSV = DATASET_DIRECTORY + "batting_card.csv"
BOWLING_CSV = DATASET_DIRECTORY + "bowling_card.csv"
DETAILS_CSV = DATASET_DIRECTORY + "details.csv"
SUMMARY_CSV = DATASET_DIRECTORY + "summary.csv"


def read_dataset(
    batting_card_path: str, bowling_card_path: str, details_path: str, summary_path: str
) -> Tuple[pd.DataFrame]:
    """Reads all the input CSV files into separate Pandas dataframes.

    Args:
        batting_card_path (str): CSV with all batting related information
        bowling_card_path (str): CSV with all bowling related information
        details_path (str): CSV with ball by ball details for each game
        summary_path (str): CSV with overview of the whole match

    Returns:
        Tuple[pd.DataFrame]: All the separate CSV files converted to dataframes
    """
    batting_df = pd.read_csv(batting_card_path)
    bowling_df = pd.read_csv(bowling_card_path)
    details_df = pd.read_csv(details_path)
    summary_df = pd.read_csv(summary_path)
    return batting_df, bowling_df, details_df, summary_df


def main(
    batting_card_path: str, bowling_card_path: str, details_path: str, summary_path: str
) -> None:
    batting_df, bowling_df, details_df, summary_df = read_dataset(
        batting_card_path, bowling_card_path, details_path, summary_path
    )


if __name__ == "__main__":
    main(BATTING_CSV, BOWLING_CSV, DETAILS_CSV, SUMMARY_CSV)
