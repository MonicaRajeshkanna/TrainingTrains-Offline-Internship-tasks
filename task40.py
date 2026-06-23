from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

word = "running"

print("Stem:", stemmer.stem(word))
print("Lemma:", lemmatizer.lemmatize(word))