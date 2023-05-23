import logging

import pandas as pd


class DatasetCleaner:
    def read_dataset(
        self,
    ) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Reads all the input CSV files into separate Pandas dataframes.

        Returns:
            Tuple[pd.DataFrame]: All the separate CSV files converted to dataframes
        """
        BATTING_CSV: str = "./input/raw_input/batting_card.csv"
        BOWLING_CSV: str = "./input/raw_input/bowling_card.csv"
        DETAILS_CSV: str = "./input/raw_input/details.csv"
        SUMMARY_CSV: str = "./input/raw_input/summary.csv"

        batting_df: pd.DataFrame = pd.read_csv(BATTING_CSV)
        bowling_df: pd.DataFrame = pd.read_csv(BOWLING_CSV)
        details_df: pd.DataFrame = pd.read_csv(DETAILS_CSV)
        summary_df: pd.DataFrame = pd.read_csv(SUMMARY_CSV)
        return batting_df, bowling_df, details_df, summary_df

    def clean_dataframe(
        self, batting_df, bowling_df, details_df, summary_df
    ) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Main function that co-ordinates the cleaning of all Dataframes

        Args:
            batting_df (pd.DataFrame): batting_card.csv dataframe
            bowling_df (pd.DataFrame): bowling_card.csv dataframe
            details_df (pd.DataFrame): details.csv dataframe
            summary_df (pd.DataFrame): summary.csv dataframe

        Returns:
            Tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame,pd.DataFrame]: all cleaned dataframes
        """
        batting_df = self.clean_batting(batting_df)
        bowling_df = self.clean_bowling(bowling_df)
        details_df = self.clean_details(details_df)
        summary_df = self.clean_summary(summary_df)

        batting_df.to_csv("./input/clean_input/batting_card.csv", index=False)
        bowling_df.to_csv("./input/clean_input/bowling_card.csv", index=False)
        details_df.to_csv("./input/clean_input/details.csv", index=False)
        summary_df.to_csv("./input/clean_input/summary.csv", index=False)
        return batting_df, bowling_df, details_df, summary_df

    def clean_batting(self, batting_df: pd.DataFrame) -> pd.DataFrame:
        """All the steps to be taken to clean the batting_df dataframe

        Args:
            batting_df (pd.Dataframe): batting_card.csv dataframe

        Returns:
            pd.DataFrame: the cleaned batting_df dataframe
        """
        if "link" in batting_df.columns:
            batting_df.drop("link", axis=1, inplace=True)

        if "commentary" in batting_df.columns:
            batting_df.drop("commentary", axis=1, inplace=True)

        # rename the fullName column to full_name for consistency
        batting_df.rename(
            columns={
                "fullName": "full_name",
                "ballsFaced": "balls_faced",
                "strikeRate": "strike_rate",
                "isNotOut": "not_out",
                "runningScore": "running_score",
                "runningOver": "running_over",
                "shortText": "short_text",
            },
            inplace=True,
        )

        # replace the string in the 'short_text' column
        batting_df = batting_df.assign(
            short_text=batting_df["short_text"].str.replace("&dagger;", "")
        )

        return batting_df

    def clean_bowling(self, bowling_df: pd.DataFrame) -> pd.DataFrame:
        """All the steps to be taken to clean the bowling_df dataframe

        Args:
            bowling_df (pd.Dataframe): bowling_card.csv dataframe

        Returns:
            pd.DataFrame: the cleaned bowling_df dataframe
        """
        duplicate_rows = bowling_df.duplicated().sum()
        if duplicate_rows > 0:
            logging.error("Duplicate rows were detected for /input/bowling_card.csv")

        if "href" in bowling_df.columns:
            bowling_df.drop("href", axis=1, inplace=True)

        bowling_df.rename(
            columns={
                "fullName": "full_name",
                "economyRate": "economy_rate",
                "foursConceded": "fours_conceded",
                "sixesConceded": "sixes_conceded",
            },
            inplace=True,
        )

        return bowling_df

    def clean_details(self, details_df) -> pd.DataFrame:
        """All the steps to be taken to clean the details_df dataframe

        Args:
            details_df (pd.Dataframe): details.csv dataframe

        Returns:
            pd.DataFrame: the cleaned details_df dataframe
        """
        if "link" in details_df.columns:
            details_df.drop("link", axis=1, inplace=True)

        duplicate_rows = details_df.duplicated().sum()
        if duplicate_rows > 0:
            logging.error(
                f"{duplicate_rows} duplicate rows were detected for /input/details.csv"
            )

        return details_df

    def clean_summary(self, summary_df) -> pd.DataFrame:
        """All the steps to be taken to clean the summary_df dataframe

        Args:
            summary_df (pd.Dataframe): summary.csv dataframe

        Returns:
            pd.DataFrame: the cleaned summary_df dataframe
        """
        duplicate_rows = summary_df.duplicated().sum()
        if duplicate_rows > 0:
            logging.error("Duplicate rows were detected for /input/summary.csv")

        return summary_df
