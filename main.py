#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: main.py
Author: Keyan de Klerk
Email: keyan@deklerk.org.za
Description: Brief description of what the script does.
"""

from src import (
    process_dataset,
    explore_batting,
    explore_bowling,
    explore_details,
    explore_summary,
    visualize_information,
)


def main() -> None:
    cleaner = process_dataset.DatasetCleaner()
    batting_df, bowling_df, details_df, summary_df = cleaner.read_dataset()
    batting_df, bowling_df, details_df, summary_df = cleaner.clean_dataframe(
        batting_df, bowling_df, details_df, summary_df
    )

    batsman = explore_batting.BattingData(batting_df)

    bowler = explore_bowling.BowlingData(bowling_df)
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

    visualizer = visualize_information.VisualizeInformation()

    """
    visualizer.show_top10_batsman(batsman.get_all_performances())
    visualizer.show_best_batsman_per_game(batsman.best_batsman_per_game())
    visualizer.show_best_home_away_batsmen(
        batsman.compare_all_performances(),
        "Home",
    )
    visualizer.show_best_home_away_batsmen(
        batsman.compare_all_performances(),
        "Away",
    )
    visualizer.show_most_boundaries(batsman.get_all_performances())

    visualizer.show_top10_bowlers(bowler.get_all_performances())
    visualizer.show_best_bowler_per_game(bowler.best_bowler_per_game())
    visualizer.show_best_home_away_bowler(bowler.compare_all_performances(), "Home")
    visualizer.show_best_home_away_bowler(bowler.compare_all_performances(), "Away")
    """


if __name__ == "__main__":
    main()
