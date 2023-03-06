from curses.ascii import isupper

alphabet = "ABCDEFGHIJKLMNOPQRSTYVWXYZ"
# alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def get_final_key(key, message):
    final_key = key

    while len(final_key) < len(message):
        final_key += key

    return final_key


def func_encr(i, k):
    if isupper(i) or (1040 <= ord(i) <= 1071):
        return chr((ord(i) + ord(k)) % len(alphabet) + ord(alphabet[0]))
    else:
        return chr((ord(i) - 32 + ord(k)) % len(alphabet) + ord(alphabet[0]) + 32)


def encrypt(message, key='LEMON'):
    key = get_final_key(key, message)

    encrypted_message = "".join(map(func_encr, message, key))

    return encrypted_message


def func_decr(i, k):
    if isupper(i) or (1040 <= ord(i) <= 1071):
        return chr((ord(i) - ord(k)) % len(alphabet) + ord(alphabet[0]))
    else:
        return chr((ord(i) - 32 - ord(k)) % len(alphabet) + ord(alphabet[0]) + 32)


def decrypt(message, key='LEMON'):
    key = get_final_key(key, message)

    decrypted_message = "".join(map(func_decr, message, key))

    return decrypted_message
