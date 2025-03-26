''' It's almost the Summer Sales!
 
# You work for a shop that wishes to give a discount of discount% to 
# the most and least expensive item purchased by a given customer 
# during the sales period. Only two products can benefit from the 
# discount. 
# You are tasked by the shop owner to implement the function 
# calculateTotalPrice(prices, discount) which takes the list of 
# prices of the products purchased by a customer and the percentage
#  discount as parameters and returns the total purchase price as an 
# integer (rounded down if the total is a float number).
 
#  Constraints:
#  0 ≤ discount ≤ 100
#  0 < price of a product < 100000
#  0 < number of products < 100 '''

import math 

def calculateTotalPrice(prices, discount):
    if not prices or discount < 0 or discount > 100:
        raise ValueError("Invalid input: Ensure prices are provided and discount is between 0 and 100")
    
    max_price = max(prices)
    min_price = min(prices)

    discount_amount = (max_price + min_price) * (discount / 100) # 120
    print(f"Discount amount: {discount_amount}")

    total_price = sum(prices) - discount_amount # 1500 - 120 = 1380
    print(f"Total price: {total_price}")

    return math.floor(total_price)

prices = [100, 200, 300, 400, 500]
discount = 20
print(calculateTotalPrice(prices, discount))
