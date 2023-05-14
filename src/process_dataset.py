import logging

import pandas as pd


class DatasetCleaner:
    def __init__(self):
        self.logging = logging.basicConfig(
            filename="./log/SA20_analysis.log",
            level=logging.DEBUG,
            format="%(asctime)s:%(levelname)s:%(message)s",
        )

    def read_dataset(
        self,
    ) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Reads all the input CSV files into separate Pandas dataframes.

        Returns:
            Tuple[pd.DataFrame]: All the separate CSV files converted to dataframes
        """
        batting_csv: str = "./input/batting_card.csv"
        bowling_csv: str = "./input/bowling_card.csv"
        details_csv: str = "./input/details.csv"
        summary_csv: str = "./input/summary.csv"

        batting_df: pd.DataFrame = pd.read_csv(batting_csv)
        bowling_df: pd.DataFrame = pd.read_csv(bowling_csv)
        details_df: pd.DataFrame = pd.read_csv(details_csv)
        summary_df: pd.DataFrame = pd.read_csv(summary_csv)
        return batting_df, bowling_df, details_df, summary_df

    def clean_dataframe(
        self, batting_df, bowling_df, details_df, summary_df
    ) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Main function that co-ordinates the cleaning of all Dataframes

        Args:
            batting_df (pd.DataFrame): batting_card.csv dataframe
            bowling_df (pd.DataFrame): bowling_card.csv dataframe
            details_df (pd.DataFrame): details_csv dataframe
            summary_df (pd.DataFrame): summary.csv dataframe

        Returns:
            Tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame,pd.DataFrame]: all cleaned dataframes
        """
        batting_df = self.clean_batting(batting_df)
        bowling_df = self.clean_bowling(bowling_df)
        details_df = self.clean_details(details_df)
        summary_df = self.clean_summary(summary_df)
        return batting_df, bowling_df, details_df, summary_df

    def clean_batting(self, batting_df) -> pd.DataFrame:
        """All the steps to be taken to clean the batting_df dataframe

        Args:
            batting_df (pd.Dataframe): batting_card.csv dataframe

        Returns:
            pd.DataFrame: the cleaned batting_df dataframe
        """
        batting_df.drop("link", axis=1, inplace=True)
        duplicate_rows = batting_df.duplicated().sum()
        if duplicate_rows > 0:
            logging.error(
                f"{duplicate_rows} duplicate rows were detected for /input/batting_card.csv"
            )

        return batting_df

    def clean_bowling(self, bowling_df) -> pd.DataFrame:
        """All the steps to be taken to clean the bowling_df dataframe

        Args:
            bowling_df (pd.Dataframe): bowling_card.csv dataframe

        Returns:
            pd.DataFrame: the cleaned bowling_df dataframe
        """
        duplicate_rows = bowling_df.duplicated().sum()
        if duplicate_rows > 0:
            logging.error(
                "Duplicate rows were detected for /input/bowling_card.csv")

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
            logging.error(
                "Duplicate rows were detected for /input/summary.csv")

        return summary_df
