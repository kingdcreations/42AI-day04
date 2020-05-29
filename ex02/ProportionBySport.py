from FileLoader import FileLoader


def proportionBySport(data, year, sport, sex):
    d1 = data.query(f'Year == {year} & Sport == "{sport}" & Sex == "{sex}"')
    d1 = d1.drop_duplicates(subset="Name", keep='first')
    d2 = data.query(f'Year == {year} & Sex == "{sex}"')
    d2 = d2.drop_duplicates(subset="Name", keep='first')
    return (d1.shape[0] / d2.shape[0])


loader = FileLoader()
data = loader.load('athlete_events.csv')
print(proportionBySport(data, 2004, 'Tennis', 'F'))
