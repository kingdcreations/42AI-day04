from FileLoader import FileLoader


class SpatioTemporalData(object):
    """docstring for SpatioTemporalData."""

    def __init__(self, data):
        self.data = data

    def when(self, loc):
        d1 = self.data.drop_duplicates(subset="Year", keep='first')
        return list(d1.query(f'City == "{loc}"')["Year"])

    def where(self, date):
        d1 = self.data.drop_duplicates(subset="Year", keep='first')
        return list(d1.query(f'Year == "{date}"')["City"])


loader = FileLoader()
data = loader.load('athlete_events.csv')
sp = SpatioTemporalData(data)
print(sp.where(1896))
print(sp.where(2016))
print(sp.when('Athina'))
print(sp.when('Paris'))
