import re

def clean_text(text: str) -> str:
    """
    Preprocess user input by:
    1. Converting to lowercase
    2. Removing punctuation
    3. Stripping extra spaces
    """
    # Lowercase
    text = text.lower()

    # Remove punctuation (anything not a word, space, or digit)
    text = re.sub(r"[^\w\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# Test case
if __name__ == "__main__":
    sample = "  HELLo!!!  How ARE you?? "
    print("Original:", repr(sample))
    print("Cleaned :", repr(clean_text(sample)))
