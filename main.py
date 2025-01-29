# <comment>Главный файл, содержащий скрипт запуска программы.</comment>
from recursive_grapher import RecursiveGrapher
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Корневая директория проекта")
    args = parser.parse_args()
    print("\n".join(RecursiveGrapher.generate_markdown(args.dir, ignore=["__pycache__", ".git", "migrations"])))


if __name__ == "__main__":
    main()
