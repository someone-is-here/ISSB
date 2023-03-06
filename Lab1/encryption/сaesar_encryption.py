# alphabet = "ABCDEFGHIJKLMNOPQRSTYVWXYZ"
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def func_encr(i, step):
    if alphabet.find(i) != -1:
        return alphabet[(alphabet.find(i) + step) % len(alphabet)]
    elif i.isalpha():
        return alphabet[(alphabet.find(i.upper()) + step) % len(alphabet)].lower()
    else:
        return i


def func_decr(i, step):
    if alphabet.find(i) != -1:
        return alphabet[(alphabet.find(i) - step) % len(alphabet)]
    elif i.isalpha():
        return alphabet[(alphabet.find(i.upper()) - step) % len(alphabet)].lower()
    else:
        return i


def encrypt(message, step=5):

    encrypted_message = ""

    for i in message:
        encrypted_message += func_encr(i, step)

    return encrypted_message


def decrypt(message, step=5):
    decrypted_message = ""

    for i in message:
        decrypted_message += func_decr(i, step)

    return decrypted_message
