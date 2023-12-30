import nltk

# Simplified example for extracting item names and quantities
tokens = nltk.word_tokenize(text)
item_names = [token for token in tokens if token in product_database]
quantities = [int(token) for token in tokens if token.isdigit()]
