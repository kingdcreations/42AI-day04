from FileLoader import FileLoader


def howManyMedalsByCountry(data, loc):
    full = data.query(f' Team == "{loc}"')[["Year", "Medal"]]
    d2 = full.groupby("Year").Medal
    d2 = dict(d2.apply(list))
    for x in d2:
        d2[x] = {'G': d2[x].count("Gold"), 'S': d2[x].count(
            "Silver"), 'B': d2[x].count("Bronze")}
    return d2


loader = FileLoader()
data = loader.load('athlete_events.csv')
print(howManyMedalsByCountry(data, 'France'))
