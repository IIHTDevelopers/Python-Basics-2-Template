import unittest
import pandas as pd
import numpy as np
import sys
import os

# Adjusting the path to import the refactored script and TestUtils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from CustomerPurchaseAnalysis import (
    create_dataframe,
    calculate_average_spending,
    get_top_spenders,

)


class TestCustomerPurchaseAnalysis(unittest.TestCase):
    def setUp(self):
        # Initialize the TestUtils object
        self.test_obj = TestUtils()
        # Create the DataFrame using the refactored function
        self.df = create_dataframe()
        # Calculate the average spending for testing
        self.average_spending = calculate_average_spending(self.df)

    def test_create_dataframe(self):
        try:
            # Check if DataFrame is created correctly
            expected_data = {
                'Customer': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
                'Items_Bought': [3, 7, 5, 2, 9],
                'Amount_Spent': [150.0, 400.0, 275.0, 100.0, 600.0]
            }
            expected_df = pd.DataFrame(expected_data)
            result = self.df.equals(expected_df)

            if result:
                self.test_obj.yakshaAssert("TestCreateDataFrame", True, "functional")
                print("TestCreateDataFrame = Passed")
            else:
                self.test_obj.yakshaAssert("TestCreateDataFrame", False, "functional")
                print("TestCreateDataFrame = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCreateDataFrame", False, "functional")
            print(f"TestCreateDataFrame = Failed ")

    def test_average_spending(self):
        try:
            # Check the average spending
            expected_average = np.mean([150.0, 400.0, 275.0, 100.0, 600.0])
            result = round(self.average_spending, 2) == round(expected_average, 2)

            if result:
                self.test_obj.yakshaAssert("TestAverageSpending", True, "functional")
                print("TestAverageSpending = Passed")
            else:
                self.test_obj.yakshaAssert("TestAverageSpending", False, "functional")
                print("TestAverageSpending = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestAverageSpending", False, "functional")
            print(f"TestAverageSpending = Failed ")

    def test_top_spenders(self):
        try:
            # Identify customers who spent above the average
            top_spenders = get_top_spenders(self.df, self.average_spending)
            expected_top_spenders = pd.DataFrame({
                'Customer': ['Bob', 'Eve'],
                'Items_Bought': [7, 9],
                'Amount_Spent': [400.0, 600.0]
            }).reset_index(drop=True)

            result = top_spenders.reset_index(drop=True).equals(expected_top_spenders)

            if result:
                self.test_obj.yakshaAssert("TestTopSpenders", True, "functional")
                print("TestTopSpenders = Passed")
            else:
                self.test_obj.yakshaAssert("TestTopSpenders", False, "functional")
                print("TestTopSpenders = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTopSpenders", False, "functional")
            print(f"TestTopSpenders = Failed ")



if __name__ == '__main__':
    unittest.main()

import unittest
import sys
import os

# Adjusting the path to import TestUtils and the inventory module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from InventoryManagement import (
    get_low_stock_items,
    calculate_inventory_value,

)


class TestInventoryManagement(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

        # Dataset: Inventory and Prices
        self.inventory_data = [
            ("Laptop", 5),
            ("Mouse", 20),
            ("Keyboard", 12),
            ("Monitor", 3),
            ("USB Drive", 50)
        ]

        self.item_prices = {
            "Laptop": 1000,
            "Mouse": 25,
            "Keyboard": 80,
            "Monitor": 300,
            "USB Drive": 15
        }
        self.reorder_level = 10

    def test_get_low_stock_items(self):
        try:
            # Get low stock items
            result = get_low_stock_items(self.inventory_data, self.reorder_level)
            expected_result = ["Laptop", "Monitor"]

            if result == expected_result:
                self.test_obj.yakshaAssert("TestGetLowStockItems", True, "functional")
                print("TestGetLowStockItems = Passed")
            else:
                self.test_obj.yakshaAssert("TestGetLowStockItems", False, "functional")
                print("TestGetLowStockItems = Failed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestGetLowStockItems", False, "functional")
            print(f"TestGetLowStockItems = Failed ")

    def test_calculate_inventory_value(self):
        try:
            # Calculate total inventory value
            result = calculate_inventory_value(self.inventory_data, self.item_prices)
            expected_result = 8110

            if result == expected_result:
                self.test_obj.yakshaAssert("TestCalculateInventoryValue", True, "functional")
                print("TestCalculateInventoryValue = Passed")
            else:
                self.test_obj.yakshaAssert("TestCalculateInventoryValue", False, "functional")
                print("TestCalculateInventoryValue = Failed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateInventoryValue", False, "functional")
            print(f"TestCalculateInventoryValue = Failed ")


if __name__ == '__main__':
    unittest.main()

import unittest
import sys
import os

# Adjusting the path to import TestUtils and the weather module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from WeatherAnalysis import (
    weather_analysis,
    save_report_to_file
)


