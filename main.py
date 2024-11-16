import random
import math

class TradingAgent:
    def __init__(self, average_price, critical_stock_level=10):
        self.average_price = average_price
        self.critical_stock_level = critical_stock_level
        self.discount_threshold = 0.20  # 20% discount

    def decide_order(self, current_price, amount_in_stock):
        # Check if the price is significantly discounted
        discounted_price = self.average_price * (1 - self.discount_threshold)
        if current_price < discounted_price:
            # Price is significantly lower
            if amount_in_stock >= self.critical_stock_level:
                tobuy = 15  # Order 15 units if stock level is sufficient
            else:
                tobuy = 10  # Order a minimum of 10 units if stock is critically low
        elif amount_in_stock < self.critical_stock_level:
            # Stock level is critically low
            tobuy = 10  # Order a minimum of 10 units
        else:
            # No need to order
            tobuy = 0

        return tobuy


average_price = 600  # Average price of the smartphone
agent = TradingAgent(average_price)


print("Trading Agent for Smartphone Inventory Management")
print("Enter 'exit' to stop the program.")

while True:
    try:
        user_price= input("Enter the current Price of the smartphone: ")
        if user_price.lower() == 'exit':
            break
        current_price =float(user_price)

        user_stock= input("Enter the current stock: ")
        if user_price.lower() == 'exit':
            break
        amount_in_stock =float(user_stock)

        order_quantity =agent.decide_order(current_price,amount_in_stock)

        print(f"Order Quantity: {order_quantity}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and stock.")   

print("Program terminated.")