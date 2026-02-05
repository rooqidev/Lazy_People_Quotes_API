# Building random quote API using FastAPI
from fastapi import FastAPI
from os import getcwd
from pydantic import BaseModel
#import sys
from random import choice
#print(getcwd())
from LQP_Modules.random_qoutes import random_quote, all_quotes, quotes_in_quantity, category_quotes, searching_quote
lazy_quotes = all_quotes()
#print(getcwd())
#print(sys.path)
#sys.path.append(getcwd())
app = FastAPI()

@app.get("/")
def API():
    return {"message": "Welcome to Random Quotes API"}

@app.get("/all-quotes")
def ALL_QUOTES():
    return {"All quotes": all_quotes()}

# Endpoint without parameters
@app.get("/random-quote")
def RANDOM_QUOTE():
    return {"Lazy peoples:": random_quote()}

# Endpoint with query parameters
@app.get("/quotes-by-category")
def QUOTES_BY_CATEGORY(category: str):
    if len(category_quotes(category)) > 0:
        return {"Qoutes by category:": category_quotes(category)}
    else:
        return {"Failed": f"Can't find quotes related this category: {category}"}

@app.get("/quotes-in-quantity")
def QUOTES_IN_QUANTITY(quantity: int):
    if quantity > len(lazy_quotes):
        return {"error": f"You can't get more than {len(lazy_quotes)} quotes"}
    else:
        return {"All quotes:": quotes_in_quantity(quantity)}

@app.get("/quote-about")
def QUOTE_ABOUT(category: str):
    return {f"{category.capitalize()} Quotes": searching_quote(category)}

