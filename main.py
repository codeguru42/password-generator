from faker import Faker


def generate_passwords(n):
    fake = Faker()
    for i in range(n):
        yield '.'.join(fake.name().split()), fake.password(25)


def main():
    for username, password in generate_passwords(10):
        print(username, password)


if __name__ == '__main__':
    main()
