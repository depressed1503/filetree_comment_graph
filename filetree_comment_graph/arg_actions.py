# <comment>Файл с валидационными классами для параметров командной строки</comment>
from argparse import Action
import os


class DirAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not (os.path.exists(values) and os.path.isdir(values)):
            print("Получено значени dir:", values)
            raise FileNotFoundError(f"Директория '{values}' не существует.")
        setattr(namespace, self.dest, values)


class IndentAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        try:
            value = int(values)  # Try converting the string to an integer
            if value < 0:
                raise ValueError("Аргумент indent должен быть числом большим и равным 0.")
        except ValueError:
            raise ValueError("Аргумент indent должен быть числом большим и равным 0.")
        setattr(namespace, self.dest, values)


class ReadmeAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not (os.path.exists(values) and os.path.isfile(values)):
            print("Получено значени readmename:", values)
            raise FileNotFoundError(f"Файл '{values}' не существует.")
        setattr(namespace, self.dest, values)


class IngoreAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)