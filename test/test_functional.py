import unittest
import os
import pandas as pd
from test.TestUtils import TestUtils

from CustomerPurchaseAnalysis import *
from InventoryManagement import *
from WeatherAnalysis import *

class TestCustomerPurchaseNew(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()

    def test_create_dataframe(self):
        try:
            df = create_dataframe()
            self.assertEqual(len(df), 5)
            self.assertListEqual(list(df.columns), ['Customer', 'Items_Bought', 'Amount_Spent'])
            self.test_obj.yakshaAssert("test_create_dataframe", True, "functional")
            print("test_create_dataframe = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_create_dataframe", False, "exception")
            print("test_create_dataframe = Failed")

    def test_average_spending(self):
        try:
            df = create_dataframe()
            avg = calculate_average_spending(df)
            self.assertEqual(avg, 375.0)
            self.test_obj.yakshaAssert("test_average_spending", True, "functional")
            print("test_average_spending = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_average_spending", False, "exception")
            print("test_average_spending = Failed")

    def test_top_spenders(self):
        try:
            df = create_dataframe()
            avg = calculate_average_spending(df)
            top_df = get_top_spenders(df, avg)

            # Check that there are 2 top spenders
            self.assertEqual(len(top_df), 2)

            # Check that their names are Mike and Leo
            self.assertIn("Mike", top_df['Customer'].values)
            self.assertIn("Leo", top_df['Customer'].values)

            # Optionally, ensure ONLY Mike and Leo are in result
            self.assertSetEqual(set(top_df['Customer'].values), {"Mike", "Leo"})

            self.test_obj.yakshaAssert("test_top_spenders", True, "functional")
            print("test_top_spenders = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_top_spenders", False, "exception")
            print("test_top_spenders = Failed")


class TestInventoryManagementNew(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.inventory = [("Tablet", 8), ("Pen Drive", 60), ("Router", 4), ("Camera", 2), ("HDMI Cable", 30)]
        cls.prices = {
            "Tablet": 300,
            "Pen Drive": 20,
            "Router": 100,
            "Camera": 500,
            "HDMI Cable": 10
        }

    def test_new_low_stock_items(self):
        try:
            result = get_low_stock_items(self.inventory, 10)
            expected = ['Tablet', 'Router', 'Camera']
            self.assertSetEqual(set(result), set(expected))
            self.test_obj.yakshaAssert("test_new_low_stock_items", True, "functional")
            print("test_new_low_stock_items = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_new_low_stock_items", False, "exception")
            print("test_new_low_stock_items = Failed")


    def test_new_inventory_value(self):
        try:
            value = calculate_inventory_value(self.inventory, self.prices)
            expected = 8*300 + 60*20 + 4*100 + 2*500 + 30*10  # = 5300
            self.assertEqual(value, expected)
            self.test_obj.yakshaAssert("test_new_inventory_value", True, "functional")
            print("test_new_inventory_value = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_new_inventory_value", False, "exception")
            print("test_new_inventory_value = Failed")


class TestWeatherFileUseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.filename = "temperatures.txt"
        # Write test file
        with open(cls.filename, "w") as f:
            f.write("28.5\n30.0\n33.7\n36.1\n29.0\n")
        cls.expected_temps = [28.5, 30.0, 33.7, 36.1, 29.0]

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.filename):
            os.remove(cls.filename)

    def test_read_temperatures(self):
        try:
            temps = read_temperatures_from_file(self.filename)
            self.assertEqual(temps, self.expected_temps)
            self.test_obj.yakshaAssert("test_read_temperatures", True, "functional")
            print("test_read_temperatures = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_read_temperatures", False, "exception")
            print("test_read_temperatures = Failed")

    def test_analyze_temperature_values(self):
        try:
            report = analyze_temperatures(self.expected_temps)
            self.assertIn("Highest Temperature: 36.1", report)
            self.assertIn("Lowest Temperature: 28.5", report)
            self.assertIn("Extreme Temperatures Detected: [28.5, 29.0, 36.1]", report)
            self.test_obj.yakshaAssert("test_analyze_temperature_values", True, "functional")
            print("test_analyze_temperature_values = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_analyze_temperature_values", False, "exception")
            print("test_analyze_temperature_values = Failed")



if __name__ == "__main__":
    unittest.main()
