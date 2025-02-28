import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def load_ev_data(file_path, sheet_name=1):
    """Loading EV sales data from an Excel file."""
    df = pd.read_excel(file_path, sheet_name='Data', usecols="B:F", skiprows=4, nrows=6)
    
    column_names = pd.read_excel(file_path, sheet_name='Data', usecols="B:F", skiprows=3, nrows=1).values.flatten()
    df.columns = column_names 

    df['Year'] = df['Year'].astype(int)

    df.iloc[:, 1:] = df.iloc[:, 1:].replace(',', '.', regex=True).astype(float)

    return df  

def bass_model(t, p, q, M):
    """Bass Model function."""
    adoption = (p + q) ** 2 * np.exp(-(p + q) * t) / (p * (1 + (q / p) * np.exp(-(p + q) * t)) ** 2)
    return M * adoption

def fit_bass_model(years, sales):
    base_year = years.min() 
    years_numeric = np.array([y - base_year for y in years]) 

    p0 = [0.05, 0.3, max(sales) * 3]  
    bounds = ([0.001, 0.001, max(sales)], [1, 1, max(sales) * 10])  

    params, _ = curve_fit(bass_model, years_numeric, sales, p0=p0, bounds=bounds, maxfev=10000)

    return params, base_year

def predict_future_sales(params, base_year, end_year=2026):
    """Predict future sales using the Bass Model."""
    p_est, q_est, M_est = params
    future_years = np.arange(base_year, end_year + 1)  
    future_years_numeric = future_years - base_year  

    future_sales = bass_model(future_years_numeric, p_est, q_est, M_est)
    return future_years, future_sales

def plot_bass_model(years, sales, fitted_sales, future_years, future_sales):
    """Plot actual sales vs. Bass Model fitted values and future predictions."""
    plt.figure(figsize=(10, 5))

    plt.plot(years, sales, 'bo-', label="Actual Sales")  
    plt.plot(years, fitted_sales, 'go-', label="Bass Model Fitted Sales")  
    plt.plot(future_years, future_sales, 'r--', label="Predicted Sales (Future)")  

    plt.xlabel("Year")
    plt.ylabel("Sales")
    plt.title("Bass Model Fitting for Hero MotoCorp Surge S32 (Three-Wheeler)")
    
    all_years = np.concatenate([years, future_years])
    plt.xticks(all_years, rotation=45)  
    plt.gca().set_xticks(all_years) 

    plt.legend()
    plt.grid()
    plt.show()
