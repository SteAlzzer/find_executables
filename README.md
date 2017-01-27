# Find executable files in folder

Скрипт рекурсивно проходит по каталогу и определяет исполняемые файлы.
Является неким ~~велосипедом~~ аналогом `find . -type f --executable`.

# Как работает
Скрипт читает заголовок каждого файла и пытается найти в нём сигнатуру.
- Для ОС семейства Windows ищем `b'MZ'` *wiki(https://ru.wikipedia.org/wiki/Portable_Executable#.D0.A1.D0.B8.D0.B3.D0.BD.D0.B0.D1.82.D1.83.D1.80.D0.B0)*
- Для Linux-подобных ОС ищем `b'ELF'` *wiki(https://en.wikipedia.org/wiki/Executable_and_Linkable_Format)*

Дополнительно есть возможнось вывести список расширений найденных исполняемых файлов (ключ `-e`).
Перечень расширений выводится в файл с отчётом.

# Как запустить
В консоли:
`python find_executables.py [-h] [-e] [path_to_folder] [path_to_report]`.
- `path_to_folder`	- путь к папке (по умолчанию - текущая папка).
- `path_to_report`	- путь к файлу отчета (по умолчанию - ./found_binaries.txt).
- `-e (--extensions)`	- построить список расширений найденных файлов.

# TODO
- [x] Добавить argparse
- [x] Построение списка расширений
- [ ] Разделение на виндовые и линуксойдные файлы