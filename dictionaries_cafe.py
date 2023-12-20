"""
Use dictionaries to calculate the total value of the stock for items on a cafe menu
"""
# declare variable to hold total value of stock

total_stock = 0

# list types of stock

menu = ["mushroom","egg","tomato","sausage"]

# create dictionary of number of items

stock_dict = {
            "mushroom": 10,
            "egg": 25,
            "tomato": 2,
            "sausage": 8
}

# create dictionary of price of items

price_dict = {
            "mushroom": 1,
            "egg": 3,
            "tomato": 2,
            "sausage": 4
}

# loop through menu items and look up values in both dictionaries to multiply together to get total


for item in menu:
    total_stock += stock_dict[item] * price_dict[item]

print(f"Total value of all stock = £ {total_stock}")

