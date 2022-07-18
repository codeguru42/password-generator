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
    username_key = sys.argv[3]
    password_key = sys.argv[4]
    i = 0
    for username, password in generate_passwords(n):
        data = {
            username_key: username,
            password_key: password
        }
        response = requests.post(url, data=data)

        if response.status_code != 200:
            print(f'Failed: {username} {password} {response.status_code}')

        if i % 1000 == 0:
            print(f'{i}/{n} passwords sent')
        i += 1


if __name__ == '__main__':
    main()
