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
from src.explore_details import DetailsData
from src.explore_summary import SummaryData


def main() -> None:
    cleaner = DatasetCleaner()
    batting_df, bowling_df, details_df, summary_df = cleaner.read_dataset()
    batting_df, bowling_df, details_df, summary_df = cleaner.clean_dataframe(
        batting_df, bowling_df, details_df, summary_df
    )

    # batsman = BattingData(batting_df)
    # print(batsman.best_batsman_per_game)
    # print(batsman.get_batsman_stats("Faf du Plessis"))
    # print(batsman.get_largest_total_for_wicket(1))
    # print(batsman.compare_all_performances())

    # bowler = BowlingData(bowling_df)
    # print(bowler.best_bowler_per_game())
    # print(bowler.get_tournament_stats())
    # print(bowler.compare_bowler_performances("Kagiso Rabada"))
    # print(bowler.compare_all_performances())

    # details = DetailsData(details_df)

    summary = SummaryData(summary_df)
    print(summary.analyze_result_vs_days())
    # print(summary.get_total_matches())
    # print(summary.get_team_wins("PC"))
    # print(summary.get_toss_decisions())
    # print(summary.get_highest_scores())
    # print(summary.get_lowest_scores())


if __name__ == "__main__":
    main()
