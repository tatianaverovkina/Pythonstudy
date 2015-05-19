def letter(string):
    a = set(["a","e","u","o","i"])
    if string.lower() in a:
        return True
    else:
        return False

print(letter('B'))
