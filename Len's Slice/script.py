
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2,6,1,3,2,7,2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(toppings)
print(num_pizzas)
num_pizzas = 7
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
pizza_and_prices = [[ 2, "pepperoni"], [6, "pineapple"], [1,"cheese"], [3, "sausage"], [2, "olives"], [7,"anchovies"], [2,"mushrooms"] ]
print(pizza_and_prices)
pizza_and_prices.sort()
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
print(pizza_and_prices)
pizza_and_prices.pop()
print(pizza_and_prices)
pizza_and_prices.insert(4, [2.5, "peppers"])
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
