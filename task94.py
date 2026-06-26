questions = {
    "python":"Python is a programming language."
}

q = input("Ask Question: ").lower()

print(questions.get(q,"Answer Not Found"))