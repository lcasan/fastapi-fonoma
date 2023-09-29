from models import Order, Criterion

def process_orders(orders: list[Order], criterion: Criterion) -> float:
    """
    This function filter the orders based on the criterion 
    and return the total revenue for the filtered orders.
    """

    total = 0.0

    if criterion != "all":
        for order in orders:
            if order.status == criterion:
                total += (order.quantity * order.price)
    else:
        for order in orders:
            total += (order.quantity * order.price)
    
    return total