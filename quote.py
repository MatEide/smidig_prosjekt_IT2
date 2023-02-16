import json

def hent_quote():
    fil = open("quote.json")
    quotes = json.load(fil)
    fil.close
    return quotes