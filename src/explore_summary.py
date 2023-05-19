from typing import Dict
import pandas as pd


class SummaryData:
    def __init__(self, summary_df: pd.DataFrame):
        self.summary_df = summary_df

    def get_total_matches(self) -> int:
        """
        Returns the total number of matches played in the tournament.

        Returns:
            int: Total number of matches played in the tournament.
        """
        return len(self.summary_df)

    def get_team_wins(self, team_name: str) -> Dict[str, int]:
        """
        Returns the total number of wins for the given team in the tournament.

        Args:
            team_name (str): Name of the team to get the total wins for.

        Returns:
            dict: A dictionary containing the number of home_wins, away_wins, and total_wins for the given team.
        """
        home_wins = len(
            self.summary_df[
                (self.summary_df["home_team"] == team_name)
                & (self.summary_df["winner"] == team_name)
            ]
        )
        away_wins = len(
            self.summary_df[
                (self.summary_df["away_team"] == team_name)
                & (self.summary_df["winner"] == team_name)
            ]
        )
        return {
            "home_wins": home_wins,
            "away_wins": away_wins,
            "total_wins": home_wins + away_wins,
        }

    def get_toss_decisions(self) -> Dict[str, int]:
        """
        Returns a dictionary of all the toss decisions made in the tournament and their frequencies.

        Returns:
            dict: A dictionary containing all the toss decisions made in the tournament and their frequencies.
        """
        return self.summary_df["decision"].value_counts().to_dict()

    def get_highest_scores(self) -> Dict[str, Dict[str, int]]:
        """
        Returns a dictionary of the highest scores in the tournament, with the team name and score.

        Returns:
            A dictionary with keys '1st Inning' and '2nd Inning', each containing a dictionary with keys 'Team' and 'Score'
        """
        self.summary_df["1st_inning_score"] = pd.to_numeric(
            self.summary_df["1st_inning_score"], errors="coerce"
        )
        highest_1st_inn_score = self.summary_df.loc[
            self.summary_df["1st_inning_score"].idxmax()
        ]
        self.summary_df["2nd_inning_score"] = pd.to_numeric(
            self.summary_df["2nd_inning_score"], errors="coerce"
        )
        highest_2nd_inn_score = self.summary_df.loc[
            self.summary_df["2nd_inning_score"].idxmax()
        ]
        return {
            "1st Inning": {
                "Team": highest_1st_inn_score["winner"],
                "Score": highest_1st_inn_score["1st_inning_score"],
            },
            "2nd Inning": {
                "Team": highest_2nd_inn_score["winner"],
                "Score": highest_2nd_inn_score["2nd_inning_score"],
            },
        }

    def get_lowest_scores(self) -> Dict[str, Dict[str, int]]:
        """
        Returns a dictionary of the lowest scores in the tournament, with the team name and score.

        Returns:
            A dictionary with keys '1st Inning' and '2nd Inning', each containing a dictionary with keys 'Team' and 'Score'
        """
        self.summary_df["1st_inning_score"] = pd.to_numeric(
            self.summary_df["1st_inning_score"], errors="coerce"
        )
        highest_1st_inn_score = self.summary_df.loc[
            self.summary_df["1st_inning_score"].idxmin()
        ]
        self.summary_df["2nd_inning_score"] = pd.to_numeric(
            self.summary_df["2nd_inning_score"], errors="coerce"
        )
        highest_2nd_inn_score = self.summary_df.loc[
            self.summary_df["2nd_inning_score"].idxmin()
        ]
        return {
            "1st Inning": {
                "Team": highest_1st_inn_score["winner"],
                "Score": highest_1st_inn_score["1st_inning_score"],
            },
            "2nd Inning": {
                "Team": highest_2nd_inn_score["winner"],
                "Score": highest_2nd_inn_score["2nd_inning_score"],
            },
        }

    def analyze_result_vs_days(self) -> pd.DataFrame:
        """The output is a pandas DataFrame with the winning team names in the columns and days between games in the index.
        The values in the cells represent the proportion of games won by each team for a particular number of days between games.

        For example, the first row with index value -11.0 represents the proportion of games won by each team when there are 11 days between games.
        The value for "Capitals" is 0.0, meaning they did not win any games when there were 11 days between games. The value for "Super Kings" is 1.0,
        meaning they won all their games when there were 11 days between games.

        Similarly, the second row with index value -7.0 represents the proportion of games won by each team when there are 7 days between games.
        The value for "Super Kings" is 1.0, meaning they won all their games when there were 7 days between games.

        You can use this output to observe the relationship between the number of days between games and the proportion of games won by each team.
        For example, you can see that for most values of days between games, "Super Kings" have a higher proportion of wins compared to other teams.
        However, for some values of days between games (e.g. -3.0), "Capitals" have a higher proportion of wins compared to other teams.

        Returns:
            pd.Dataframe: dataframe containing all teams and their respective win rates compared to game break
        """
        # convert start_date and end_date columns to datetime format
        self.summary_df["start_date"] = pd.to_datetime(self.summary_df["start_date"])
        self.summary_df["end_date"] = pd.to_datetime(self.summary_df["end_date"])

        # extract the name of the winning team from the 'result' column
        self.summary_df["winning_team"] = (
            self.summary_df["result"].str.split(" won").str[0]
        )

        # calculate the number of days between consecutive games
        self.summary_df["start_date"] = pd.to_datetime(
            self.summary_df["start_date"], format="%Y-%m-%dT%H:%M%z"
        )
        self.summary_df["days_between_games"] = (
            self.summary_df.groupby("winning_team")["start_date"]
            .diff()  # type: ignore
            .dt.days
        )

        # group by days between games and calculate the average result for each group
        result_by_days = (
            self.summary_df.groupby("days_between_games")["winning_team"]
            .value_counts(normalize=True)
            .unstack()
            .fillna(0)
        )

        result_by_days.drop(
            ["Starts at 17:30 local time", "No result"], axis=1, inplace=True
        )
        result_by_days = result_by_days.loc[~(result_by_days == 0).all(axis=1)]
        return result_by_days
