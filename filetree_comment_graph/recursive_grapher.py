# <comment>Файл с классом, содержащим статические методы для построение графа директории</comment>
import os
import re
import fnmatch


class RecursiveGrapher():
    """
    Класс для создания графа директории с заданными именем файла комментари, глубиной отступа, директорией и игнорированием файлов/директорий.
    """
    DIR_COMMENT_FILE_NAME = "comment"
    DIR_INDENT_DEPTH = 4
    def __init__(self, indent_depth=4, dir_comment_file_name="comment"):
        self.DIR_INDENT_DEPTH = indent_depth
        self.DIR_COMMENT_FILE_NAME = dir_comment_file_name

    def get_file_comment(self, file_path: str):
        """
        Метод, возвращающий строку с комментарием, которая идёт после имени файла в графе.
        """
        try:
            with open(file_path, encoding="utf-8") as f:
                f_text = f.read()
                comment_match = re.search(r"<comment>(.*?)</comment>", f_text)
                if comment_match:
                    return " # " + comment_match.group(1)
        except UnicodeDecodeError:
            return ""
        return ""
    
    def get_dir_comment(self, dir_path: str):
        """
        Метод, возвращающий строку с комментарием, которая идёт после имени папки в графе.
        """
        dir_comment_file = os.path.join(dir_path, RecursiveGrapher.DIR_COMMENT_FILE_NAME)
        if os.path.exists(dir_comment_file) and os.path.isfile(dir_comment_file):
            with open(dir_comment_file, encoding="utf-8") as f:
                return " # " + f.readlines()[0]
        else:
            return ""
     
    def generate_markdown(self, dir_path: str, ignore: list[str], indent=0):
        """
        Рекурсивный метод, генерирующий строки markdown разметки c комментариями для всех вложенных папок и файлов.
        """
        markdown_lines = []
        if not os.path.isdir(dir_path):
            return ""
        items = os.listdir(dir_path)
        for item in items:
            item_path = os.path.join(dir_path, item)
            relative_path = os.path.relpath(item_path, dir_path)
            # Проверяем, есть ли текущий объект в списке игнорирования. 
            if any(fnmatch.fnmatch(item_path, ignore_item) or fnmatch.fnmatch(item, ignore_item) or fnmatch.fnmatch(relative_path, ignore_item) for ignore_item in ignore):
                continue
            # Проверяем, если текущий объект - это директория.
            if os.path.isdir(item_path):
                markdown_lines.append(f"|{'-' * self.DIR_INDENT_DEPTH * indent}📁{item}{self.get_dir_comment(item_path)}")
                markdown_lines.extend(self.generate_markdown(item_path, ignore, indent+1))
            else:
                if item != self.DIR_COMMENT_FILE_NAME:
                    markdown_lines.append(f"|{'-' * self.DIR_INDENT_DEPTH * indent}💾{item}{self.get_file_comment(item_path)}")
        return markdown_lines
