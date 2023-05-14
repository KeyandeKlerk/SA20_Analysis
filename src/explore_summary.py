import pandas as pd


class SummaryData:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)

    def get_tournament_summary(self):
        return self.df
