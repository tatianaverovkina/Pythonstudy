def histogram(integers):
    try:
        for i in integers:
            print(i * "*")
    except TypeError:
            print("Cannot convert list item to integers")

histogram([4,9,7])
