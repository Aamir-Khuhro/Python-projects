import csv
import json
from prettytable import PrettyTable

def store_sample_data():
    """
    Store sample sales data for restaurant menu in CSV file named 'menu.csv'.
    We will add more fields in data given in assessment. It will help us to perform the required tasks.
    """
    # Define the field names for sample sales data
    fields = ['item', 'price', 'category', 'items_sold_Mon', 'items_sold_Tue', 'items_sold_Wed',
              'items_sold_Thu', 'items_sold_Fri', 'items_sold_Sat', 'items_sold_Sun', 'customer_ratings']

    # Define the data rows for sample sales data
    rows = [
        ['Chicken Parmigiana', 19.99, 'Main', 30, 25, 20, 35, 40, 57, 78, [4.5, 5.0, 4.5, 4.0, 3.5]],
        ['Fish and Chips', 18.99, 'Main', 14, 25, 18, 22, 25, 35, 45, [4.5, 4.5, 4.5, 4.2, 5.0]],
        ['Margherita Pizza', 15.99, 'Main', 15, 28, 20, 31, 40, 43, 55, [5.0, 4.0, 4.5, 4.4, 3.8]],
        ['Caesar Salad', 9.99, 'Starter', 18, 20, 22, 18, 18, 23, 23, [4.5, 4.0, 4.5, 4.2, 5.0]],
        ['Garlic Bread', 6.99, 'Starter', 18, 8, 11, 15, 18, 11, 31, [3.5, 4.0, 4.0, 3.8, 4.3]],
        ['Tiramisu', 7.99, 'Dessert', 25, 20, 31, 25, 30, 33, 45, [4.5, 5.0, 4.5, 4.5, 3.5]],
        ['Cheesecake', 6.99, 'Dessert', 25, 18, 22, 20, 22, 25, 26, [4.0, 4.0, 4.2, 4.5, 5.0]],
    ]

    # Store the sample sales data in 'menu.csv' file
    with open('menu.csv', 'w', newline='') as file:
        # Create file writer object
        writer = csv.writer(file)

        # Write field names in file
        writer.writerow(fields)

        # Write rows in file
        writer.writerows(rows)


def display_menu_data():
    """
    Display the restaurant menu data in table format.
    """

    # Read data from the CSV file
    try:
        with open('menu.csv', 'r') as file:
            # Create dictionary reader object
            reader = csv.reader(file)

            # Create a PrettyTable object
            table = PrettyTable()

            # Add columns to the table
            table.field_names = next(reader)

            # Add rows to the table
            for row in reader:
                table.add_row(row)

            # Print the table
            print(table)
    except FileNotFoundError:
        print("Error: 'menu.csv' file not found.")


def calculate_average_ratings():
    """
    Calculate the average rating for each menu item.
    """
    # Read menu data from file
    try:
        with open('menu.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Reading the first row and moving to the second row, as we need to process data, not fields

            # Create a PrettyTable object
            table = PrettyTable()

            # Add columns to the table
            table.field_names = ['Item', 'Avg. rating']

            for row in reader:
                item = row[0]
                item_ratings = json.loads(row[-1])  # Using json.loads to safely convert the string representation of the list to a list
                item_avg_rating = sum(item_ratings) / len(item_ratings)
                table.add_row([item, f'{item_avg_rating:.1f}'])
            print(table)
    except FileNotFoundError:
        print("Error: 'menu.csv' file not found.")


def calculate_sales_of_each_day():
    """
    Calculates total sales of all items for each day of the week.
    """
    # Read menu data from file
    try:
        with open('menu.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Reading the first row and moving to the second row, as we need to process data, not fields
            data = [row for row in reader]  # Converting iterable reader to a 2D array to make data access easier

            # Create a PrettyTable object
            table = PrettyTable()

            # Add columns to the table
            table.field_names = ['Day', 'Total Sales']

            days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

            for j, day in zip(range(3, 10), days):
                day_sales = 0
                # Go through all rows
                for i in range(len(data)):
                    item_price = float(data[i][1]) # Convert string float type as price can be in pointss
                    num_of_items_sold = int(data[i][j]) # Convert string to int type as quantity is always integer
                    item_sales = item_price * num_of_items_sold # Calculating sales of particular item
                    day_sales += item_sales # Add to day's total sales
                table.add_row([day, f'{day_sales:.2f}']) 
            print(table)
    except FileNotFoundError:
        print("Error: 'menu.csv' file not found.")


def determine_most_popular_item():
    """
    Finds the most popular item based on the menu based on its rating.
    """
    try:
        with open('menu.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Reading the first row and moving to the second row, as we need to process data, not fields
            avg_ratings = []  # Ratings list to keep average ratings of all items
            data = [row for row in reader]  # Converting iterable reader to a 2D array to make data access easier

            for row in data:
                ratings = row[-1]  # Last column in each row has a list of ratings for the item
                ratings = json.loads(ratings)  # Using json.loads to safely convert the string representation of the list to a list
                avg_ratings.append(sum(ratings) / len(ratings))  # Add average rating of each item to the list average ratings

            # Finding item with the best rating
            max_rating = max(avg_ratings)
            index_of_max = avg_ratings.index(max_rating)  # Getting index of maximum rating in the list
            max_rating_item = data[index_of_max][0]  # Item is in the first column
            print(f'Most popular Item: {max_rating_item}')
    except FileNotFoundError:
        print("Error: 'menu.csv' file not found.")


if __name__ == "__main__":
    store_sample_data()
    display_menu_data()
    calculate_average_ratings()
    calculate_sales_of_each_day()
    determine_most_popular_item()
