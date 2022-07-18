def generate_passwords(n):
    for i in range(n):
        yield 'username', 'password'


def main():
    for username, password in generate_passwords(10):
        print(username, password)


if __name__ == '__main__':
    main()
