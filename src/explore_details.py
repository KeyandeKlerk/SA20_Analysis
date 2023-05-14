import pandas as pd


class DetailsData:
    def __init__(self, details_df: pd.DataFrame):
        self.details_df = details_df

    def all_density_of_runs(self) -> pd.DataFrame:
        count_df = (
            self.details_df.groupby(["current_innings", "runs"])
            .size()
            .reset_index(name="count")
        )
        return count_df

    def inning_density_of_runs(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        innings_1_df = self.details_df[self.details_df["innings_id"] == 1]
        innings_2_df = self.details_df[self.details_df["innings_id"] == 2]

        innings_1_count_df = (
            innings_1_df.groupby(["current_innings", "runs"])
            .size()
            .reset_index(name="count")
        )
        innings_2_count_df = (
            innings_2_df.groupby(["current_innings", "runs"])
            .size()
            .reset_index(name="count")
        )

        return innings_1_count_df, innings_2_count_df

    def likelihood_of_six_per_over(self):
        sixes = self.details_df[self.details_df["runs"] == 6].copy()
        sixes_by_over = sixes.groupby("over")["runs"].count()
        total_sixes = sixes["runs"].count()
        sixes_by_over_total = sixes.groupby("over")["runs"].sum()
        six_probs = {}
        for over, sixes_at_over in sixes_by_over.iteritems():  # type: ignore
            six_prob = sixes_at_over / total_sixes
            six_probs[over] = six_prob
        return six_probs, sixes_by_over_total
