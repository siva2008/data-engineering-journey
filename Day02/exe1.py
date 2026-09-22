sales = [
    {
        "order_id": 1001,
        "customer": "John",
        "quantity": 5,
        "price": 20
    },
    {
        "order_id": 1002,
        "customer": "Sarah",
        "quantity": 3,
        "price": "ABC"
    },
    {
        "order_id": 1003,
        "customer": "David",
        "quantity": 10,
        "price": 15
    }
]

def calculate_total(quantity, price):
     quantity = float(quantity)
     price = float(price)

     return quantity * price


for order in sales:

    try:
        total = calculate_total(
            order["quantity"],
            order["price"]
        )

        print(
            "Order:", order["order_id"],
            "Customer:", order["customer"],
            "Total:", total
        )

    except (TypeError, ValueError):
        print(
            "Invalid data for Order:",
            order["order_id"]
        )