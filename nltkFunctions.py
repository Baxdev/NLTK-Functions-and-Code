#Returns the length of the "set" of the text (i.e. how many different words/punctuation symbols it uses)
#The set is all of the tokens in a text, with duplicate tokens removed.
#"Tokens" are a sequence of characters that are treated as a group.
#Tokens can be things like words or punctuation symbols.
def lexical_diversity(text):
    return len(set(text)) / len(text)

#Shows the percentage of unique types in a text.
#A "type" is a unique item of vocabulary
def percentage(count, total):
    return 100 * count / total

