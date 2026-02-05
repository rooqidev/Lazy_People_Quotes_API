lazy_quotes = [
    "I’m not lazy, I’m on energy-saving mode.",
    "Doing nothing is my favorite hobby.",
    "I put the pro in procrastinate.",
    "Why rush when you can nap?",
    "I’ll do it later. Later is my time.",
    "My bed and I are in a committed relationship.",
    "Hard work never killed anyone, but why risk it?",
    "If it requires effort, I’ll think about it tomorrow.",
    "I woke up tired.",
    "I’m not lazy, I’m just highly relaxed.",
    "Today’s goal: survive.",
    "I work smart so I can work less.",
    "Sleep now, conquer never.",
    "I’m busy doing nothing.",
    "Motivation is on vacation.",
    "If at first you don’t succeed, nap.",
    "I have a strong dislike for unnecessary movement.",
    "Why stand when you can sit?",
    "My brain needs a loading screen.",
    "I’ll start after this break.",
    "Effort detected. Abort mission.",
    "I’m not avoiding work, I’m postponing greatness.",
    "Nap first, think later.",
    "I do my best work in bed.",
    "Today feels like a tomorrow problem.",
    "I came. I saw. I decided to nap.",
    "My to-do list ran away.",
    "Laziness is just efficiency misunderstood.",
    "Too tired to be tired.",
    "I run on caffeine and excuses.",
    "If it’s not urgent, it’s optional.",
    "I’ll do it… eventually.",
    "Brain says yes, body says no.",
    "Minimum effort, maximum comfort.",
    "I was productive once. It was awful.",
    "Resting is a lifestyle.",
    "Why do today what tomorrow can forget?",
    "I’m conserving energy for later decades.",
    "Busy resting.",
    "This looks like a future me problem.",
    "Effort is overrated.",
    "I specialize in doing the bare minimum.",
    "Sleep is my spirit animal.",
    "I’m not slow, I’m relaxed.",
    "Work hard? I barely work.",
    "Currently buffering.",
    "I plan to be productive… someday.",
    "My motivation has left the chat.",
    "I tried. That’s enough.",
    "Doing nothing takes skill.",
    "Rest now, panic later.",
    "I function best horizontally.",
    "I choose comfort over chaos.",
    "Today’s achievement: stayed in bed."
]
from random import choice
def random_quote():
    return choice(lazy_quotes)

def all_quotes():
    return lazy_quotes

quotes_Category = []
def category_quotes(query):
    global qoutes_Category
    quotes_Category = []
    for quote in lazy_quotes:
        if query.lower() in quote.lower():
            quotes_Category.append(quote)
    return quotes_Category

quotes_in_qty = []
def quotes_in_quantity(quantity):
    global quotes_in_qty
    for index in range(quantity):
        quotes_in_qty.append(choice(lazy_quotes))
    return quotes_in_qty

that_quotes = []
def search_quote(query):
    for quote in lazy_quotes:
        if query.lower() in quote.lower():
            that_quotes.append(quote)
        else:
            continue

def searching_quote(query):
    global that_quotes
    search_quote(query)
    if len(that_quotes) > 0:
        return choice(that_quotes)
        that_quotes = []
    else:
        return f"Sorry!, there's no qoute related {query}"

if __name__ == "__main__":
    print(random_quote())
