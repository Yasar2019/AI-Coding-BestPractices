def calculate_order_total(items):
    """Return discounted subtotal rounded to two decimals.

    Each item must be a mapping with numeric ``price`` and integer ``quantity``.
    Orders with a subtotal of 100.00 or more receive a 10% discount.
    Negative quantities are invalid.
    """
    subtotal = 0.0
    for item in items:
        price = item["price"]
        quantity = item["quantity"]
        subtotal += price * quantity

    # Intentionally buggy starter implementation for Lab 02.
    if subtotal > 100:
        subtotal *= 0.90

    return round(subtotal, 2)
