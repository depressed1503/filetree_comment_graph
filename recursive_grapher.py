# <comment>Файл с классом, содержащим статические методы для построение графа директории.</comment>
import os
import re


class RecursiveGrapher():
    DIR_COMMENT_FILE_NAME = "comment"
    DIR_INDENT_DEPTH = 4

    @staticmethod
    def get_file_comment(file_path: str):
        try:
            with open(file_path, encoding="utf-8") as f:
                f_text = f.read()
                comment_match = re.search(r"<comment>(.*?)</comment>", f_text)
                if comment_match:
                    return comment_match.group(1)
        except UnicodeDecodeError:
            return ""
        return ""
    
    @staticmethod
    def get_dir_comment(dir_path: str):
        dir_comment_file = os.path.join(dir_path, RecursiveGrapher.DIR_COMMENT_FILE_NAME)
        if os.path.exists(dir_comment_file) and os.path.isfile(dir_comment_file):
            with open(dir_comment_file, encoding="utf-8") as f:
                return " # " + f.readlines()[0]
        else:
            return ""
     
    @staticmethod
    def generate_markdown(dir_path: str, ignore: list[str], indent=0):
        markdown_lines = []
        if not os.path.isdir(dir_path):
            return ""
        items = os.listdir(dir_path)
        for item in items:
            item_path = os.path.join(dir_path, item)
            # check if file or directory is required to be ignored
            if item_path in ignore or item in ignore:
                continue
            # check if path is directory and extract comments recursively
            if os.path.isdir(item_path):
                markdown_lines.append(f"{" " * RecursiveGrapher.DIR_INDENT_DEPTH * indent}📁{item}{RecursiveGrapher.get_dir_comment(item_path)}")
                markdown_lines.extend(RecursiveGrapher.generate_markdown(item_path, ignore, indent+1))
            else:
                if item != RecursiveGrapher.DIR_COMMENT_FILE_NAME:
                    markdown_lines.append(f"{" " * RecursiveGrapher.DIR_INDENT_DEPTH * indent}💾{item} # {RecursiveGrapher.get_file_comment(item_path)}")
        return markdown_lines
