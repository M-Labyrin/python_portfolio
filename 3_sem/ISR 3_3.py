# Создание скрипта для считывания данных справочных логов изтекстового файла и
# преобразования их в CSV-формат с последующейзаписью в новый файл.

import csv

with open('log-file.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('log-file.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