class TestWeatherAnalysis(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

        # Sample temperature dataset
        self.temperatures = {32.5, 34.0, 31.2, 29.8, 35.5}
        self.expected_sorted_temps = [29.8, 31.2, 32.5, 34.0, 35.5]
        self.expected_max_temp = 35.5
        self.expected_min_temp = 29.8
        self.expected_extreme_temps = [29.8, 35.5]
        self.expected_report = f"""
    Weather Analysis Report
    ------------------------
    Temperatures (°C): {self.expected_sorted_temps}
    Highest Temperature: {self.expected_max_temp}
    Lowest Temperature: {self.expected_min_temp}
    Extreme Temperatures Detected: {self.expected_extreme_temps}
    """

    def test_weather_analysis(self):
        try:
            # Perform weather analysis
            report = weather_analysis(self.temperatures)

            # Verify the content of the report
            result = (
                    f"Temperatures (°C): {self.expected_sorted_temps}" in report and
                    f"Highest Temperature: {self.expected_max_temp}" in report and
                    f"Lowest Temperature: {self.expected_min_temp}" in report and
                    f"Extreme Temperatures Detected: {self.expected_extreme_temps}" in report
            )

            if result:
                self.test_obj.yakshaAssert("TestWeatherAnalysis", True, "functional")
                print("TestWeatherAnalysis = Passed")
            else:
                self.test_obj.yakshaAssert("TestWeatherAnalysis", False, "functional")
                print("TestWeatherAnalysis = Failed")
                print("Expected Report:\n", self.expected_report)
                print("Actual Report:\n", report)
        except Exception as e:
            self.test_obj.yakshaAssert("TestWeatherAnalysis", False, "functional")
            print(f"TestWeatherAnalysis = Failed | Exception: {e}")

    def test_save_report_to_file(self):
        try:
            # Filename for testing
            test_filename = "test_weather_report.txt"

            # Save report to file
            save_report_to_file(self.expected_report, test_filename)

            # Check if file exists and has the correct content
            if os.path.exists(test_filename):
                with open(test_filename, "r", encoding="utf-8") as file:
                    content = file.read()
                    result = self.expected_report.strip() in content.strip()

                    if result:
                        self.test_obj.yakshaAssert("TestSaveReportToFile", True, "functional")
                        print("TestSaveReportToFile = Passed")
                    else:
                        self.test_obj.yakshaAssert("TestSaveReportToFile", False, "functional")
                        print("TestSaveReportToFile = Failed")
                        print("Expected Content:\n", self.expected_report)
                        print("Actual Content:\n", content)
            else:
                self.test_obj.yakshaAssert("TestSaveReportToFile", False, "functional")
                print("TestSaveReportToFile = Failed | File not found")

            # Clean up
            if os.path.exists(test_filename):
                os.remove(test_filename)
        except Exception as e:
            self.test_obj.yakshaAssert("TestSaveReportToFile", False, "functional")
            print(f"TestSaveReportToFile = Failed | Exception: {e}")


if __name__ == '__main__':
    unittest.main()
