my_dictionary = {"piekarnia": ["chleb", "pączek", "bułki"], "warzywniak": [
    "marchew", "seler", "buraki"]}
x = 0
print("Zadanie 1")
for key, value in my_dictionary.items():
    value_1 = [val.capitalize() for val in value]
    print(
        f"Idę do: {key.capitalize()}, kupuję następujące produkty: {value_1}")
    x += len(value)
#x = len(my_dictionary['piekarnia']) + len(my_dictionary['warzywniak'])

print(f"Łącznie kupuję: {x} produktów")
