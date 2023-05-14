#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: main.py
Author: Keyan de Klerk
Email: keyan@deklerk.org.za
Description: Brief description of what the script does.
"""

from src import process_dataset, explore_batting, explore_bowling, explore_details, explore_summary


def main() -> None:
    cleaner = process_dataset.DatasetCleaner()
    batting_df, bowling_df, details_df, summary_df = cleaner.read_dataset()
    batting_df, bowling_df, details_df, summary_df = cleaner.clean_dataframe(
        batting_df, bowling_df, details_df, summary_df
    )

    # batsman = explore_batting.BattingData(batting_df)
    # print(batsman.best_batsman_per_game)
    # print(batsman.get_batsman_stats("Faf du Plessis"))
    # print(batsman.get_largest_total_for_wicket(1))
    # print(batsman.compare_all_performances())
    # print(batsman.get_all_performances())

    # bowler = explore_bowling.BowlingData(bowling_df)
    # print(bowler.best_bowler_per_game())
    # print(bowler.get_tournament_stats())
    # print(bowler.compare_bowler_performances("Kagiso Rabada"))
    # print(bowler.compare_all_performances())

    # details = explore_details.DetailsData(details_df)
    # probability_six_by_over, total_six_by_over = details.likelihood_of_six_per_over()
    # print(details.inning_density_of_runs())

    # summary = explore_summary.SummaryData(summary_df)
    # print(summary.analyze_result_vs_days())
    # print(summary.get_total_matches())
    # print(summary.get_team_wins("PC"))
    # print(summary.get_toss_decisions())
    # print(summary.get_highest_scores())
    # print(summary.get_lowest_scores())


if __name__ == "__main__":
    main()
