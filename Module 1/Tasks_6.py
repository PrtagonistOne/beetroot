# Task 1
some_sentence = input('Please input a sentence: ').strip()
# some_sentence = 'This is a very unique and quirky and smart sentence'.strip()
some_list = list(some_sentence)
key_value = ''
list_of_key_values = []
for i, letters in enumerate(some_list):  # subtract every word from the string given
    if letters != ' ':
        key_value += some_list[i]
    elif letters == ' ':
        print(key_value)
        list_of_key_values.append(key_value)
        key_value = ''
list_of_key_values.append(key_value)  # add the last word of the sentence to a list of keys for dict

dict_of_words = {}
for i, key_value in enumerate(list_of_key_values):  # create new dict item by using every word in sentence as the key
    dict_of_words[key_value] = list_of_key_values.count(key_value)
    # use count to appoint the value of occurrences of the same word (that is used as a key) in a sentence
print(dict_of_words)


# Task 2
def total_price_of_stock(fruits: dict, price: dict) -> float:
    total_sum = 0
    for key, value in fruits.items():
        price[key] *= value  # use price dict to multiply it's value of it's stock price value
        total_sum += price[key]  # add every stock price of each fruit
    print(f'\nThe total price of the stock is {total_sum}')

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price_of_stock(stock, prices)
# Task 3
list_comprehension_exercise = [(i, pow(i, 2)) for i in range(1, 11)]
# sqrd = [items1 ** 2 for items1 in list(range(1, 10))]
print(list_comprehension_exercise)
