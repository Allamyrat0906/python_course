# define a dictionary
dictionary = {
    "apple": "a fruit",
    "car": "a vehicle",
    "book": "a thing to read",
    "house": "a place to live",
}

# get input from the user
word = input("Enter a word: ")

# look up the word in the dictionary
if word in dictionary:
    definition = dictionary[word]
    print(f"The definition of {word} is {definition}.")
else:
    print(f"Sorry, the word {word} is not in the dictionary.")