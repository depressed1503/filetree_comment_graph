# <comment>Главный файл, содержащий скрипт запуска программы.</comment>
from filetree_comment_graph.recursive_grapher import RecursiveGrapher
import re, os, argparse
from filetree_comment_graph.arg_actions import *


def replace_project_tree(dir: str, markdown: str, readme_file_name: str="README.md", project_root_tag_text: str="project_root"):
    """
    Метод, заменяющий текст внутри тега project_root_tag_text на актуальную инструкцию в файле readme_file_name.
    """
    def replace_inner(match):
        """
        Вспомогательный метод для замены при попощи re.sub.
        """
        return f"{match.group(1)}{markdown}{match.group(3)}"
    
    text = ""
    with open(os.path.join(dir, readme_file_name), mode="r", encoding="utf-8") as f:
        text = f.read()
        pattern = fr"(<{project_root_tag_text}>)(.*?)(</{project_root_tag_text}>)"
        text = re.sub(pattern, replace_inner, text, flags=re.DOTALL)
    with open(readme_file_name, mode="w") as f:
        f.write(text)


def main():
    """
    Точка входа в программу/модуль.
    """
    # Добавляем аргументы командной строки и парсим их при помощи argparse.
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Корневая директория проекта", action=DirAction, const=".")
    parser.add_argument("--indent", "-i", help="Корневая директория проекта", action=IndentAction, const=4, default=4)
    parser.add_argument("--readmename", "-r", help="Название файла README в директории проекта.", action=ReadmeAction, const="README.md", default="README.md")
    parser.add_argument("--ignore", "-n", help="Список игнорируемых директорий.", nargs="*", action=IngoreAction, const=[".git"], default=[".git"])
    parser.add_argument("--tag", "-t", help="Внутренний текст тега для вставки дерева.", default="project_root")
    args = parser.parse_args()
    
    # Генерируем строки markdown разметки с графом директории.
    rg = RecursiveGrapher(indent_depth=int(args.indent))
    lines = rg.generate_markdown(args.dir, ignore=args.ignore)
    md = "\n```\n" + "\n".join(lines) + "\n```\n"
    print(md)
    # Заменяем текущее дерево на новое.
    replace_project_tree(args.dir, md, args.readmename, args.tag)


if __name__ == "__main__":
    main()
