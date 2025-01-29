# <comment>Главный файл, содержащий скрипт запуска программы.</comment>
from recursive_grapher import RecursiveGrapher
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")
    args = parser.parse_args()
    print("\n".join(RecursiveGrapher.generate_markdown(args.dir, ignore=["__pycache__", ".git"])))


if __name__ == "__main__":
    main()