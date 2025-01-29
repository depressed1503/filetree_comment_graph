# <comment>Главный файл, содержащий скрипт запуска программы.</comment>
from .recursive_grapher import RecursiveGrapher
import re, os, argparse
from .arg_actions import *


def replace_project_tree(dir: str, markdown: str, readme_file_name: str="README.md"):
    def replace_inner(match):
        return f"{match.group(1)}{markdown}{match.group(3)}"
    
    text = ""
    with open(os.path.join(dir, readme_file_name), mode="r") as f:
        text = f.read()
        pattern = r"(<project_root>)(.*?)(</project_root>)"
        text = re.sub(pattern, replace_inner, text, flags=re.DOTALL)
    with open(readme_file_name, mode="w") as f:
        f.write(text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Корневая директория проекта", action=DirAction, const=".")
    parser.add_argument("--indent", "-i", help="Корневая директория проекта", action=IndentAction, const=4, default=4)
    parser.add_argument("--readmename", "-r", help="Название файла README в директории проекта.", action=ReadmeAction, const="README.md", default="README.md")
    parser.add_argument("--ignore", "-n", help="Список игнорируемых директорий.", nargs="*", action=IngoreAction, const=[".git"], default=[".git"])
    args = parser.parse_args()
    rg = RecursiveGrapher(indent_depth=int(args.indent))
    lines = rg.generate_markdown(args.dir, ignore=args.ignore)
    md = "\n```\n" + "\n".join(lines) + "\n```\n"
    print(md)
    replace_project_tree(args.dir, md, args.readmename)


if __name__ == "__main__":
    main()
