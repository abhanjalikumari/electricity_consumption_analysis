"""
Project Title: Electricity Consumption Analysis and Forecasting System
Student Name: Abhanjali
Roll Number: 25/SCA/BCOA/028
Course: BCA
Language: Python
"""

import csv
from pathlib import Path

DATA_FILE = Path(__file__).with_name("electricity_records.csv")

MONTHS = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]


class ElectricityAnalyzer:

    def __init__(self):
        self.records = []
        self.load_data()

    # Load saved electricity records
    def load_data(self):
        if not DATA_FILE.exists():
            return

        try:
            with open(DATA_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    try:
                        month = row["Month"].strip().title()
                        year = int(row["Year"])
                        units = float(row["Units"])

                        if month in MONTHS and year > 0 and units >= 0:
                            self.records.append({
                                "month": month,
                                "year": year,
                                "units": units
                            })

                    except (ValueError, KeyError):
                        continue

            self.sort_data()

        except OSError:
            print("Unable to load previous records.")

    # Arrange records month-wise
    def sort_data(self):
        self.records.sort(
            key=lambda x: (
                x["year"],
                MONTHS.index(x["month"])
            )
        )

    # Save records in CSV file
    def save_data(self):
        try:
            with open(DATA_FILE, "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(["Month", "Year", "Units"])

                for item in self.records:
                    writer.writerow([
                        item["month"],
                        item["year"],
                        item["units"]
                    ])

            print("Records saved successfully.")

        except OSError:
            print("Error while saving records.")

    # Add a new monthly reading
    def add_reading(self):
        print("\n--- ADD ELECTRICITY READING ---")

        month = input("Enter month: ").strip().title()

        if month not in MONTHS:
            print("Invalid month name.")
            return

        try:
            year = int(input("Enter year: "))
            units = float(input("Enter electricity units: "))

        except ValueError:
            print("Please enter valid numeric values.")
            return

        if year <= 0 or units < 0:
            print("Year must be positive and units cannot be negative.")
            return

        for item in self.records:
            if item["month"] == month and item["year"] == year:
                print("This month's record already exists.")
                return

        self.records.append({
            "month": month,
            "year": year,
            "units": units
        })

        self.sort_data()
        self.save_data()

        print("New electricity reading added successfully.")

    # Display all monthly readings
    def display_records(self):
        if not self.records:
            print("No electricity records found.")
            return

        print("\n========== MONTHLY RECORDS ==========")

        print("{:<15}{:<10}{:>12}".format(
            "Month", "Year", "Units"
        ))

        print("-" * 37)

        for item in self.records:
            print("{:<15}{:<10}{:>12.2f}".format(
                item["month"],
                item["year"],
                item["units"]
            ))

        print("=" * 37)

    # Calculate total and average consumption
    def consumption_summary(self):
        if not self.records:
            print("No data available.")
            return

        values = [item["units"] for item in self.records]

        total = sum(values)
        average = total / len(values)

        print("\n====== CONSUMPTION SUMMARY ======")
        print("Total Consumption:", round(total, 2), "units")
        print("Average Consumption:", round(average, 2), "units")
        print("Total Months Recorded:", len(values))

    # Find highest and lowest consumption
    def compare_consumption(self):
        if not self.records:
            print("No data available for comparison.")
            return

        highest = max(self.records, key=lambda x: x["units"])
        lowest = min(self.records, key=lambda x: x["units"])

        print("\n====== USAGE COMPARISON ======")

        print("Highest Consumption:")
        print(highest["month"], highest["year"],
              "-", highest["units"], "units")

        print("\nLowest Consumption:")
        print(lowest["month"], lowest["year"],
              "-", lowest["units"], "units")

    # Forecast next month's consumption
    def forecast_usage(self):
        if len(self.records) < 3:
            print("At least 3 monthly records are required.")
            return

        recent_records = self.records[-3:]
        weights = [1, 2, 3]
        weighted_total = 0

        print("\n====== FUTURE CONSUMPTION FORECAST ======")

        for record, weight in zip(recent_records, weights):
            print(
                record["month"],
                record["year"],
                ":",
                record["units"],
                "units"
            )

            weighted_total += record["units"] * weight

        forecast = weighted_total / sum(weights)

        print("\nEstimated Next Month Consumption:",
              round(forecast, 2), "units")

        print("Method: Three-Month Weighted Moving Average")
        print("This value is an estimate, not an actual reading.")

    # Main menu of the application
    def main_menu(self):
        print("\nELECTRICITY CONSUMPTION ANALYSIS SYSTEM")

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. Add Monthly Electricity Reading")
            print("2. Display All Records")
            print("3. View Consumption Summary")
            print("4. Compare Monthly Consumption")
            print("5. Forecast Future Consumption")
            print("6. Save Records")
            print("7. Exit")
            print("================================")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_reading()

            elif choice == "2":
                self.display_records()

            elif choice == "3":
                self.consumption_summary()

            elif choice == "4":
                self.compare_consumption()

            elif choice == "5":
                self.forecast_usage()

            elif choice == "6":
                self.save_data()

            elif choice == "7":
                self.save_data()
                print("Thank you for using the system!")
                break

            else:
                print("Invalid choice. Select from 1 to 7.")


# Start the project
if __name__ == "__main__":
    application = ElectricityAnalyzer()
    application.main_menu()
