import pandas as pd
import numpy as np

# --- This is the new, specific filename ---
FILENAME_TO_SAVE = 'phone_repair_shop_data.csv'

def create_and_save_fake_data():
    """
    Generates a 2-year fake repair dataset and saves it
    to 'phone_repair_shop_data.csv' to simulate a real business.
    """
    print(f"Generating 2 years of fake 'Phone Repair Shop' data...")
    
    dates = pd.date_range(start='2022-01-01', periods=730, freq='D')
    
    # Base repairs per day
    base_repairs = 10
    time = np.arange(730)
    
    # Slight upward trend as the shop gets more popular
    trend = 0.02 * time
    
    # More repairs on weekends/Mondays
    weekly_seasonality = 3 * np.sin(2 * np.pi * (time % 7) / 7)
    
    # BIG spike in Jan/Feb (post-holiday drops) and a dip in summer
    yearly_seasonality = 10 * np.sin(2 * np.pi * (time % 365.25) / 365.25 - np.pi/2) 
    
    # Random noise to make it look real
    noise = np.random.normal(0, 2, 730)
    
    # Combine all parts
    repairs = base_repairs + trend + weekly_seasonality + yearly_seasonality + noise
    # Ensure no negative repairs
    repairs = np.maximum(repairs, 0).astype(int)
    
    # We must have columns named 'ds' (datestamp) and 'y' (value)
    df = pd.DataFrame({'ds': dates, 'y': repairs})
    
    try:
        # Save the data to the new CSV file name
        df.to_csv(FILENAME_TO_SAVE, index=False)
        print(f"Success! Saved fake data to '{FILENAME_TO_SAVE}'")
        print("You can now run 'python demand_forecaster.py' to use this file.")
        
    except Exception as e:
        print(f"Error saving file: {e}")
        print("Please check folder permissions.")

if __name__ == "__main__":
    create_and_save_fake_data()