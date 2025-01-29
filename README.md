# Генератор графа директории проекта с комментариями

## Использование как python скрипта:
```shell
python3 main.py path/to/directory -i 4 -n __pycache__ .git
```

## Использование как .whl модуля:

Подготовка (Unix)
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 setup.py bdist_wheel
pip install dist/filetree_comment_graph-0.1-py3-none-any.whl --force-reinstall
```

Вызов
```
python -m filetree_comment_graph path/to/directory -i 4 -n __pycache__ .git
```

Этот пример показывает выполнение построения графа директории **path/to/directory** c отступами по **4** пробела и игнорированием директорий **__pycache__** и **.git**.

Для полного списка всех аргументов используйте
```
python3 main.py -h
```
или
```
python3 -m filetree_comment_graph -h
```

Директории должны содержать файл `comment` с единственной строчкой - комментарием.
Файлы должны содержать тег `<comment>комментарий</comment>` с комментарием.

Так же доступно игнорирование файлов и директорий. Игнорируемые файлы и директории нужно вписать в аргумент **ignore** в файле `main.py`. Пути до файлов и директорий могут быть: а) абсолютными, б) просто именами в формате **folder1**, **file2**.

<project_root>
```
|💾recursive_grapher.py # Файл с классом, содержащим статические методы для построение графа директории.
|💾arg_actions.py # 
|💾README.md # комментарий
|💾.gitignore # 
|💾main.py # Главный файл, содержащий скрипт запуска программы.
```
</project_root>