import csv


def calculate_total(quantity, price):
    quantity = int(quantity)
    price = float(price)

    return quantity * price


def validate_order(order):
    if not order["quantity"]:
        return False

    if not order["price"]:
        return False

    try:
        int(order["quantity"])
        float(order["price"])
    except (ValueError, TypeError):
        return False

    return True


with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if not validate_order(row):
            print("Invalid data for Order:", row["order_id"])
            continue

        try:
            total = calculate_total(
                row["quantity"],
                row["price"]
            )

            print(
                "Order:", row["order_id"],
                "Customer:", row["customer"],
                "Total:", total
            )

        except (ValueError, TypeError):
            print("Error processing Order:", row["order_id"])