Electricity Consumption Analysis and Forecasting System


1. Project Overview

The Electricity Consumption Analysis and Forecasting System is a Python-based mini project designed to record, manage, and analyze monthly electricity consumption.

The system helps users understand their electricity usage by calculating total consumption, average consumption, and identifying the highest and lowest usage months. It also estimates future electricity consumption using a Weighted Moving Average method.

2. Project Objectives

1. To maintain monthly electricity consumption records.
2. To calculate total and average electricity usage.
3. To identify months with maximum and minimum consumption.
4. To estimate next month's electricity consumption.
5. To store records permanently using CSV file handling.

3. Technologies Used

- Programming Language: Python
- Concepts: Class and Object, Functions, Loops, Conditional Statements
- File Handling: CSV
- Module: CSV and Pathlib

4. Main Features

1. Add Monthly Electricity Reading
2. Display All Consumption Records
3. Calculate Total and Average Consumption
4. Compare Highest and Lowest Consumption
5. Forecast Future Electricity Usage
6. Save Records in a CSV File

5. Forecasting Method

The project uses the Three-Month Weighted Moving Average method.

The formula is:

Forecast = (A × 1 + B × 2 + C × 3) / 6

Where:

- A = First month's consumption
- B = Second month's consumption
- C = Third month's consumption

More weight is given to the most recent month's consumption.

6. Project Files

- electricity_consumption_system.py – Main Python source code.
- electricity_records.csv – Stores monthly electricity consumption records. This file is created automatically when the program saves records.

7. How to Run the Project

1. Install Python on your computer.
2. Download or clone this GitHub repository.
3. Open the project folder.
4. Run the following command:

python electricity_consumption_system.py

5. Select an option from the main menu.
6. Enter monthly electricity consumption details.

8. Expected Output

The system displays:

- Monthly electricity records
- Total electricity consumption
- Average electricity consumption
- Highest and lowest consumption
- Estimated next month's electricity consumption

9. Conclusion

This project provides a simple way to manage and analyze electricity consumption records. It helps users understand their electricity usage and estimate future consumption through Python programming and basic forecasting techniques.

10. Developed By

Name: Abhanjali
Roll Number: 25/SCA/BCOA/028
Course: Bachelor of Computer Applications (BCA)
Project Type: Individual Mini Project
Language: Python
