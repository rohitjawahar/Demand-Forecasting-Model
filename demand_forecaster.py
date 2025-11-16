import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import numpy as np

# --- This is the new, specific filename ---
DATA_FILENAME = 'phone_repair_shop_data.csv'

# This is the fake data generator from before.
# We'll use it as a fallback.
def create_fake_demo_data():
    """
    Generates a 2-year fake repair dataset to simulate
    a real-world scenario if no file is found.
    """
    print("Generating 2 years of fake demo data...")
    
    dates = pd.date_range(start='2022-01-01', periods=730, freq='D')
    # Phone repair shop has fewer "sales" than a retail store
    base_repairs = 10
    time = np.arange(730)
    
    # Slight upward trend as the shop gets more popular
    trend = 0.02 * time
    
    # More repairs on weekends/Mondays
    weekly_seasonality = 3 * np.sin(2 * np.pi * (time % 7) / 7)
    
    # BIG spike in Jan/Feb (post-holiday drops) and a dip in summer
    yearly_seasonality = 10 * np.sin(2 * np.pi * (time % 365.25) / 365.25 - np.pi/2) 
    
    noise = np.random.normal(0, 2, 730)
    
    repairs = base_repairs + trend + weekly_seasonality + yearly_seasonality + noise
    # Ensure no negative repairs
    repairs = np.maximum(repairs, 0).astype(int)
    
    df = pd.DataFrame({'ds': dates, 'y': repairs})
    print("Fake data generation complete.")
    return df

def run_forecaster(data):
    """
    Trains the Prophet model and generates forecast plots.
    """
    print("Initializing Prophet model...")
    # Add a specific seasonality for the post-holiday spike
    model = Prophet(daily_seasonality=False, weekly_seasonality=True, yearly_seasonality=True)
    
    print("Training (fitting) model on historical data...")
    model.fit(data)
    
    print("Creating future dataframe for 6 months (180 days)...")
    future_dataframe = model.make_future_dataframe(periods=180)
    
    print("Making predictions...")
    forecast = model.predict(future_dataframe)
    
    # --- Visualization ---
    print("Generating Plot 1: The Main Forecast...")
    fig1 = model.plot(forecast)
    plt.title('AI Forecast vs. Actual Repairs (Next 6 Months)')
    plt.xlabel('Date')
    plt.ylabel('Predicted Repairs')
    
    print("Generating Plot 2: Forecast Components...")
    fig2 = model.plot_components(forecast)
    
    print("Displaying plots. Close the plot windows to exit.")
    plt.show()

# --- Main execution (This is the new "smarter" part) ---
if __name__ == "__main__":
    
    sales_df = None

    print(f"--- Checking for real data file: '{DATA_FILENAME}' ---")
    
    try:
        # 1. Try to load real data from the CSV
        real_data = pd.read_csv(DATA_FILENAME)
        
        # 2. Check if it has the required 'ds' and 'y' columns
        if 'ds' in real_data.columns and 'y' in real_data.columns:
            print("Success! Found real data. Using it for the forecast.")
            sales_df = real_data
            
            # IMPORTANT: Convert the 'ds' column to datetime objects
            sales_df['ds'] = pd.to_datetime(sales_df['ds'])
            
        else:
            print(f"Found '{DATA_FILENAME}', but it's missing 'ds' or 'y' columns.")
            print("Please check the column names in your file.")

    except FileNotFoundError:
        # This is not an error, it's just a fallback.
        print(f"'{DATA_FILENAME}' not found.")
        
    except Exception as e:
        # Catch other potential errors
        print(f"An error occurred while loading real data: {e}")

    # 3. If loading real data failed, use fake data.
    if sales_df is None:
        print("--- Falling back to fake demo data. ---")
        sales_df = create_fake_demo_data()
    
    # 4. Run the forecast on whichever data we ended up with.
    print("--- Running the forecaster... ---")
    run_forecaster(sales_df)