AI-Powered Demand Forecaster for a Phone Repair Shop

This project is a complete, real-world tool that uses Python and the Prophet forecasting library to predict the daily number of repair requests for a small business.

The goal is to help the shop owner optimize staffing and inventory by anticipating busy periods (like the post-holiday rush) and slow periods.

The Business Problem

Small businesses like phone repair shops run on thin margins.

Over-staffing on a slow day loses money.

Under-staffing on a busy day leads to bad customer service and lost revenue.

Over-stocking on parts (like iPhone screens) ties up cash.

This tool solves this by providing a 6-month forecast based on historical data.

Key Features

Data-Driven: The model is not hard-coded; it reads data from phone_repair_shop_data.csv.

Seasonal Detection: The AI automatically detects and models complex patterns, like:

Weekly patterns (e.g., more repairs on Mondays and Saturdays).

Yearly patterns (e.g., a major spike in January/February after people drop their new holiday phones).

Modular Scripts: The project is split into two professional scripts:

generate_sample_csv.py: A helper script to create 2 years of realistic sample data.

demand_forecaster.py: The main AI tool that loads the data, trains the model, and plots the forecast.

Forecast Results

The model's predictions (blue line) are plotted against the historical data (black dots). The light-blue shaded area shows the 95% confidence interval for the 6-month forecast.

Forecast Component Analysis

This is why the model is making its predictions. It breaks down the data into its core patterns:

Trend: Shows the shop's steady, long-term growth.

Weekly: Confirms that business is slowest on Sundays and peaks on Mondays/Saturdays.

Yearly: Clearly identifies the massive spike in Jan/Feb and a slow period in late summer.

How to Run This Project

You can run this entire project on your local machine.

Clone the repository (or download the ZIP):

git clone [https://github.com/rohitjawahar/Demand-Forecasting-Model.git](https://github.com/rohitjawahar/Demand-Forecasting-Model.git)
cd Phone-Repair-Demand-Forecasting


Install the required libraries:

pip install -r requirements.txt


Run the data generator (Run this once):
This creates the phone_repair_shop_data.csv file.

python generate_sample_csv.py


Run the main forecaster:
This will read the new CSV and generate the plots.

python demand_forecaster.py
