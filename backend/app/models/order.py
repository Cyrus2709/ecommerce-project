class OrderItem:
    def __init__(self, productId: str, quantity: int, price: float):
        self.productId = productId
        self.quantity = quantity
        self.price = price


class Order:
    def __init__(self, orderId: str, date: str, customerId: str, items: list, total: float):
        self.orderId = orderId
        self.date = date
        self.customerId = customerId
        self.items = items
        self.total = total
