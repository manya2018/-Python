# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f_input:  # TODO считать содержимое csv файла
        data = [line for line in csv.DictReader(f_input)]

        with open(OUTPUT_FILENAME,'w') as output_f:  # TODO Сериализовать в файл с отступами равными 4
             json.dump(data,output_f,indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
