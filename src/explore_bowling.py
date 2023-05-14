from typing import Dict, Any
import pandas as pd
import numpy as np


class BowlingData:
    def __init__(self, bowling_df: pd.DataFrame):
        self.bowling_df = bowling_df

    def best_bowler_per_game(self) -> pd.DataFrame:
        """Returns the best bowler for each game along with their bowling statistics.

        Returns:
            pd.DataFrame: A dataframe containing the match_id, full name of the bowler,
            overs bowled, maidens bowled, runs conceded, wickets taken, and economy rate for
            the best bowler in each game.
        """
        # create a new dataframe to store the best bowler in each game
        best_bowler_df = pd.DataFrame(
            columns=[
                "match_id",
                "fullName",
                "overs",
                "maidens",
                "conceded",
                "wickets",
                "economyRate",
            ]
        ).reset_index(drop=True)

        # loop through each game in the data
        for match_id, game_data in self.bowling_df.groupby("match_id"):
            # find the row with the maximum wickets
            max_wickets_row = game_data.loc[game_data["wickets"].idxmax()]
            print(max_wickets_row)
            # if there are multiple rows with the maximum wickets, find the one with the lowest conceded
            if (game_data["wickets"] == max_wickets_row["wickets"]).sum() > 1:
                min_conceded_row = game_data.loc[game_data["conceded"].idxmin()]
                # if there are still multiple rows, find the one with the smallest economy rate
                if (game_data["conceded"] == min_conceded_row["conceded"]).sum() > 1:
                    best_bowler_row = game_data.loc[game_data["economyRate"].idxmin()]
                else:
                    best_bowler_row = min_conceded_row
            else:
                best_bowler_row = max_wickets_row

            # add the best bowler row to the new dataframe
            best_bowler_df = pd.concat(
                [
                    best_bowler_df,
                    best_bowler_row.loc[
                        [
                            "match_id",
                            "fullName",
                            "overs",
                            "maidens",
                            "conceded",
                            "wickets",
                            "economyRate",
                        ]
                    ]
                    .to_frame()
                    .T,
                ],
                ignore_index=True,
            )

        return best_bowler_df

    def calculate_balls(self, bowling_df):
        overs = int(bowling_df["overs"].sum())
        # sum the decimal parts of overs
        balls_decimal = (bowling_df["overs"].sum() - overs).sum()
        balls_bowled = overs * 6 + int(round(balls_decimal * 10))
        return balls_bowled

    def get_all_performances(self) -> pd.DataFrame:
        """
        Calculates and returns the tournament statistics for the bowlers.

        Returns:
            DataFrame: A pandas DataFrame containing the following columns:
                - fullName (str): The name of the bowler.
                - total_overs (float): The total number of overs bowled by the bowler.
                - total_wickets (int): The total number of wickets taken by the bowler.
                - total_maidens (int): The total number of maidens bowled by the bowler.
                - total_conceded (int): The total number of runs conceded by the bowler.
                - avg_economy_rate (float): The average economy rate of the bowler.
                - dot_balls (int): The total number of dot balls bowled by the bowler.
                - fours_conceded (int): The total number of fours conceded by the bowler.
                - sixes_conceded (int): The total number of sixes conceded by the bowler.
                - wides_bowled (int): The total number of wides bowled by the bowler.
                - no_balls_bowled (int): The total number of no-balls bowled by the bowler.
        """
        # Group by fullName and sum the desired columns
        grouped = self.bowling_df.groupby("fullName").agg(
            {
                "overs": "sum",
                "wickets": "sum",
                "maidens": "sum",
                "conceded": "sum",
                "economyRate": "mean",
                "dots": "sum",
                "foursConceded": "sum",
                "sixesConceded": "sum",
                "wides": "sum",
                "noballs": "sum",
            }
        )
        # Rename the columns
        grouped.columns = [
            "total_overs",
            "total_wickets",
            "total_maidens",
            "total_conceded",
            "avg_economy_rate",
            "dot_balls",
            "fours_conceded",
            "sixes_conceded",
            "wides_bowled",
            "no_balls_bowled",
        ]

        average = self.bowling_df.groupby("fullName").apply(
            lambda x: (x["conceded"].sum() / x["wickets"].sum())
            if x["wickets"].sum() != 0
            else np.NaN
        )

        grouped["average"] = average.values

        # Calculate bowling average for each player
        average = self.bowling_df.groupby("fullName").apply(
            lambda x: x["conceded"].sum() / x["wickets"].sum()
            if x["wickets"].sum() != 0
            else np.NaN
        )

        # Add bowling average to the grouped DataFrame
        grouped["average"] = average.values

        # apply the function to the "overs" column and create a new column "balls_bowled"
        balls_bowled = self.bowling_df.groupby("fullName").apply(self.calculate_balls)
        grouped["balls_bowled"] = balls_bowled.values

        # calculate total number of wickets taken by each player
        wickets_taken = (
            self.bowling_df["wickets"].groupby(self.bowling_df["fullName"]).sum()
        )

        # calculate strike rate for each player
        strike_rate = (balls_bowled / wickets_taken).replace(np.inf, np.nan)

        grouped["strike_rate"] = strike_rate.values

        # Reset the index
        return grouped.reset_index()

    def compare_bowler_performances(self, bowler_name: str) -> Dict[str, str]:
        """
        This function takes a pandas dataframe containing bowling statistics for a cricket tournament and a bowler name,
        and compares the bowler's performance at home versus away matches.

        Args:
        - df: pandas dataframe containing bowling statistics
        - bowler_name: string, the name of the bowler whose performance is to be compared

        Returns:
        - A dictionary containing the average runs conceded, wickets taken, economy rate, and bowling strike rate for the bowler
        at home and away matches.
        """

        # Filter the dataframe to include only the specified bowler's data
        bowler_df = self.bowling_df[self.bowling_df["fullName"] == bowler_name]

        # Split the data into home and away matches
        bowler_team = bowler_df["bowling_team"]
        home_df = bowler_df[bowler_df["home_team"] == bowler_team]
        away_df = bowler_df[bowler_df["away_team"] == bowler_team]

        # Calculate the average runs conceded, wickets taken, economy rate, and bowling strike rate for home and away matches
        home_runs = home_df["conceded"].mean()
        away_runs = away_df["conceded"].mean()

        home_wickets = home_df["wickets"].mean()
        away_wickets = away_df["wickets"].mean()

        home_economy = home_df["economyRate"].mean()
        away_economy = away_df["economyRate"].mean()

        if home_wickets != 0:
            home_strike_rate = home_df["overs"].sum() / home_wickets
        else:
            home_strike_rate = np.nan

        if away_wickets != 0:
            away_strike_rate = away_df["overs"].sum() / away_wickets
        else:
            away_strike_rate = np.nan

        # Create a dictionary to store the results
        results = {
            "bowler_name": bowler_name,
            "home_runs_conceded": home_runs,
            "away_runs_conceded": away_runs,
            "home_wickets_taken": home_wickets,
            "away_wickets_taken": away_wickets,
            "home_economy_rate": home_economy,
            "away_economy_rate": away_economy,
            "home_strike_rate": home_strike_rate,
            "away_strike_rate": away_strike_rate,
        }

        return results

    def compare_all_performances(self) -> pd.DataFrame:
        """
        This function takes a pandas dataframe containing bowling statistics for a cricket tournament, loops over every
        unique bowler in the dataframe, and creates a new dataframe with the performances for every bowler.

        Args:
        - df: pandas dataframe containing bowling statistics

        Returns:
        - A pandas dataframe containing the average runs conceded, wickets taken, economy rate, and bowling strike rate for
        every bowler in the input dataframe, at home and away matches.
        """

        bowler_names = self.bowling_df["fullName"].unique()

        results_list = []

        for bowler_name in bowler_names:
            bowler_results = self.compare_bowler_performances(bowler_name)
            results_list.append(bowler_results)

        results_df = pd.DataFrame(results_list)

        return results_df
