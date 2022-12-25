import conf
import random
import json
import faker
fake = faker.Faker("ru")


output_file = "output.json"


def main() -> None:
    """
    Записывает генерируемые словари в json файл
    :return: json файл
    """
    for _ in range(100):
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(next(dict_books), f, indent=4, ensure_ascii=False)


def generator():
    """
    Генерирует словарь, содержащий информацию о книге
    :return: словарь
    """
    dict_ = {
        "model": conf.MODEL,
        "pk": next(counter),
        "fields": {
            "title": title_name(),
            "year": year_name(),
            "pages": pages_name(),
            "isbn13": isbn_name(),
            "rating": rating_name(),
            "price": price_name(),
            "author": author_name()
        }
    }
    yield dict_


dict_books = generator()


def title_name() -> str:
    """
    Возвращает название книги
    :return: название книги
    """
    filename = "books.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(5):
            f.write(fake.catch_phrase()+"\n")
    list_title = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            list_title.append(line.strip())
        title = random.choices(list_title)
        title_str = "".join(title)
    return title_str


def year_name() -> int:
    """
    Возвращает год издания книги
    :return: год
    """
    year = random.randint(1950, 2022)
    return year


def pages_name() -> int:
    """
    Возвращает количество страниц в книге
    :return: количество страниц
    """
    pages = random.randint(10, 3000)
    return pages


def isbn_name() -> str:
    """
    Возвращает уникальный идентификационный номер издания
    :return: isbn13
    """
    isbn13 = fake.isbn13()
    return isbn13


def rating_name() -> float:
    """
    Возвращает рейтинг книги
    :return: рейтинг
    """
    rating = random.uniform(0, 5)
    rating_round = round(rating, 2)
    return rating_round


def price_name() -> float:
    """
    Возвращает цену книги
    :return: цена
    """
    price = random.uniform(1, 5000)
    price_round = round(price, 2)
    return price_round


def author_name() -> list:
    """
    Возвращает имена и фамилии авторов (от 1 до 3)
    :return: список авторов
    """
    author_start = []
    author_number = random.randint(1, 3)
    for _ in range(author_number):
        author_start.append(" ".join((fake.first_name_male(), fake.last_name_male())))
        author_start.append(" ".join((fake.first_name_female(), fake.last_name_female())))
    author = random.choices(author_start, k=author_number)
    return author


def step():
    """
    Автоинкремент
    :return:
    """
    step_ = 1
    while True:
        yield step_
        step_ += 1


counter = step()


if __name__ == '__main__':
    main()
