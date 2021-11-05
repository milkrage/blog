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


def generator(lowercase=True, uppercase=True, number=True, symbol=True, length=16, amount=10):
    soup = []

    if lowercase:
        soup += [chr(letter) for letter in range(97, 123)]

    if uppercase:
        soup += [chr(letter) for letter in range(65, 91)]

    if number:
        soup += [number for number in range(10)]

    if symbol:
        soup += [chr(symbol) for symbol in range(33, 48)]
        soup += [chr(symbol) for symbol in range(58, 65)]
        soup += [chr(symbol) for symbol in range(91, 96)]
        soup += [chr(symbol) for symbol in range(123, 127)]

    result = []

    for _ in range(amount):
        password = []

        for item in range(length):
            char = secrets.choice(soup)
            char = str(char) if isinstance(char, int) else char
            password.append(char)

        result.append(''.join(password))

    return result
