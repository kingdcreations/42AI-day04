import pandas as pd


class FileLoader(object):
    """docstring for FileLoader."""

    def __init__(self):
        pass

    def load(self, arg):
        data = pd.read_csv(arg)
        print(
            f"Loading dataset of dimensions {data.shape[0]} x {data.shape[1]}")
        return data

    def display(self, arg, n):
        if n > 0:
            print(arg[:n])
        else:
            print(arg[:n-1:-1])


loader = FileLoader()
data = loader.load("mdr.csv")
loader.display(data, -12)
