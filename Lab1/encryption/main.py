import сaesar_encryption
import vigenere_encryption


if __name__ == '__main__':
    message = 'Съешь же ещё этих мягких французских булок, да выпей чаю.'
    res = сaesar_encryption.encrypt(message, 3)

    print("Encrypted: ", res)
    print("Decrypted: ", сaesar_encryption.decrypt(res, 3))

    message = 'ATTACKATDAWN'
    res = vigenere_encryption.encrypt(message)
    print("Encrypted: ", res)
    print("Decrypted: ", vigenere_encryption.decrypt(res))


