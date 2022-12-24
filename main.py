import conf
from itertools import count
import random
import json
import faker
fake = faker.Faker("ru")



def title_name():
    filename = "books.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(5):
            f.write(fake.catch_phrase()+"\n")


def year_name():
    year = random.randint(1950, 2022)
    return year


def pages_name():
    pages = random.randint(10, 3000)
    return pages


def isbn_name():
    isbn13 = fake.isbn13()
    return isbn13


def rating_name():
    rating = random.uniform(0, 5)
    return rating


def price_name():
    price = random.uniform()
    return price


def author_name():
    author_start = []
    author_number = random.randint(1, 3)
    for _ in range(author_number):
        author_start.append(" ".join((fake.first_name_male(), fake.last_name_male())))
        author_start.append(" ".join((fake.first_name_female(), fake.last_name_female())))
    author = random.choices(author_start, k=author_number)
    return author


def step():
    counter = count(1, 1)
    yield counter


сonf.MODEL
pk = next(counter)

if __name__ == '__main__':
    def main():
