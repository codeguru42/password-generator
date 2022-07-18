def generate_passwords():
    yield 'username', 'password'


def main():
    for username, password in generate_passwords():
        print(username, password)


if __name__ == '__main__':
    main()
