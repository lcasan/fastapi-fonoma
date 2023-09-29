from models import Order, Criterion

def process_orders(orders: list[Order], criterion: Criterion):
    total = 0.0
    for order in orders:
        if order.status == criterion:
            total += (order.quantity * order.price)
    return total