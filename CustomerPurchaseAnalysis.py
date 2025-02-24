import pandas as pd


def create_dataframe():
    """
    Create and return a DataFrame containing customer purchase data.
    """
    # Predefined customer purchase dataset
    data = {
        'Customer': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Items_Bought': [3, 7, 5, 2, 9],
        'Amount_Spent': [150.0, 400.0, 275.0, 100.0, 600.0]
    }
    # TODO: Create DataFrame from 'data'
    pass


def calculate_average_spending(df):
    """
    Calculate and return the average spending amount.
    """
    # TODO: Calculate mean of 'Amount_Spent'
    pass


def get_top_spenders(df, average_spending):
    """
    Identify and return customers who spent above the average amount.
    """
    # TODO: Filter customers spending above the average
    pass


def main():
    """
    Main function to execute customer purchase analysis.
    """
    # TODO: Create DataFrame
    # TODO: Calculate average spending
    # TODO: Identify and print top spenders

    # TODO: Print the DataFrame
    # TODO: Display high-spending customers
    pass


if __name__ == "__main__":
    main()
