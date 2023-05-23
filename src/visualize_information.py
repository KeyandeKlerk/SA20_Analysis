from typing import Dict, Tuple
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd
import numpy as np

# Define a color dictionary mapping team names to colors
TEAM_COLOURS = {
    "PR": "pink",
    "JSK": "blue",
    "DSG": "green",
    "PC": "red",
    "MICT": "gold",
    "SEC": "orange",
}


class VisualizeInformation:
    def show_top10_batsman(self, all_performances: pd.DataFrame) -> None:
        # Create a new dataframe with the top 10 players based on total_runs
        top_10_players = all_performances.nlargest(10, "total_runs")

        # Create the bar chart with different colors
        bars = plt.bar(
            top_10_players["fullName"],
            top_10_players["total_runs"],
            color=[TEAM_COLOURS.get(team, "gray") for team in top_10_players["team"]],
        )

        # Create a list of unique teams
        unique_teams = top_10_players["team"].unique()

        # Create a list of legend handles
        legend_handles = [
            Patch(facecolor=TEAM_COLOURS.get(team, "gray"), edgecolor="black")
            for team in unique_teams
        ]

        # Create the legend
        plt.legend(legend_handles, unique_teams, loc="upper right")

        plt.xlabel("Player Name")
        plt.ylabel("Total Runs")
        plt.title("Top 10 Players by Total Runs")

        # Rotate x-axis tick labels by 45 degrees
        plt.xticks(rotation=45, ha="right")

        # Adjust the layout to avoid overlapping labels
        plt.tight_layout()

        # Save the bar chart to a folder (change the path as per your requirement)
        plt.savefig("result/batsman_graphs/top_10_batsmen.png")

    def show_best_batsman_per_game(self, best_df: pd.DataFrame) -> None:
        # Visualize the lowest_scores
        plt.figure(figsize=(10, 6))
        plt.bar(
            best_df["match_id"] - 1343940,
            best_df["runs"],
        )
        plt.xlabel("Game Number")
        plt.ylabel("Runs")
        plt.title("Most Runs per Game")

        plt.xticks(
            range(1, len(best_df) + 1),
            range(1, len(best_df) + 1),
            rotation=45,
            ha="right",
        )
        # Adjust the layout to avoid overlapping labels
        plt.tight_layout()

        # Save the bar chart to a folder (change the path as per your requirement)
        plt.savefig("result/batsman_graphs/best_batsman_per_game.png")

    def show_best_home_away_batsmen(
        self,
        batsman_df: pd.DataFrame,
        home_or_away: str,
    ) -> None:
        runs_column = f"{str.lower(home_or_away)}_runs_scored"
        strike_rate_column = f"{str.lower(home_or_away)}_strike_rate"
        # Sort the dataframe by average home runs in descending order
        sorted_df = batsman_df.sort_values(by=runs_column, ascending=False)

        # Get the top N batsmen by average runs
        top_batsmen = sorted_df.head(10)

        # Set the width of the bars
        bar_width = 0.8

        # Create an array of indices for the x-axis ticks
        indices = np.arange(len(top_batsmen))

        # Plot the average runs as a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(
            indices,
            top_batsmen[runs_column],
            label="Average Runs",
            width=bar_width,
        )

        # Plot the average runs as a scatter plot with dots
        plt.scatter(
            indices,
            top_batsmen[strike_rate_column],
            label="Average Strike Rate",
            color="red",
        )

        # Set the x-axis ticks and labels
        plt.xticks(
            indices,
            top_batsmen["batsman_name"],
            rotation=45,
            ha="right",
        )

        # Set the y-axis label
        plt.ylabel("Runs / Strike Rate")

        # Set the chart title
        plt.title(f"Top 10 {home_or_away} Batsmen by Average Runs")

        # Add a legend
        plt.legend()

        # Adjust the layout
        plt.tight_layout()

        # Save the plot to a file
        plt.savefig(f"result/batsman_graphs/best_{str.lower(home_or_away)}_batsmen.png")

        # Show the plot

    def show_most_boundaries(self, all_performances: pd.DataFrame):
        # Create a new dataframe with the top 10 players based on total_runs
        top_10_players = all_performances.nlargest(10, "boundary_percentage")

        # Create the bar chart with different colors
        bars = plt.bar(
            top_10_players["fullName"],
            top_10_players["boundary_percentage"],
            color=[TEAM_COLOURS.get(team, "gray") for team in top_10_players["team"]],
        )

        # Create a list of unique teams
        unique_teams = top_10_players["team"].unique()

        # Create a list of legend handles
        legend_handles = [
            Patch(facecolor=TEAM_COLOURS.get(team, "gray"), edgecolor="black")
            for team in unique_teams
        ]

        # Create the legend
        plt.legend(legend_handles, unique_teams, loc="upper right")

        plt.xlabel("Player Name")
        plt.ylabel("Boundary %")
        plt.title("Top 10 Players by Boundary Percentage")

        # Rotate x-axis tick labels by 45 degrees
        plt.xticks(rotation=45, ha="right")

        # Adjust the layout to avoid overlapping labels
        plt.tight_layout()

        # Save the bar chart to a folder (change the path as per your requirement)
        plt.savefig("result/batsman_graphs/top_10_boundary_percentage.png")

    def show_top10_bowlers(self, bowling_df: pd.DataFrame) -> None:
        # Create a new dataframe with the top 10 players based on total_runs
        top_10_players = bowling_df.nlargest(10, "total_wickets")

        # Create the bar chart with different colors
        fig, ax = plt.subplots()  # Create a figure and axis object

        bars = ax.bar(
            top_10_players["fullName"],
            top_10_players["total_wickets"],
            color=[TEAM_COLOURS.get(team, "gray") for team in top_10_players["team"]],
        )

        # Create a list of unique teams
        unique_teams = top_10_players["team"].unique()

        # Create a list of legend handles
        legend_handles = [
            Patch(facecolor=TEAM_COLOURS.get(team, "gray"), edgecolor="black")
            for team in unique_teams
        ]

        # Create the legend
        ax.legend(legend_handles, unique_teams, loc="upper right")

        plt.xlabel("Player Name")
        plt.ylabel("Total Wickets")
        plt.title("Top 10 Players by Total Wickets")

        # Rotate x-axis tick labels by 45 degrees
        plt.xticks(rotation=45, ha="right")

        # Adjust the layout to avoid overlapping labels
        plt.tight_layout()

        # Save the bar chart to a folder (change the path as per your requirement)
        plt.savefig("result/bowler_graphs/top_10_bowlers.png")

    def show_best_bowler_per_game(self, best_df: pd.DataFrame) -> None:
        # Visualize the lowest_scores
        plt.figure(figsize=(10, 6))
        plt.bar(
            best_df["match_id"] - 1343940,
            best_df["wickets"],
        )
        # Plot the average runs as a scatter plot with dots
        plt.scatter(
            best_df["match_id"] - 1343940,
            best_df["economyRate"],
            label="Economy Rate",
            color="red",
        )
        plt.xlabel("Game Number")
        plt.ylabel("Wickets/Economy Rate")
        plt.title("Most Wickets/Economy Rate per Game")

        plt.xticks(
            range(1, len(best_df) + 1),
            range(1, len(best_df) + 1),
            rotation=45,
            ha="right",
        )
        # Adjust the layout to avoid overlapping labels
        plt.tight_layout()

        # Save the bar chart to a folder (change the path as per your requirement)
        plt.savefig("result/bowler_graphs/best_bowler_per_game.png")

    def show_best_home_away_bowler(
        self,
        bowler_df: pd.DataFrame,
        home_or_away: str,
    ) -> None:
        wickets_column = f"{str.lower(home_or_away)}_wickets_taken"
        economy_rate_column = f"{str.lower(home_or_away)}_economy_rate"
        # Sort the dataframe by average home runs in descending order
        sorted_df = bowler_df.sort_values(by=wickets_column, ascending=False)

        # Get the top N bowler by average runs
        top_bowler = sorted_df.head(10)

        # Set the width of the bars
        bar_width = 0.8

        # Create an array of indices for the x-axis ticks
        indices = np.arange(len(top_bowler))

        # Plot the average runs as a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(
            indices,
            top_bowler[wickets_column],
            label="Average Wickets",
            width=bar_width,
        )

        # Plot the average runs as a scatter plot with dots
        plt.scatter(
            indices,
            top_bowler[economy_rate_column],
            label="Average Economy Rate",
            color="red",
        )

        # Set the x-axis ticks and labels
        plt.xticks(
            indices,
            top_bowler["bowler_name"],
            rotation=45,
            ha="right",
        )

        # Set the y-axis label
        plt.ylabel("Wickets / Economy Rate")

        # Set the chart title
        plt.title(f"Top 10 {home_or_away} Bowler by Average Wickets")

        # Add a legend
        plt.legend()

        # Adjust the layout
        plt.tight_layout()

        # Save the plot to a file
        plt.savefig(f"result/bowler_graphs/best_{str.lower(home_or_away)}_bowler.png")

        # Show the plot

    def show_probability_six_per_over(self, prob_six_per_over: Dict) -> None:
        plt.figure(figsize=(10, 6))
        x = list(prob_six_per_over.keys())
        y = list(prob_six_per_over.values())

        plt.plot(x, y)
        plt.xlabel("Over")
        plt.ylabel("Probability of 6")
        plt.title("Probability of 6 Per Over")
        plt.xlim(1, 20)
        # Save the plot to a file
        plt.savefig(f"result/details_graphs/probability_six_per_over.png")

    def show_total_sixes_per_over(self, total_sixes) -> None:
        plt.figure(figsize=(10, 6))
        plt.plot(total_sixes.index, total_sixes.values)
        plt.xlabel("Over")
        plt.ylabel("Total sixes")
        plt.title("Total Sixes Per Over")
        plt.xlim(1, 20)
        plt.savefig("result/details_graphs/total_sixes_per_over.png")

    def show_team_run_count(
        self, innings_density: pd.DataFrame, first_or_second: str
    ) -> None:
        teams = innings_density["current_innings"].unique()
        num_teams = len(teams)
        num_cols = 3
        num_rows = (num_teams + 1) // num_cols  # Calculate the number of rows required
        fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 6 * num_rows))

        for i, team in enumerate(teams):
            team_data = innings_density[innings_density["current_innings"] == team]
            runs = team_data["runs"]
            count = team_data["count"]
            row = i // num_cols
            col = i % num_cols
            ax = (
                axs[row, col] if num_rows > 1 else axs[col]
            )  # Select the correct subplot axes
            ax.bar(runs, count)
            ax.set_xlabel("Runs")
            ax.set_ylabel("Count")
            ax.set_title(f"{first_or_second} Innings - Count by Run Type - {team}")

        plt.tight_layout()  # Adjust spacing between subplots
        plt.savefig(f"result/details_graphs/team_run_count_{first_or_second}.png")

    def show_game_break_wins(self, summary_df: pd.DataFrame) -> None:
        plt.figure(figsize=(4, 6))
        # Plot the heatmap
        plt.imshow(summary_df.iloc[:, 2:], cmap="hot", interpolation="nearest")
        plt.colorbar(label="Probability")
        plt.xticks(
            range(len(summary_df.columns[2:])), summary_df.columns[2:], rotation=45
        )
        plt.yticks(range(len(summary_df.index)), summary_df.index)
        plt.xlabel("Winning Team")
        plt.ylabel("Days Between Games")
        plt.title("Probability Heatmap")
        plt.tight_layout()
        plt.savefig("result/summary_graphs/game_break_wins.png")

    def toss_decisions(self, toss_decisions: Dict[str, int]) -> None:
        labels = list(toss_decisions.keys())
        values = list(toss_decisions.values())
        plt.figure(figsize=(4, 6))
        plt.bar(labels, values)
        plt.xlabel("Decision Made")
        plt.ylabel("Amount of Times Chosen")
        plt.title("Toss Won Decision")
        plt.savefig("result/summary_graphs/toss_decisions.png")

    def show_lowest_scores(self, lowest_scores: Dict[str, Dict[str, int]]) -> None:
        # Set the width of the bars
        bar_width = 0.8
        innings = list(lowest_scores.keys())
        scores = [
            lowest_scores["1st Inning"]["Score"],
            lowest_scores["2nd Inning"]["Score"],
        ]
        colors = [
            TEAM_COLOURS[lowest_scores["1st Inning"]["Team"]],
            TEAM_COLOURS[lowest_scores["2nd Inning"]["Team"]],
        ]
        # Create a list of legend handles
        legend_handles = [
            Patch(facecolor=TEAM_COLOURS.get(team, "gray"), edgecolor="black")
            for team in [
                lowest_scores["1st Inning"]["Team"],
                lowest_scores["2nd Inning"]["Team"],
            ]
        ]
        plt.figure(figsize=(10, 6))
        # Create the legend
        plt.legend(
            legend_handles,
            [lowest_scores["1st Inning"]["Team"], lowest_scores["2nd Inning"]["Team"]],
            loc="upper right",
        )

        plt.bar(innings, scores, color=colors, width=bar_width)
        plt.xlabel("Inning")
        plt.ylabel("Score")
        plt.title("Lowest Team Scores by Inning")
        plt.savefig("result/details_graphs/lowest_score_by_inning.png")

    def show_highest_scores(self, highest_scores: Dict[str, Dict[str, int]]) -> None:
        # Set the width of the bars
        bar_width = 0.8
        innings = list(highest_scores.keys())
        scores = [
            highest_scores["1st Inning"]["Score"],
            highest_scores["2nd Inning"]["Score"],
        ]
        colors = [
            TEAM_COLOURS[highest_scores["1st Inning"]["Team"]],
            TEAM_COLOURS[highest_scores["2nd Inning"]["Team"]],
        ]
        plt.figure(figsize=(10, 6))
        # Create a list of legend handles
        legend_handles = [
            Patch(facecolor=TEAM_COLOURS.get(team, "gray"), edgecolor="black")
            for team in [
                highest_scores["1st Inning"]["Team"],
                highest_scores["2nd Inning"]["Team"],
            ]
        ]
        # Create the legend
        plt.legend(
            legend_handles,
            [
                highest_scores["1st Inning"]["Team"],
                highest_scores["2nd Inning"]["Team"],
            ],
            loc="upper right",
        )

        plt.bar(innings, scores, color=colors, width=bar_width)
        plt.xlabel("Inning")
        plt.ylabel("Score")
        plt.title("Highest Team Scores by Inning")
        plt.savefig("result/details_graphs/highest_score_by_inning.png")
