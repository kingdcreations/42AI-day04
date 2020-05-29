from FileLoader import FileLoader
import matplotlib.pyplot as plt
import pandas as pd


class MyPlotLib(object):
    """docstring for MyPlotLib."""

    def __init__(self):
        pass

    def histogram(self, data, feature):
        data = data.drop_duplicates("Name")
        fig, axes = plt.subplots(ncols=len(feature))
        i = 0
        for x in axes:
            x.hist(data[feature[i]], bins=10)
            x.grid()
            x.set_title(feature[i])
            i += 1
        fig.tight_layout()
        plt.show()

    def density(self, data, feature):
        data = data.drop_duplicates("Name").dropna()
        pd.DataFrame(data, columns=feature).plot(kind='density')
        plt.show()

    def pair_plot(self, data, feature):
        data = data.drop_duplicates("Name").dropna()
        pd.DataFrame(data, columns=feature).plot(kind='scatter', x=feature[0], y=feature[1])
        plt.show()

    def box_plot(self, data, feature):
        data = data.drop_duplicates("Name").dropna()
        pd.DataFrame(data, columns=feature).plot(kind='box')
        plt.show()


loader = FileLoader()
data = loader.load('athlete_events.csv')
mpl = MyPlotLib()
mpl.histogram(data, ["Height", "Weight"])
mpl.density(data, ["Weight", "Height"])
mpl.pair_plot(data, ["Weight", "Height"])
mpl.box_plot(data, ["Weight", "Height"])
