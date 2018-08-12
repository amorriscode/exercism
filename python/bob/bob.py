import re

def hey(phrase):
    # Clean the phrase up by removing whitespace and numbers
    cleanedPhrase = re.sub(r"[^a-zA-Z?,]", "", phrase)
    isQuestion = cleanedPhrase.endswith("?")
    isYelling = cleanedPhrase == cleanedPhrase.upper()

    # Nothing was said to Bob
    if not cleanedPhrase:
        return "Fine. Be that way!"

    # Question was yelled at Bob
    elif isYelling and isQuestion and len(cleanedPhrase) > 1:
        return "Calm down, I know what I'm doing!"

    # Question was asked of Bob
    elif isQuestion:
        return "Sure."

    # Something was yelled at Bob
    # Makes sure there were actual letters in the phrase
    elif isYelling and re.search('[a-zA-Z]', cleanedPhrase):
        return "Whoa, chill out!"

    return "Whatever."
