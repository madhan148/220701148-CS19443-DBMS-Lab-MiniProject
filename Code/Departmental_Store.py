import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime

conn = sqlite3.connect('departmental_store.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS DepartmentalStore (
                StoreID TEXT PRIMARY KEY,
                StoreName TEXT NOT NULL,
                Location TEXT NOT NULL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS Employee (
                EmployeeID TEXT PRIMARY KEY,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                Role TEXT NOT NULL,
                Salary REAL NOT NULL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS Customer (
                CustomerID TEXT PRIMARY KEY,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                Email TEXT NOT NULL,
                Phone TEXT NOT NULL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS Sales (
                SaleID TEXT PRIMARY KEY,
                Date TEXT NOT NULL,
                TotalPrice REAL NOT NULL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS Supplier (
                SupplierID TEXT PRIMARY KEY,
                SupplierName TEXT NOT NULL,
                ContactInfo TEXT NOT NULL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS Product (
                ProductID TEXT PRIMARY KEY,
                ProductName TEXT NOT NULL,
                Description TEXT NOT NULL,
                Price REAL NOT NULL,
                StockQuantity INTEGER NOT NULL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS Category (
                CategoryID TEXT PRIMARY KEY,
                CategoryName TEXT NOT NULL
            )''')

conn.commit()

def add_store():
    store_id = entry_store_id.get()
    store_name = entry_store_name.get()
    location = entry_store_location.get()
    c.execute('INSERT INTO DepartmentalStore (StoreID, StoreName, Location) VALUES (?, ?, ?)', 
              (store_id, store_name, location))
    conn.commit()
    messagebox.showinfo("Success", "Store added successfully.")
    entry_store_id.delete(0, END)
    entry_store_name.delete(0, END)
    entry_store_location.delete(0, END)

def view_stores():
    for row in tree_stores.get_children():
        tree_stores.delete(row)
    c.execute('SELECT * FROM DepartmentalStore')
    stores = c.fetchall()
    for store in stores:
        tree_stores.insert("", "end", values=store)

def add_employee():
    emp_id = entry_emp_id.get()
    first_name = entry_emp_first_name.get()
    last_name = entry_emp_last_name.get()
    role = entry_emp_role.get()
    salary = float(entry_emp_salary.get())
    c.execute('INSERT INTO Employee (EmployeeID, FirstName, LastName, Role, Salary) VALUES (?, ?, ?, ?, ?)', 
              (emp_id, first_name, last_name, role, salary))
    conn.commit()
    messagebox.showinfo("Success", "Employee added successfully.")
    entry_emp_id.delete(0, END)
    entry_emp_first_name.delete(0, END)
    entry_emp_last_name.delete(0, END)
    entry_emp_role.delete(0, END)
    entry_emp_salary.delete(0, END)

def view_employees():
    for row in tree_employees.get_children():
        tree_employees.delete(row)
    c.execute('SELECT * FROM Employee')
    employees = c.fetchall()
    for emp in employees:
        tree_employees.insert("", "end", values=emp)

def add_customer():
    cust_id = entry_cust_id.get()
    first_name = entry_cust_first_name.get()
    last_name = entry_cust_last_name.get()
    email = entry_cust_email.get()
    phone = entry_cust_phone.get()
    c.execute('INSERT INTO Customer (CustomerID, FirstName, LastName, Email, Phone) VALUES (?, ?, ?, ?, ?)', 
              (cust_id, first_name, last_name, email, phone))
    conn.commit()
    messagebox.showinfo("Success", "Customer added successfully.")
    entry_cust_id.delete(0, END)
    entry_cust_first_name.delete(0, END)
    entry_cust_last_name.delete(0, END)
    entry_cust_email.delete(0, END)
    entry_cust_phone.delete(0, END)

def view_customers():
    for row in tree_customers.get_children():
        tree_customers.delete(row)
    c.execute('SELECT * FROM Customer')
    customers = c.fetchall()
    for cust in customers:
        tree_customers.insert("", "end", values=cust)

def add_sale():
    sale_id = entry_sale_id.get()
    date = entry_sale_date.get()
    total_price = float(entry_sale_total_price.get())
    c.execute('INSERT INTO Sales (SaleID, Date, TotalPrice) VALUES (?, ?, ?)', 
              (sale_id, date, total_price))
    conn.commit()
    messagebox.showinfo("Success", "Sale recorded successfully.")
    entry_sale_id.delete(0, END)
    entry_sale_date.delete(0, END)
    entry_sale_total_price.delete(0, END)

def view_sales():
    for row in tree_sales.get_children():
        tree_sales.delete(row)
    c.execute('SELECT * FROM Sales')
    sales = c.fetchall()
    for sale in sales:
        tree_sales.insert("", "end", values=sale)

def add_supplier():
    supplier_id = entry_supplier_id.get()
    supplier_name = entry_supplier_name.get()
    contact_info = entry_supplier_contact_info.get()
    c.execute('INSERT INTO Supplier (SupplierID, SupplierName, ContactInfo) VALUES (?, ?, ?)', 
              (supplier_id, supplier_name, contact_info))
    conn.commit()
    messagebox.showinfo("Success", "Supplier added successfully.")
    entry_supplier_id.delete(0, END)
    entry_supplier_name.delete(0, END)
    entry_supplier_contact_info.delete(0, END)

def view_suppliers():
    for row in tree_suppliers.get_children():
        tree_suppliers.delete(row)
    c.execute('SELECT * FROM Supplier')
    suppliers = c.fetchall()
    for supplier in suppliers:
        tree_suppliers.insert("", "end", values=supplier)

def add_product():
    product_id = entry_product_id.get()
    product_name = entry_product_name.get()
    description = entry_product_description.get()
    price = float(entry_product_price.get())
    stock_quantity = int(entry_product_stock_quantity.get())
    c.execute('INSERT INTO Product (ProductID, ProductName, Description, Price, StockQuantity) VALUES (?, ?, ?, ?, ?)', 
              (product_id, product_name, description, price, stock_quantity))
    conn.commit()
    messagebox.showinfo("Success", "Product added successfully.")
    entry_product_id.delete(0, END)
    entry_product_name.delete(0, END)
    entry_product_description.delete(0, END)
    entry_product_price.delete(0, END)
    entry_product_stock_quantity.delete(0, END)

def view_products():
    for row in tree_products.get_children():
        tree_products.delete(row)
    c.execute('SELECT * FROM Product')
    products = c.fetchall()
    for product in products:
        tree_products.insert("", "end", values=product)

def add_category():
    category_id = entry_category_id.get()
    category_name = entry_category_name.get()
    c.execute('INSERT INTO Category (CategoryID, CategoryName) VALUES (?, ?)', 
              (category_id, category_name))
    conn.commit()
    messagebox.showinfo("Success", "Category added successfully.")
    entry_category_id.delete(0, END)
    entry_category_name.delete(0, END)

def view_categories():
    for row in tree_categories.get_children():
        tree_categories.delete(row)
    c.execute('SELECT * FROM Category')
    categories = c.fetchall()
    for category in categories:
        tree_categories.insert("", "end", values=category)

root = Tk()
root.title("Departmental Store Management System")

tabControl = ttk.Notebook(root)
tab_stores = ttk.Frame(tabControl)
tab_employees = ttk.Frame(tabControl)
tab_customers = ttk.Frame(tabControl)
tab_sales = ttk.Frame(tabControl)
tab_suppliers = ttk.Frame(tabControl)
tab_products = ttk.Frame(tabControl)
tab_categories = ttk.Frame(tabControl)

tabControl.add(tab_stores, text='Stores')
tabControl.add(tab_employees, text='Employees')
tabControl.add(tab_customers, text='Customers')
tabControl.add(tab_sales, text='Sales')
tabControl.add(tab_suppliers, text='Suppliers')
tabControl.add(tab_products, text='Products')
tabControl.add(tab_categories, text='Categories')

tabControl.pack(expand=1, fill="both")

frame_store_form = Frame(tab_stores)
frame_store_form.pack(side=TOP, fill=X, pady=10, padx=10)

Label(frame_store_form, text="Store ID").grid(row=0, column=0, padx=5, pady=5)
entry_store_id = Entry(frame_store_form)
entry_store_id.grid(row=0, column=1, padx=5, pady=5)

Label(frame_store_form, text="Store Name").grid(row=1, column=0, padx=5, pady=5)
entry_store_name = Entry(frame_store_form)
entry_store_name.grid(row=1, column=1, padx=5, pady=5)

Label(frame_store_form, text="Location").grid(row=2, column=0, padx=5, pady=5)
entry_store_location = Entry(frame_store_form)
entry_store_location.grid(row=2, column=1, padx=5, pady=5)

Button(frame_store_form, text="Add Store", command=add_store).grid(row=3, column=1, pady=10)

frame_store_tree = Frame(tab_stores)
frame_store_tree.pack(side=TOP, fill=BOTH, expand=True)

tree_stores = ttk.Treeview(frame_store_tree, columns=("StoreID", "StoreName", "Location"), show='headings')
tree_stores.heading("StoreID", text="Store ID")
tree_stores.heading("StoreName", text="Store Name")
tree_stores.heading("Location", text="Location")
tree_stores.pack(fill=BOTH, expand=True)

Button(frame_store_tree, text="View Stores", command=view_stores).pack(side=LEFT, padx=5, pady=5)

frame_emp_form = Frame(tab_employees)
frame_emp_form.pack(side=TOP, fill=X, pady=10, padx=10)

Label(frame_emp_form, text="Employee ID").grid(row=0, column=0, padx=5, pady=5)
entry_emp_id = Entry(frame_emp_form)
entry_emp_id.grid(row=0, column=1, padx=5, pady=5)

Label(frame_emp_form, text="First Name").grid(row=1, column=0, padx=5, pady=5)
entry_emp_first_name = Entry(frame_emp_form)
entry_emp_first_name.grid(row=1, column=1, padx=5, pady=5)

Label(frame_emp_form, text="Last Name").grid(row=2, column=0, padx=5, pady=5)
entry_emp_last_name = Entry(frame_emp_form)
entry_emp_last_name.grid(row=2, column=1, padx=5, pady=5)

Label(frame_emp_form, text="Role").grid(row=3, column=0, padx=5, pady=5)
entry_emp_role = Entry(frame_emp_form)
entry_emp_role.grid(row=3, column=1, padx=5, pady=5)

Label(frame_emp_form, text="Salary").grid(row=4, column=0, padx=5, pady=5)
entry_emp_salary = Entry(frame_emp_form)
entry_emp_salary.grid(row=4, column=1, padx=5, pady=5)

Button(frame_emp_form, text="Add Employee", command=add_employee).grid(row=5, column=1, pady=10)

frame_emp_tree = Frame(tab_employees)
frame_emp_tree.pack(side=TOP, fill=BOTH, expand=True)

tree_employees = ttk.Treeview(frame_emp_tree, columns=("EmployeeID", "FirstName", "LastName", "Role", "Salary"), show='headings')
tree_employees.heading("EmployeeID", text="Employee ID")
tree_employees.heading("FirstName", text="First Name")
tree_employees.heading("LastName", text="Last Name")
tree_employees.heading("Role", text="Role")
tree_employees.heading("Salary", text="Salary")
tree_employees.pack(fill=BOTH, expand=True)

Button(frame_emp_tree, text="View Employees", command=view_employees).pack(side=LEFT, padx=5, pady=5)

frame_cust_form = Frame(tab_customers)
frame_cust_form.pack(side=TOP, fill=X, pady=10, padx=10)

Label(frame_cust_form, text="Customer ID").grid(row=0, column=0, padx=5, pady=5)
entry_cust_id = Entry(frame_cust_form)
entry_cust_id.grid(row=0, column=1, padx=5, pady=5)

Label(frame_cust_form, text="First Name").grid(row=1, column=0, padx=5, pady=5)
entry_cust_first_name = Entry(frame_cust_form)
entry_cust_first_name.grid(row=1, column=1, padx=5, pady=5)

Label(frame_cust_form, text="Last Name").grid(row=2, column=0, padx=5, pady=5)
entry_cust_last_name = Entry(frame_cust_form)
entry_cust_last_name.grid(row=2, column=1, padx=5, pady=5)

Label(frame_cust_form, text="Email").grid(row=3, column=0, padx=5, pady=5)
entry_cust_email = Entry(frame_cust_form)
entry_cust_email.grid(row=3, column=1, padx=5, pady=5)

Label(frame_cust_form, text="Phone").grid(row=4, column=0, padx=5, pady=5)
entry_cust_phone = Entry(frame_cust_form)
entry_cust_phone.grid(row=4, column=1, padx=5, pady=5)

Button(frame_cust_form, text="Add Customer", command=add_customer).grid(row=5, column=1, pady=10)

frame_cust_tree = Frame(tab_customers)
frame_cust_tree.pack(side=TOP, fill=BOTH, expand=True)

tree_customers = ttk.Treeview(frame_cust_tree, columns=("CustomerID", "FirstName", "LastName", "Email", "Phone"), show='headings')
tree_customers.heading("CustomerID", text="Customer ID")
tree_customers.heading("FirstName", text="First Name")
tree_customers.heading("LastName", text="Last Name")
tree_customers.heading("Email", text="Email")
tree_customers.heading("Phone", text="Phone")
tree_customers.pack(fill=BOTH, expand=True)

Button(frame_cust_tree, text="View Customers", command=view_customers).pack(side=LEFT, padx=5, pady=5)

frame_sale_form = Frame(tab_sales)
frame_sale_form.pack(side=TOP, fill=X, pady=10, padx=10)

Label(frame_sale_form, text="Sale ID").grid(row=0, column=0, padx=5, pady=5)
entry_sale_id = Entry(frame_sale_form)
entry_sale_id.grid(row=0, column=1, padx=5, pady=5)

Label(frame_sale_form, text="Date").grid(row=1, column=0, padx=5, pady=5)
entry_sale_date = Entry(frame_sale_form)
entry_sale_date.grid(row=1, column=1, padx=5, pady=5)

Label(frame_sale_form, text="Total Price").grid(row=2, column=0, padx=5, pady=5)
entry_sale_total_price = Entry(frame_sale_form)
entry_sale_total_price.grid(row=2, column=1, padx=5, pady=5)

Button(frame_sale_form, text="Add Sale", command=add_sale).grid(row=3, column=1, pady=10)

frame_sale_tree = Frame(tab_sales)
frame_sale_tree.pack(side=TOP, fill=BOTH, expand=True)

tree_sales = ttk.Treeview(frame_sale_tree, columns=("SaleID", "Date", "TotalPrice"), show='headings')
tree_sales.heading("SaleID", text="Sale ID")
tree_sales.heading("Date", text="Date")
tree_sales.heading("TotalPrice", text="Total Price")
tree_sales.pack(fill=BOTH, expand=True)

Button(frame_sale_tree, text="View Sales", command=view_sales).pack(side=LEFT, padx=5, pady=5)

frame_supplier_form = Frame(tab_suppliers)
frame_supplier_form.pack(side=TOP, fill=X, pady=10, padx=10)

Label(frame_supplier_form, text="Supplier ID").grid(row=0, column=0, padx=5, pady=5)
entry_supplier_id = Entry(frame_supplier_form)
entry_supplier_id.grid(row=0, column=1, padx=5, pady=5)

Label(frame_supplier_form, text="Supplier Name").grid(row=1, column=0, padx=5, pady=5)
entry_supplier_name = Entry(frame_supplier_form)
entry_supplier_name.grid(row=1, column=1, padx=5, pady=5)

Label(frame_supplier_form, text="Contact Info").grid(row=2, column=0, padx=5, pady=5)
entry_supplier_contact_info = Entry(frame_supplier_form)
entry_supplier_contact_info.grid(row=2, column=1, padx=5, pady=5)

Button(frame_supplier_form, text="Add Supplier", command=add_supplier).grid(row=3, column=1, pady=10)

frame_supplier_tree = Frame(tab_suppliers)
frame_supplier_tree.pack(side=TOP, fill=BOTH, expand=True)

tree_suppliers = ttk.Treeview(frame_supplier_tree, columns=("SupplierID", "SupplierName", "ContactInfo"), show='headings')
tree_suppliers.heading("SupplierID", text="Supplier ID")
tree_suppliers.heading("SupplierName", text="Supplier Name")
tree_suppliers.heading("ContactInfo", text="Contact Info")
tree_suppliers.pack(fill=BOTH, expand=True)

Button(frame_supplier_tree, text="View Suppliers", command=view_suppliers).pack(side=LEFT, padx=5, pady=5)

frame_product_form = Frame(tab_products)
frame_product_form.pack(side=TOP, fill=X, pady=10, padx=10)

Label(frame_product_form, text="Product ID").grid(row=0, column=0, padx=5, pady=5)
entry_product_id = Entry(frame_product_form)
entry_product_id.grid(row=0, column=1, padx=5, pady=5)

Label(frame_product_form, text="Product Name").grid(row=1, column=0, padx=5, pady=5)
entry_product_name = Entry(frame_product_form)
entry_product_name.grid(row=1, column=1, padx=5, pady=5)

Label(frame_product_form, text="Description").grid(row=2, column=0, padx=5, pady=5)
entry_product_description = Entry(frame_product_form)
entry_product_description.grid(row=2, column=1, padx=5, pady=5)

Label(frame_product_form, text="Price").grid(row=3, column=0, padx=5, pady=5)
entry_product_price = Entry(frame_product_form)
entry_product_price.grid(row=3, column=1, padx=5, pady=5)

Label(frame_product_form, text="Stock Quantity").grid(row=4, column=0, padx=5, pady=5)
entry_product_stock_quantity = Entry(frame_product_form)
entry_product_stock_quantity.grid(row=4, column=1, padx=5, pady=5)

Button(frame_product_form, text="Add Product", command=add_product).grid(row=5, column=1, pady=10)

frame_product_tree = Frame(tab_products)
frame_product_tree.pack(side=TOP, fill=BOTH, expand=True)

tree_products = ttk.Treeview(frame_product_tree, columns=("ProductID", "ProductName", "Description", "Price", "StockQuantity"), show='headings')
tree_products.heading("ProductID", text="Product ID")
tree_products.heading("ProductName", text="Product Name")
tree_products.heading("Description", text="Description")
tree_products.heading("Price", text="Price")
tree_products.heading("StockQuantity", text="Stock Quantity")
tree_products.pack(fill=BOTH, expand=True)

Button(frame_product_tree, text="View Products", command=view_products).pack(side=LEFT, padx=5, pady=5)

frame_category_form = Frame(tab_categories)
frame_category_form.pack(side=TOP, fill=X, pady=10, padx=10)

Label(frame_category_form, text="Category ID").grid(row=0, column=0, padx=5, pady=5)
entry_category_id = Entry(frame_category_form)
entry_category_id.grid(row=0, column=1, padx=5, pady=5)

Label(frame_category_form, text="Category Name").grid(row=1, column=0, padx=5, pady=5)
entry_category_name = Entry(frame_category_form)
entry_category_name.grid(row=1, column=1, padx=5, pady=5)

Button(frame_category_form, text="Add Category", command=add_category).grid(row=2, column=1, pady=10)

frame_category_tree = Frame(tab_categories)
frame_category_tree.pack(side=TOP, fill=BOTH, expand=True)

tree_categories = ttk.Treeview(frame_category_tree, columns=("CategoryID", "CategoryName"), show='headings')
tree_categories.heading("CategoryID", text="Category ID")
tree_categories.heading("CategoryName", text="Category Name")
tree_categories.pack(fill=BOTH, expand=True)

Button(frame_category_tree, text="View Categories", command=view_categories).pack(side=LEFT, padx=5, pady=5)

root.mainloop()

conn.close()
