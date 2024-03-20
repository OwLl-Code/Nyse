import xml.etree.ElementTree  # Импорт модуля для работы с XML


def main():
    try:
        NYSE = xml.etree.ElementTree.parse(
            "nyse.xml"
        )  # Попытка парсинга файла 'nyse.xml' c информацией о бирже
    except FileNotFoundError:  # Обработка исключения, если файл не найден
        print("Stock data file not found")
        exit(1)
    except (
        xml.etree.ElementTree.ParseError
    ):  # Обработка исключения, если файл содержит неверные данные
        print("Stock data file contains invalid data")
        exit(2)

    quotes = NYSE.getroot()  # Получение корневого элемента дерева XML

    print(
        "COMPANY".ljust(40), end=""
    )  # Вывод заголовка COMPANY и выравнивание по левому краю
    print(
        "LAST".ljust(10), end=""
    )  # Вывод заголовка LAST и выравнивание по левому краю
    print(
        "CHANGE".ljust(10), end=""
    )  # Вывод заголовка CHANGE и выравнивание по левому краю
    print("MIN".ljust(10), end="")  # Вывод заголовка MIN и выравнивание по левому краю
    print("MAX".ljust(10), end="")  # Вывод заголовка MAX и выравнивание по левому краю
    print()  # Переход на новую строку
    print("-" * 80)  # Вывод горизонтального разделителя

    for quote in quotes.findall("quote"):  # Обход всех элементов 'quote' в дереве XML
        print(
            quote.text.ljust(40), end=""
        )  # Вывод текстового контента элемента 'quote' с выравниванием по левому краю
        print(
            quote.attrib["last"].ljust(10), end=""
        )  # Вывод атрибута 'last' элемента 'quote' с выравниванием по левому краю
        print(
            quote.attrib["change"].ljust(10), end=""
        )  # Вывод атрибута 'change' элемента 'quote' с выравниванием по левому краю
        print(
            quote.attrib["min"].ljust(10), end=""
        )  # Вывод атрибута 'min' элемента 'quote' с выравниванием по левому краю
        print(
            quote.attrib["max"].ljust(10), end=""
        )  # Вывод атрибута 'max' элемента 'quote' с выравниванием по левому краю


if __name__ == "__main__":
    print("Запущено как самостоятельный модуль")
    main()
else:
    print("Запущено как импортируемый модуль")
