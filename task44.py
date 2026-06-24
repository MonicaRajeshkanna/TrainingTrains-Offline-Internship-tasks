dictionary = {
    "hello": "வணக்கம்",
    "good": "நல்ல",
    "thank you": "நன்றி"
}

word = input("Enter English word: ").lower()

print(dictionary.get(word, "Translation not found"))