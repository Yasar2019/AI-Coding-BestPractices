import unittest

from order_total import calculate_order_total


class OrderTotalTests(unittest.TestCase):
    def test_empty_cart(self):
        self.assertEqual(calculate_order_total([]), 0.00)

    def test_below_discount_threshold(self):
        items = [{"price": 49.99, "quantity": 2}]
        self.assertEqual(calculate_order_total(items), 99.98)

    def test_exact_discount_threshold(self):
        items = [{"price": 25.00, "quantity": 4}]
        self.assertEqual(calculate_order_total(items), 90.00)

    def test_above_discount_threshold(self):
        items = [{"price": 60.00, "quantity": 2}]
        self.assertEqual(calculate_order_total(items), 108.00)

    def test_negative_quantity_is_rejected(self):
        items = [{"price": 10.00, "quantity": -1}]
        with self.assertRaises(ValueError):
            calculate_order_total(items)

    def test_rounds_final_total_to_two_decimals(self):
        items = [{"price": 33.335, "quantity": 3}]
        self.assertEqual(calculate_order_total(items), 90.00)


if __name__ == "__main__":
    unittest.main()
