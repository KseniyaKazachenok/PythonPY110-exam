import random
import faker
fake = faker.Faker("ru")


def book_length(fn):
    def wrapper(*args: str):
        result = fn(*args)
        if len(result) > 45:
            raise ValueError("Длина названия книги превышает заданное значение")

        return result

    return wrapper


@book_length
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
