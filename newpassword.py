import random


def password():
    all_char = '0123456789qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJIKOLP'

    index = len(all_char) + 1

    passward = ''

    for _ in range(8):
        n = random.randint(0, index)

        passward += all_char[n]

    return passward


def port():
    port = random.randint(30000, 39999)
    return port
