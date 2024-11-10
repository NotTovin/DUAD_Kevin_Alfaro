import json

def load_data():
    try:
        with open('financials.json', 'r') as file:
            financials = json.load(file)
    except FileNotFoundError:
        financials = {'categories': [], 'movements': []}
    return financials


def save_data(financials):
    with open('financials.json', 'w') as file:
        json.dump(financials, file, indent = 4)