import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag

# Download required resources
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

# Try to get both versions of the tagger
try:
    nltk.download("averaged_perceptron_tagger_eng", quiet=True)
except:
    nltk.download("averaged_perceptron_tagger", quiet=True)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return "a"
    elif tag.startswith("V"):
        return "v"
    elif tag.startswith("N"):
        return "n"
    else:
        return None

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = word_tokenize(text)
    try:
        tagged = pos_tag(tokens, lang="eng")  # new way
    except:
        tagged = pos_tag(tokens)              # fallback

    cleaned = []
    for word, tag in tagged:
        if word in stop_words: continue
        if len(word) < 3: continue
        wn_tag = get_wordnet_pos(tag)
        if wn_tag:
            lemma = lemmatizer.lemmatize(word, wn_tag)
            cleaned.append(lemma)

    return " ".join(cleaned)

if __name__ == "__main__":
    sample = "  The cats are sitting on the mat, happily! 123   "
    print("Original:", sample)
    print("Processed:", preprocess_text(sample))
