def translate(words):
    d = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    result = []
    for word in words:
        w = word.lower()
        if w in d.keys():
            result.append(d[w])
        else:
            result.append(word)
    return result

print(translate(["Merry","Christmas","and","Byaka"]))
