import os
import pandas as pd

from JustRead import app

DATASET_PATH = os.path.join(app.root_path, 'dataset', 'books.csv')


def get_label_name(string):
    return string.replace("_", " ").capitalize()


class ModelChoices:
    def __init__(self, choices_list):
        for item in choices_list:
            setattr(self, item.lower(), get_label_name(item))

    def choices(self):
        return [(k, v) for k, v in self.__dict__.items()]

    def values(self):
        return [v for v in self.__dict__.keys()]

    def labels(self):
        return [l for l in self.__dict__.values()]


df = pd.read_csv(DATASET_PATH, sep=',')


UserTypeChoices = ModelChoices(['BookStore', 'Customer', 'Courier'])

if __name__ == '__main__':
    print(df.item.unique())

