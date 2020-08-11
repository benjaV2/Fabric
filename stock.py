LOCATION = "location"
AMOUNT = "amount"

stock = {"Milk": {AMOUNT: 10, "location": [5, 6]},
         "Bread": {AMOUNT: 10, "location": [1, 5]},
         "Salt": {AMOUNT: 10, "location": [6, 5]},
         "Soap": {AMOUNT: 10, "location": [8, 9]},
         "Pasta": {AMOUNT: 10, "location": [9, 2]}
         }


def get_location(product):
    return stock[product]["location"]


def add_stock(product):
    global stock
    stock[product][AMOUNT] += 1


def reduce_stock(product):
    global stock
    if stock[product][AMOUNT] > 0:
        stock[product][AMOUNT] -= 1
    else:
        raise Exception('not enough stock')


def get_stock():
    return [{'name': k, 'amount': v[AMOUNT]} for k, v in stock.items()]
