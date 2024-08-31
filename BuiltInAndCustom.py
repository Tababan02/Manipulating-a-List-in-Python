price = [10, 20, 30, 40, 50]
def maxCustom(price):
    price = 0
    for price in price:
        if price > max_price:
            max_price = price
    return max_price

# Built-in function
print(max(price))
print(min(price))

#custom function
print(maxCustom(price))