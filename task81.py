news = input("Enter News: ")

fake_words = ["rumor", "fake", "hoax"]

if any(word in news.lower() for word in fake_words):
    print("Potential Fake News")
else:
    print("Looks Genuine")