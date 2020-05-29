from FileLoader import FileLoader


def howManyMedals(data, name):
    full = data.query(f' Name == "{name}"')[["Year", "Medal"]]
    d2 = full.groupby("Year").Medal
    d2 = dict(d2.apply(list))
    for x in d2:
        d2[x] = {'G': d2[x].count("Gold"), 'S': d2[x].count(
            "Silver"), 'B': d2[x].count("Bronze")}
    return d2


loader = FileLoader()
data = loader.load('athlete_events.csv')
print(howManyMedals(data, 'Kjetil Andr Aamodt'))
