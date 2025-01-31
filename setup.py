# <comment>Сетап файл для выпуска .whl пакета</comment>
from setuptools import setup, find_packages


setup(
    name="filetree_comment_graph",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "filetree_comment_graph=filetree_comment_graph.__main__:main",
        ],
    },
)