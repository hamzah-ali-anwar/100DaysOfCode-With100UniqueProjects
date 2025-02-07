''' It's almost the Summer Sales!
 
# You work for a shop that wishes to give a discount of discount% to the most and least expensive item purchased by a given customer during the sales period. Only two products can benefit from the discount. 
#   You are tasked by the shop owner to implement the function calculateTotalPrice(prices, discount) which takes the list of prices of the products purchased by a customer and the percentage discount as parameters and returns the total purchase price as an integer (rounded down if the total is a float number).
 
#  Constraints:
#  0 ≤ discount ≤ 100
#  0 < price of a product < 100000
#  0 < number of products < 100 '''

def calculateTotalPrice(prices: list[int], discount: int) -> int:
    if not prices or discount < 0 or discount > 100:
        return 0 # Edge case handling
    
    # Find most and least expensive item
    most_expensive = max(prices)
    least_expensive = min(prices)

    # Calculate discount
    discount_amount = (most_expensive + least_expensive) * (discount / 100)

    # Calculate total price after discount
    total_price = sum(prices) - discount_amount

    return int(total_price)

prices = [200, 150, 50, 400, 600]
discount = 20
print(calculateTotalPrice(prices, discount))