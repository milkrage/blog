import secrets


def set_value(soup, field, default, type=None, max=None, min=None):
    value = soup.get(field, default)

    if type is not None:
        value = type(value)

    if max is not None:
        if value > max:
            value = max

    if min is not None:
        if value < min:
            value = min

    return value


def generator(lowercase=True, uppercase=True, number=True, length=16, amount=10):
    soup = []

    if lowercase:
        soup += [chr(letter) for letter in range(97, 123)]

    if uppercase:
        soup += [chr(letter) for letter in range(65, 91)]

    if number:
        soup += [number for number in range(10)]

    result = []

    for _ in range(amount):
        password = []

        for item in range(length):
            symbol = secrets.choice(soup)
            symbol = str(symbol) if isinstance(symbol, int) else symbol
            password.append(symbol)

        result.append(''.join(password))

    return result
