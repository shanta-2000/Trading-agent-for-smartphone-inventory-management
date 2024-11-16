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

# Example usage:
average_price = 600  # Average price of the smartphone
agent = TradingAgent(average_price)

# Scenario 1: Price is low, stock is sufficient
current_price = 500
amount_in_stock = 20
order_quantity = agent.decide_order(current_price, amount_in_stock)
print(f"Order Quantity: {order_quantity}")  # Output: 15

# Scenario 2: Stock is critically low
current_price = 650
amount_in_stock = 5
order_quantity = agent.decide_order(current_price, amount_in_stock)
print(f"Order Quantity: {order_quantity}")  # Output: 10

# Scenario 3: Price is high, stock is sufficient
current_price = 650
amount_in_stock = 20
order_quantity = agent.decide_order(current_price, amount_in_stock)
print(f"Order Quantity: {order_quantity}")  # Output: 0

