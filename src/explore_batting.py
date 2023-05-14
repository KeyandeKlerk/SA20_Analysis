from typing import Any, Dict
import ast

import pandas as pd
import numpy as np


class BattingData:
    def __init__(self, batting_df: pd.DataFrame):
        self.batting_df = batting_df

    def best_batsman_per_game(self) -> pd.DataFrame:
        # create a new dataframe to store the best batsman in each game
        best_batsman_df = pd.DataFrame(
            columns=['match_id', 'fullName', 'runs'])

        # loop through each game in the data
        for match_id in self.batting_df['match_id'].unique():
            # subset the data to only include the current game
            game_data = self.batting_df[self.batting_df['match_id'] == match_id]

            # calculate the batting average for each batsman in the game
            batting_averages = game_data.groupby('fullName')['runs'].mean()

            # get the batsman with the highest batting average
            best_batsman = batting_averages.idxmax()

            # get the score of the best batsman
            score = game_data.loc[game_data['fullName']
                                  == best_batsman, 'runs'].sum()

            # add the best batsman and their score to the new dataframe
            new_row = {'match_id': match_id,
                       'fullName': best_batsman, 'runs': score}
            best_batsman_df = pd.concat(
                [best_batsman_df, pd.DataFrame(new_row, index=[0])], ignore_index=True)
        return best_batsman_df

    def get_batsman_stats(self, batsman_name: str) -> pd.DataFrame:
        return self.batting_df.loc[self.batting_df["fullName"] == batsman_name, ["match_id", "runs", "ballsFaced", "fours", "sixes", "strikeRate", "isNotOut"]]

    def get_largest_total_for_wicket(self, wicket_number: int) -> Dict[str, Any]:
        # Extract dictionary from string
        self.batting_df['score_dict'] = self.batting_df['runningScore'].apply(
            lambda x: ast.literal_eval(x) if isinstance(x, str) else {})

        # Filter the rows where wickets == wicket_number
        wicket_filter = self.batting_df['score_dict'].apply(
            lambda x: 'wickets' in x and x['wickets'] == wicket_number)
        filtered_df = self.batting_df[wicket_filter]

        # Find the row with the highest runs value
        max_runs_row = filtered_df.loc[filtered_df['score_dict'].apply(lambda x: 'runs' in x),
                                       'score_dict'].apply(pd.Series)['runs'].idxmax()
        max_runs = filtered_df.loc[max_runs_row]['score_dict']['runs']

        # Get the match_id and match_name for the row with the highest runs value
        match_id = filtered_df.loc[max_runs_row, 'match_id']
        match_name = filtered_df.loc[max_runs_row, 'match_name']

        return {'match_id': match_id, 'match_name': match_name, 'max_runs': max_runs}

    def compare_batsman_performances(self, batsman_name: str) -> Dict[str, str]:
        """
        This function takes a pandas dataframe containing batting statistics for a cricket tournament and a batsman name,
        and compares the batsman's performance at home versus away matches.

        Args:
        - df: pandas dataframe containing batting statistics
        - batsman_name: string, the name of the batsman whose performance is to be compared

        Returns:
        - A dictionary containing the average runs scored, balls faced, strike rate, and batting strike rate for the batsman
        at home and away matches.
        """

        # Filter the dataframe to include only the specified batsman's data
        batsman_df = self.batting_df[self.batting_df['fullName']
                                     == batsman_name]

        # Split the data into home and away matches
        batsman_team = batsman_df["current_innings"]
        home_df = batsman_df[batsman_df['home_team'] == batsman_team]
        away_df = batsman_df[batsman_df["away_team"] == batsman_team]

        # Calculate the average runs scored, balls faced, strike rate, and batting strike rate for home and away matches
        home_runs = home_df['runs'].mean()
        away_runs = away_df['runs'].mean()

        home_balls_faced = home_df['ballsFaced'].mean()
        away_balls_faced = away_df['ballsFaced'].mean()

        home_strike = home_df['strikeRate'].mean()
        away_strike = away_df['strikeRate'].mean()

        # Create a dictionary to store the results
        results = {
            'batsman_name': batsman_name,
            'home_runs_scored': home_runs,
            'away_runs_scored': away_runs,
            'home_balls_faced': home_balls_faced,
            'away_balls_faced': away_balls_faced,
            'home_strike_rate': home_strike,
            'away_strike_rate': away_strike,
        }

        return results

    def compare_all_performances(self) -> pd.DataFrame:
        """
        This function takes a pandas dataframe containing batting statistics for a cricket tournament, loops over every
        unique batsman in the dataframe, and creates a new dataframe with the performances for every batsman.

        Args:
        - df: pandas dataframe containing batting statistics

        Returns:
        - A pandas dataframe containing the average runs scored, balls faced and batting strike rate for
        every batsman in the input dataframe, at home and away matches.
        """

        batsman_names = self.batting_df['fullName'].unique()

        results_list = []

        for batsman_name in batsman_names:
            batsman_results = self.compare_batsman_performances(batsman_name)
            results_list.append(batsman_results)

        results_df = pd.DataFrame(results_list)

        return results_df
