from project.legendary_item import LegendaryItem
import unittest


class TestLegendaryItem(unittest.TestCase):

    def setUp(self):
        self.item = LegendaryItem("AB-12", 40, 50, 100)

    def test_valid_initialization(self):
        self.assertEqual(self.item.identifier, "AB-12")
        self.assertEqual(self.item.power, 40)
        self.assertEqual(self.item.durability, 50)
        self.assertEqual(self.item.price, 100)

    def test_invalid_identifier_characters_raises(self):
        with self.assertRaises(ValueError) as cm:
            LegendaryItem("AB_12", 40, 50, 100)
        self.assertEqual(str(cm.exception), "Identifier can only contain letters, digits, or hyphens!")

    def test_invalid_identifier_length_raises(self):
        with self.assertRaises(ValueError) as cm:
            LegendaryItem("A1-", 40, 50, 100)
        self.assertEqual(str(cm.exception), "Identifier must be at least 4 characters long!")

    def test_negative_power_raises(self):
        with self.assertRaises(ValueError) as cm:
            LegendaryItem("AB-12", -1, 50, 100)
        self.assertEqual(str(cm.exception), "Power must be a non-negative integer!")

    def test_durability_below_range_raises(self):
        with self.assertRaises(ValueError) as cm:
            LegendaryItem("AB-12", 40, 0, 100)
        self.assertEqual(str(cm.exception), "Durability must be between 1 and 100 inclusive!")

    def test_durability_above_range_raises(self):
        with self.assertRaises(ValueError) as cm:
            LegendaryItem("AB-12", 40, 101, 100)
        self.assertEqual(str(cm.exception), "Durability must be between 1 and 100 inclusive!")

    def test_price_zero_raises(self):
        with self.assertRaises(ValueError) as cm:
            LegendaryItem("AB-12", 40, 50, 0)
        self.assertEqual(str(cm.exception), "Price must be a multiple of 10 and not 0!")

    def test_price_not_multiple_of_10_raises(self):
        with self.assertRaises(ValueError) as cm:
            LegendaryItem("AB-12", 40, 50, 55)
        self.assertEqual(str(cm.exception), "Price must be a multiple of 10 and not 0!")

    def test_is_precious_false_below_50(self):
        self.assertFalse(self.item.is_precious)

    def test_is_precious_true_at_50(self):
        item = LegendaryItem("XY-99", 50, 50, 100)
        self.assertTrue(item.is_precious)

    def test_is_precious_true_above_50(self):
        item = LegendaryItem("XY-99", 60, 50, 100)
        self.assertTrue(item.is_precious)

    def test_enhance_increases_power_price_and_durability(self):
        self.item.enhance()
        self.assertEqual(self.item.power, 80)
        self.assertEqual(self.item.price, 110)
        self.assertEqual(self.item.durability, 60)

    def test_enhance_caps_durability_at_100(self):
        item = LegendaryItem("AA-11", 10, 95, 50)
        item.enhance()
        self.assertEqual(item.durability, 100)

    def test_evaluate_eligible(self):
        item = LegendaryItem("AA-11", 60, 80, 50)
        result = item.evaluate(70)
        self.assertEqual(result, "AA-11 is eligible.")

    def test_evaluate_not_eligible_due_to_durability(self):
        item = LegendaryItem("AA-11", 60, 50, 50)
        result = item.evaluate(70)
        self.assertEqual(result, "Item not eligible.")

    def test_evaluate_not_eligible_due_to_power(self):
        item = LegendaryItem("AA-11", 40, 90, 50)
        result = item.evaluate(70)
        self.assertEqual(result, "Item not eligible.")


if __name__ == "__main__":
    unittest.main()


