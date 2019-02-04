def caesar_encryption(str):
    ct = ""
    for s in str:
        if s == ' ':
            continue
        ascii_value = ord(s) - 97
        ct += chr(((ascii_value + 3) % 26 + 97))
    return ct

def caesar_decryption(str, key_value):
    pt = ""
    for s in str:
        if s == ' ':
            continue
        if s == '\n':
            break
        ascii_value = ord(s) - 97
        pt += chr(((ascii_value - key_value) % 26 + 97))
    return pt