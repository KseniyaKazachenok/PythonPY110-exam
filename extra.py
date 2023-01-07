import random
import faker
fake = faker.Faker("ru")


def parametr(length):
    """ Предлагает выбрать максимальное значение длины названия книги """
    def book_length(fn):
        def wrapper(*args: str):
            result = fn(*args)
            if len(result) > length:
                raise ValueError("Длина названия книги превышает заданное значение")

            return result

        return wrapper

    return book_length


@parametr(50)
def title_name() -> str:
    """
    Возвращает название книги
    :return: название книги
    """
    filename = "books1.txt"
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


if __name__ == '__main__':
    title_name()
