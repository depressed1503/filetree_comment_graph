# <comment>Главный файл, содержащий скрипт запуска программы.</comment>
from recursive_grapher import RecursiveGrapher


def main():
    print("\n".join(RecursiveGrapher.generate_markdown(input(), ignore=["__pycache__"])))


if __name__ == "__main__":
    main()