# Define the dictionary
word_values = {
    "cat": "A small domesticated carnivore, Felis domestica, kept as a pet.",
    "dog": "A domesticated carnivore, Canis lupus familiaris, used for various purposes.",
    "bird": "Any warm-blooded vertebrate having feathers and laying hard-shelled eggs."
}

# Get user input
input_word = input("Enter a word (cat, dog, or bird): ").lower()

# Get the value from the dictionary
value = word_values.get(input_word or "Word not found in the dictionary.")

# Print the value
print(value)

