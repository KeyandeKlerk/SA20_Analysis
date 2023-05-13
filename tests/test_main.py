import pytest
import pandas as pd
import sys

sys.path.append("..")  # Add parent directory to Python path

from main import read_dataset


def test_read_dataset():
    batting_card_path = "./input/batting_card.csv"
    bowling_card_path = "./input/bowling_card.csv"
    details_path = "./input/details.csv"
    summary_path = "./input/summary.csv"

    # Call the read_dataset function to read the CSV files
    batting_df, bowling_df, details_df, summary_df = read_dataset(
        batting_card_path, bowling_card_path, details_path, summary_path
    )

    # Check that all dataframes are not empty
    assert not batting_df.empty
    assert not bowling_df.empty
    assert not details_df.empty
    assert not summary_df.empty

    # Check that the number of columns is correct for each dataframe
    assert batting_df.shape[1] == 25
    assert bowling_df.shape[1] == 24
    assert details_df.shape[1] == 44
    assert summary_df.shape[1] == 45

    # Check that the column names are correct for each dataframe
    assert list(batting_df.columns) == [
        "season",
        "match_id",
        "match_name",
        "home_team",
        "away_team",
        "venue",
        "city",
        "country",
        "current_innings",
        "innings_id",
        "name",
        "fullName",
        "runs",
        "ballsFaced",
        "minutes",
        "fours",
        "sixes",
        "strikeRate",
        "captain",
        "isNotOut",
        "runningScore",
        "runningOver",
        "shortText",
        "commentary",
        "link",
    ]
    assert list(bowling_df.columns) == [
        "season",
        "match_id",
        "match_name",
        "home_team",
        "away_team",
        "bowling_team",
        "venue",
        "city",
        "country",
        "innings_id",
        "name",
        "fullName",
        "overs",
        "maidens",
        "conceded",
        "wickets",
        "economyRate",
        "dots",
        "foursConceded",
        "sixesConceded",
        "wides",
        "noballs",
        "captain",
        "href",
    ]
    assert list(details_df.columns) == [
        "comment_id",
        "match_id",
        "match_name",
        "home_team",
        "away_team",
        "current_innings",
        "innings_id",
        "over",
        "ball",
        "runs",
        "shortText",
        "isBoundary",
        "isWide",
        "isNoball",
        "batsman1_id",
        "batsman1_name",
        "batsman1_runs",
        "batsman1_balls",
        "bowler1_id",
        "bowler1_name",
        "bowler1_overs",
        "bowler1_maidens",
        "bowler1_runs",
        "bowler1_wkts",
        "batsman2_id",
        "batsman2_name",
        "batsman2_runs",
        "batsman2_balls",
        "bowler2_id",
        "bowler2_name",
        "bowler2_overs",
        "bowler2_maidens",
        "bowler2_runs",
        "bowler2_wkts",
        "wicket_id",
        "wkt_batsman_name",
        "wkt_bowler_name",
        "wkt_batsman_runs",
        "wkt_batsman_balls",
        "wkt_text",
        "isRetiredHurt",
        "text",
        "preText",
        "postText",
    ]
    assert list(summary_df.columns) == [
        "season",
        "id",
        "name",
        "short_name",
        "description",
        "home_team",
        "away_team",
        "toss_won",
        "decision",
        "1st_inning_score",
        "2nd_inning_score",
        "home_score",
        "away_score",
        "winner",
        "result",
        "start_date",
        "end_date",
        "venue_id",
        "venue_name",
        "home_captain",
        "away_captain",
        "pom",
        "points",
        "super_over",
        "home_overs",
        "home_runs",
        "home_wickets",
        "home_boundaries",
        "away_overs",
        "away_runs",
        "away_wickets",
        "away_boundaries",
        "highlights",
        "home_key_batsman",
        "home_key_bowler",
        "home_playx1",
        "away_playx1",
        "away_key_batsman",
        "away_key_bowler",
        "match_days",
        "umpire1",
        "umpire2",
        "tv_umpire",
        "referee",
        "reserve_umpire",
    ]
