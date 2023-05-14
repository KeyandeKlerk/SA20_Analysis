import pandas as pd


class DetailsData:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)

    def get_match_details(self, match_id):
        return self.df[self.df['match_id'] == match_id]
