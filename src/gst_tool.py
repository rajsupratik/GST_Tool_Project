import pandas as pd

def calculate_gst(data, rate_column, amount_column):
    """
    Calculate GST for the given dataset.
    """
    data['GST'] = data[amount_column] * data[rate_column] / 100
    return data

def reconcile_gst(sales_gst, purchase_gst):
    """
    Reconcile GST paid (sales) with GST claimed (purchases).
    """
    net_gst = sales_gst - purchase_gst
    return net_gst

def generate_report(data, output_path):
    """
    Generate an Excel report from the given data.
    """
    data.to_excel(output_path, index=False, engine='openpyxl')
    print(f"Report saved to {output_path}")
