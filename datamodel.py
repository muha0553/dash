# Import
import pandas as pd
import numpy as np


############################## Data import #####################
#githubpath = 'https://github.com/muha0553/dash/tree/main/data/'
githubpath = './data/'

# Import from Excel file, 4 different sheets
df_customers = pd.read_excel(githubpath + "my_shop_data.xlsx", sheet_name="customers")
df_order = pd.read_excel(githubpath + "my_shop_data.xlsx", sheet_name="order")
df_employee = pd.read_excel(githubpath + "my_shop_data.xlsx", sheet_name="employee")
df_products = pd.read_excel(githubpath + "my_shop_data.xlsx", sheet_name="products")

def get_data():
    # Employee name
    df_employee['emp_name'] = df_employee['firstname'] + ' ' + df_employee['lastname']
    df_order['total'] = df_order['unitprice'] * df_order['quantity']
    order = pd.merge(df_order, df_products, on='product_id')
    order = pd.merge(order, df_employee, on='employee_id')
    order = pd.merge(order, df_customers, on='customer_id')

    # Order - Select colomns
    order = order[['order_id', 
                'product_id', 'productname', 'type',
                'customer_id', 'cust_name',
                'employee_id', 'emp_name', 
                'total']]


    return order
