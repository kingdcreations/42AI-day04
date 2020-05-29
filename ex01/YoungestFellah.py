from FileLoader import FileLoader


def youngestFellah(data, year):
    d1 = data.query(f'Year == {year} & Sex == "F"').Age.min()
    d2 = data.query(f'Year == {year} & Sex == "M"').Age.min()
    di = {"f": d1, "m": d2}
    return di


loader = FileLoader()
data = loader.load('athlete_events.csv')
print(youngestFellah(data, 2004))
