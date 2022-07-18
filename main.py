import sys

import requests
from faker import Faker


def generate_passwords(n):
    fake = Faker()
    for i in range(n):
        yield '.'.join(fake.name().split()), fake.password(25)


def main():
    url = sys.argv[1]
    n = int(sys.argv[2])
    for username, password in generate_passwords(n):
        data = {
            'username': username,
            'passwordx': password
        }
        response = requests.post(url, data=data)
        print(username, password, response.status_code)


if __name__ == '__main__':
    main()
