#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: main.py
Author: Keyan de Klerk
Email: keyan@deklerk.org.za
Description: Brief description of what the script does.
"""


from src.process_dataset import DatasetCleaner
from src.explore_batting import BattingData
from src.explore_bowling import BowlingData


def main() -> None:
    cleaner = DatasetCleaner()
    batting_df, bowling_df, details_df, summary_df = cleaner.read_dataset()
    batting_df, bowling_df, details_df, summary_df = cleaner.clean_dataframe(
        batting_df, bowling_df, details_df, summary_df
    )

    batsman = BattingData(batting_df)
    # print(batsman.best_batsman_per_game)
    # print(batsman.get_batsman_stats("Faf du Plessis"))
    # print(batsman.get_largest_total_for_wicket(1))

    bowler = BowlingData(bowling_df)
    # print(bowler.best_bowler_per_game())
    # print(bowler.get_tournament_stats())
    # print(bowler.compare_bowler_performances("Kagiso Rabada"))
    # print(bowler.compare_all_performances())


if __name__ == "__main__":
    main()
