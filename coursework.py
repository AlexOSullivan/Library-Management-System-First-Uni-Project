from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import *
import unittest
import sqlite3
import time
from PIL import Image, ImageTk


#Here are my classes for this feature

class Administrator:
    #The administrator is the user and uses __init__ so that usernames and passwords can be assigned
    #to variables that will be used in the login function
    def __init__(self, usernames, passwords):
        self.usernames = usernames
        self.passwords = passwords


#These are the usernames and password for each employee of AAT, calling the administrator class
A1 = Administrator("administrator", "aat")
A2 = Administrator("administrator2", "aat2")
A3 = Administrator("administrator3", "aat3")
A4 = Administrator("administrator4", "aat4")


class MainPage:
    def __init__(self, master):
        start_frame = Frame(master)
        start_frame.pack()


#---------------------------------------------------
#These are simple frame swapping function that are activated via a button
def category_add_button():
    category_add_frame.pack()
    category_frame.forget()


def category_edit_button():
    category_edit_frame.pack()
    category_frame.forget()


def category_delete_button():
    category_delete_frame.pack()
    category_frame.forget()


def category_return_button():
    second_frame.pack()
    category_frame.forget()


def category_add_return_button():
    category_frame.pack()
    category_add_frame.forget()


def category_edit_return_button():
    category_frame.pack()
    category_edit_frame.forget()


def category_delete_return_button():
    category_frame.pack()
    category_delete_frame.forget()


def product_return_button():
    second_frame.pack()
    product_frame.forget()


def product_add_button():
    product_add_frame.pack()
    product_frame.forget()


def product_edit_button():
    product_edit_frame.pack()
    product_frame.forget()


def product_delete_button():
    product_delete_frame.pack()
    product_frame.forget()


def product_add_return_button():
    product_frame.pack()
    product_add_frame.forget()


def product_edit_return_button():
    product_frame.pack()
    product_edit_frame.forget()


def product_delete_return_button():
    product_frame.pack()
    product_delete_frame.forget()


def stock_return_button():
    second_frame.pack()
    stock_frame.forget()


def stock_return():
    stock_frame.pack()
    low_stock_frame.forget()


def response_to_button1():
    category_frame.pack()
    second_frame.forget()
    tk.Label(category_frame, text='Select Function', font=font1).grid(column=3, row=0, columnspan=1)


def response_to_button2():
    product_frame.pack()
    second_frame.forget()
    tk.Label(product_frame, text='Select Function', font=font1).grid(column=3, row=0, columnspan=1)


def response_to_button3():
    stock_frame.pack()
    second_frame.forget()
    tk.Label(stock_frame, text='Stock Taking', font=font1).grid(column=0, row=0)


#---------------------------------------
#These are the most important functions in the code
def login_id():
    #process for employee to enter their username
    #The If statement is for when the user enters the correct credentials
    if entry1.get() == A1.usernames and entry2.get() == A1.passwords or entry1.get() == A2.usernames and entry2.get()\
     == A2.passwords or entry1.get() == A3.usernames and entry2.get() == A3.passwords or entry1.get() == A4.usernames\
     and entry2.get() == A4.passwords:
        second_frame.pack()
        start_frame.forget()
        successful_message = "Welcome back"
        heading2 = tk.Label(second_frame, text=successful_message, font=font2)
        heading2.grid(column=3, row=0, columnspan=1)
        assert successful_message == "Welcome back"
    #The else statement is for when the user enters the wrong credentials
    else:
        unsuccessful_message = "Login Unsuccessful Please Try Again!"
        assert unsuccessful_message == "Login Unsuccessful Please Try Again!"
        unsuccessful_label = Label(start_frame, text=unsuccessful_message)
        unsuccessful_label.grid(column=3, row=0, columnspan=1, rowspan=3)


def view_data():
    #This is for obtaining information from the database and inserting into listbox, this is category info
    cursor.execute("SELECT * FROM ProductCategory")
    row = cursor.fetchall()
    return row


def view_data2():
    #This is the same as view data but with product info
    cursor.execute("SELECT * FROM ProductInfo")
    row2 = cursor.fetchall()
    return row2


def view_stock():
    #Also similar to the two above but for stock taking
    cursor.execute("SELECT ProductID, ProductName, ProductQuantity FROM ProductInfo where ProductQuantity <= 20")
    row3 = cursor.fetchall()
    return row3


def add_category():
    #This function is to add the user entered info into the database and display it in listbox
    if category_add_entry1.get() == "":
        tk.Label(category_add_frame, text="Need All Details").grid(column=2, row=6)
    elif category_add_entry2.get() == "":
        tk.Label(category_add_frame, text="Need All Details").grid(column=2, row=6)
    elif category_add_entry3.get() == "":
        tk.Label(category_add_frame, text="Need All Details").grid(column=2, row=6)
    elif category_add_entry4.get() == "":
        tk.Label(category_add_frame, text="Need All Details").grid(column=2, row=6)
    else:
        category_number = category_add_entry1.get()
        category_name = category_add_entry2.get()
        age_category = category_add_entry3.get()
        location_warehouse = category_add_entry4.get()
        cursor.execute(
            """INSERT into ProductCategory VALUES (:CategoryNumber, :CategoryName, :ProductAgeCategory,
             :LocationInWarehouse)""",
            {'CategoryNumber': category_number,
             'CategoryName': category_name,
             'ProductAgeCategory': age_category,
             'LocationInWarehouse': location_warehouse})
        category_add_entry1.delete(0, END)
        category_add_entry2.delete(0, END)
        category_add_entry3.delete(0, END)
        category_add_entry4.delete(0, END)
        add_listbox.delete(0, END)
        edit_listbox.delete(0, END)
        delete_page_listbox.delete(0, END)
        #This is making use of the view data function, your see this a lot
        for row in view_data():
            add_listbox.insert(END, row, str(""))
            edit_listbox.insert(END, row, str(""))
            delete_page_listbox.insert(END, row, str(""))
            con.commit()


def edit_category():
    #This function is to edit the category info and display in listbox
    if category_edit_entry3.get() == "CategoryName":
        cursor.execute("""UPDATE ProductCategory SET
         CategoryName = ? WHERE CategoryName = ? """, (category_edit_entry.get(), category_edit_entry2.get()))
        con.commit()
        edit_listbox.delete(0, END)
        for row in view_data():
            edit_listbox.insert(END, row, str(""))
    elif category_edit_entry3.get() == "CategoryNumber":
        cursor.execute("""UPDATE ProductCategory SET
         CategoryNumber = ? WHERE CategoryNumber = ? """, (category_edit_entry.get(), category_edit_entry2.get()))
        con.commit()
        edit_listbox.delete(0, END)
        for row in view_data():
            edit_listbox.insert(END, row, str(""))
    elif category_edit_entry3.get() == "AgeCategory":
        cursor.execute("""UPDATE ProductCategory SET
         ProductAgeCategory = ? WHERE
          ProductAgeCategory = ? """, (category_edit_entry.get(), category_edit_entry2.get()))
        con.commit()
        edit_listbox.delete(0, END)
        for row in view_data():
            edit_listbox.insert(END, row, str(""))
    elif category_edit_entry3.get() == "LocationInWarehouse":
        cursor.execute("""UPDATE ProductCategory SET
         LocationInWarehouse = ? WHERE
          LocationInWarehouse = ? """, (category_edit_entry.get(), category_edit_entry2.get()))
        con.commit()
        edit_listbox.delete(0, END)
        for row in view_data():
            edit_listbox.insert(END, row, str(""))
    else:
        edit_error = tk.Label(category_edit_frame, text="Unsuccessful attempt")
        edit_error.grid(column=2, row=5, columnspan=2)


def delete_category():
    #This is to delete a category that already exists
    result = "DELETE FROM ProductCategory WHERE CategoryName = ? "
    entry = [category_delete_entry.get()]
    cursor.execute(result, entry)
    con.commit()
    delete_page_listbox.delete(0, END)
    for row in view_data():
        delete_page_listbox.insert(END, row, str(""))


def add_product():
    #This function shares the same purpose as add category but is for the products
    if product_add_entry1.get() == "":
        tk.Label(product_add_frame, text="Need All Details").grid(column=2, row=10)
    elif product_add_entry2.get() == "":
        tk.Label(product_add_frame, text="Need All Details").grid(column=2, row=10)
    elif product_add_entry3.get() == "":
        tk.Label(product_add_frame, text="Need All Details").grid(column=2, row=10)
    elif product_add_entry4.get() == "":
        tk.Label(product_add_frame, text="Need All Details").grid(column=2, row=10)
    elif product_add_entry5.get() == "":
        tk.Label(product_add_frame, text="Need All Details").grid(column=2, row=10)
    elif product_add_entry6.get() == "":
        tk.Label(product_add_frame, text="Need All Details").grid(column=2, row=10)
    elif product_add_entry7.get() == "":
        tk.Label(product_add_frame, text="Need All Details").grid(column=2, row=10)
    elif product_add_entry8.get() == "":
        tk.Label(product_add_frame, text="Need All Details").grid(column=2, row=10)
    else:
        cursor.execute("""INSERT into ProductInfo VALUES (:CategoryNumber, :ProductID, :ProductName, :ProductImage,\
         :ProductDescription, :ProductAgeCategory, :ProductPrice, :ProductQuantity)""",
                       {'CategoryNumber': product_add_entry1.get(),
                        'ProductID': product_add_entry2.get(),
                        'ProductName': product_add_entry3.get(),
                        'ProductImage': product_add_entry4.get(),
                        'ProductDescription': product_add_entry5.get(),
                        'ProductAgeCategory': product_add_entry6.get(),
                        'ProductPrice': product_add_entry7.get(),
                        'ProductQuantity': product_add_entry8.get()})
    product_add_entry1.delete(0, END)
    product_add_entry2.delete(0, END)
    product_add_entry3.delete(0, END)
    product_add_entry4.delete(0, END)
    product_add_entry5.delete(0, END)
    product_add_entry6.delete(0, END)
    product_add_entry7.delete(0, END)
    product_add_entry8.delete(0, END)
    product_add_listbox.delete(0, END)
    for row2 in view_data2():
        product_add_listbox.insert(END, row2, str(""))
        con.commit()


def edit_product():
    #This is to edit products in the system with user inputs
    if product_edit_entry3.get() == "ProductID":
        cursor.execute("""UPDATE ProductInfo SET
         ProductID = ? WHERE ProductID = ? """, (product_edit_entry.get(), product_edit_entry2.get()))
        con.commit()
        product_edit_listbox.delete(0, END)
        for row2 in view_data2():
            product_edit_listbox.insert(END, row2, str(""))
    elif product_edit_entry3.get() == "CategoryNumber":
        cursor.execute("""UPDATE ProductInfo SET
         CategoryNumber = ? WHERE CategoryNumber = ? """, (product_edit_entry.get(), product_edit_entry2.get()))
        con.commit()
        product_edit_listbox.delete(0, END)
        for row2 in view_data2():
            product_edit_listbox.insert(END, row2, str(""))
    elif product_edit_entry3.get() == "Name":
        cursor.execute("""UPDATE ProductInfo SET
         Name = ? WHERE ProductName = ? """, (product_edit_entry.get(), product_edit_entry2.get()))
        con.commit()
        product_edit_listbox.delete(0, END)
        for row2 in view_data2():
            product_edit_listbox.insert(END, row2, str(""))
    elif product_edit_entry3.get() == "ProductImage":
        cursor.execute("""UPDATE ProductInfo SET
         ProductImage = ? WHERE ProductImage = ? """, (product_edit_entry.get(), product_edit_entry2.get()))
        con.commit()
        product_edit_listbox.delete(0, END)
        for row2 in view_data2():
            product_edit_listbox.insert(END, row2, str(""))
    elif product_edit_entry3.get() == "Description":
        cursor.execute("""UPDATE ProductInfo SET
         ProductDescription = ? WHERE ProductDescription = ? """, (product_edit_entry.get(), product_edit_entry2.get()))
        con.commit()
        product_edit_listbox.delete(0, END)
        for row2 in view_data2():
            product_edit_listbox.insert(END, row2, str(""))
    elif product_edit_entry3.get() == "ProductAgeCategory":
        cursor.execute("""UPDATE ProductInfo SET
         ProductAgeCategory = ? WHERE ProductAgeCategory = ? """, (product_edit_entry.get(), product_edit_entry2.get()))
        con.commit()
        product_edit_listbox.delete(0, END)
        for row2 in view_data2():
            product_edit_listbox.insert(END, row2, str(""))
    elif product_edit_entry3.get() == "ProductPrice":
        cursor.execute("""UPDATE ProductInfo SET
         ProductPrice = ? WHERE ProductPrice = ? """, (product_edit_entry.get(), product_edit_entry2.get()))
        con.commit()
        product_edit_listbox.delete(0, END)
        for row2 in view_data2():
            product_edit_listbox.insert(END, row2, str(""))
    elif product_edit_entry3.get() == "ProductQuantity":
        cursor.execute("""UPDATE ProductInfo SET
         ProductQuantity = ? WHERE ProductQuantity = ? """, (product_edit_entry.get(), product_edit_entry2.get()))
        con.commit()
        product_edit_listbox.delete(0, END)
        for row2 in view_data2():
            product_edit_listbox.insert(END, row2, str(""))
    else:
        product_edit_error = tk.Label(product_edit_frame, text="Unsuccessful attempt")
        product_edit_error.grid(column=2, row=5, columnspan=2)


def delete_product():
    #this is to delete a product off the system and display in listbox
    if product_delete_entry.get() != "":
        result = "DELETE FROM ProductInfo WHERE ProductName = ? "
        entry = [product_delete_entry.get()]
        cursor.execute(result, entry)
        con.commit()
        product_delete_listbox.delete(0, END)
        for row2 in view_data2():
            product_delete_listbox.insert(END, row2, str(""))
    else:
        tk.Label(product_delete_frame, text="Please enter details").grid(column=2, row=3, columnspan=1)


def for_stock_file():
    #This is to create a file that contains products, its price and quantity while also naming file after time
    cursor.execute("SELECT ProductName, ProductPrice, ProductQuantity FROM ProductInfo")
    my_results = (cursor.fetchall())
    time_name = time.strftime("%Hh-%Mm-%Ss, %d-%m-%Y")
    f = open("Stock Taking " + time_name + '.txt', 'w+')
    f.write(str(my_results))
    f.close()


def stock_frame_swap():
    #Acts as a frame swap as well as keep user up to date on stock on the frame with a listbox
    low_stock_frame.pack()
    stock_frame.forget()
    cursor.execute("SELECT ProductID, ProductName, ProductQuantity FROM ProductInfo where ProductQuantity <= 20")
    cursor.fetchall()
    product_delete_listbox.delete(0, END)
    for row3 in view_stock():
        stock_listbox.insert(END, row3, str(""))


def low_stock_file():
    #This is to create a file that can be printed and show products with less than 20 stock
    cursor.execute("SELECT ProductID, ProductName, ProductQuantity FROM ProductInfo where ProductQuantity <=20")
    query = (cursor.fetchall())
    time_name = time.strftime("%Hh-%Mm-%Ss, %d-%m-%Y")
    f = open("Low Stock File" + time_name + '.txt', 'w+')
    f.write(str(query))
    f.close()


#Database code to create or use an existing database
con = sqlite3.connect("AAT.db")
cursor = con.cursor()
#These are all the tables included
cursor.execute("""CREATE TABLE IF NOT EXISTS ProductInfo (
                CategoryNumber INTEGER,
                ProductID INTEGER, 
                ProductName TEXT, 
                ProductImage TEXT, 
                ProductDescription TEXT, 
                ProductAgeCategory INTEGER,
                ProductPrice REAL,
                ProductQuantity INTEGER
                )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ProductCategory ( 
                CategoryNumber INTEGER,
                CategoryName TEXT,
                ProductAgeCategory INTEGER,
                LocationInWarehouse TEXT
                )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Customer_queries (
                QueryID INTEGER,
                CustomerID INTEGER,
                Status BLOB, 
                Subject TEXT, 
                Message TEXT, 
                StaffID INTEGER, 
                Staff_response TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Customers (
                CustomerID INTEGER,
                CustomerName TEXT,
                Surname TEXT,
                Email TEXT,
                Country TEXT,
                City TEXT,
                Street_Address TEXT,
                Phone_Number INTEGER,
                Date_of_birth INTEGER,
                Debit_Credit_Card INTEGER,
                Db_Ct_Card_Check BLOB)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Sales_table ( 
                SaleID INTEGER,
                Date INTEGER,
                Time INTEGER,
                ProductID INTEGER,
                ProductName TEXT,
                ProductType TEXT,
                ProductPrice INTEGER,
                ProductAmount INTEGER,
                Discount REAL,
                PricePurchase INTEGER,
                ShippingPrice REAL,
                TotalPrice REAL,
                CustomerID INTEGER)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Staff_members (
                userID INTEGER,
                password TEXT,
                name TEXT,
                surname TEXT,
                email TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Supplier_Stock(
                ProductID INTEGER,
                CategoryNumber TEXT,
                ProductName TEXT,
                ProductPrice REAL,
                ProductStock INTEGER)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Suppliers (
                SupplierID INTEGER,
                SupplierName TEXT,
                SupplierCountry TEXT,
                SupplierAddress TEXT,
                SupplierEmail TEXT,
                SupplierContactNumber INTEGER)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Discounts (
                DiscountID INTEGER,
                DiscountName TEXT,
                DiscountCategory TEXT,
                ProductID INTEGER)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Applied_discounts (
                AppliedDiscountID INTEGER,
                ProductCategory INTEGER,
                ProductID INTEGER)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Customer_reviews (
                ReviewID INTEGER,
                CategoryNumber INTEGER,
                ProductID INTEGER,
                ProductName TEXT,
                CustomerID INTEGER,
                ReviewDetail TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Discount_scheme (
                DiscountSchemeID INTEGER,
                DiscountNrProducts INTEGER,
                DiscountPercentage REAL,
                DiscountID INTEGER)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Staff_members (
                UserID INTEGER,
                password TEXT,
                UserName TEXT,
                UserSurname TEXT,
                UserEmail TEXT)""")


#Start of programme
root = tk.Tk()
#Title of programme
root.title("AAT website UI")
#Size of programme
width, height = 600, 500
#This allows the programme to be centered in the middle of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cord = int((screen_width/2) - (width/2))
y_cord = int((screen_height/2) - (height/2))
root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))
#Fonts to be used
font1 = font.Font(family='georgia', size='28', weight='bold')
font2 = font.Font(family='georgia', size='15', weight='bold')
#Frames that shell be used
start_frame = tk.Frame(root)
second_frame = tk.Frame(root)
category_frame = tk.Frame(root)
category_add_frame = tk.Frame(root)
category_edit_frame = tk.Frame(root)
category_delete_frame = tk.Frame(root)
product_frame = tk.Frame(root)
product_add_frame = tk.Frame(root)
product_edit_frame = tk.Frame(root)
product_delete_frame = tk.Frame(root)
stock_frame = tk.Frame(root)
low_stock_frame = tk.Frame(root)

#First frame code
#Introducing user with heading
heading = tk.Label(start_frame, text='Welcome To The AAT Website!\n', font=font1)
#Placement on screen using the grid method
heading.grid(column=1, row=0, columnspan=4)
#Makes sure that start frame is shown first when starting programme
start_frame.pack(fill='both', expand=1)
#Text next to the entry bars to tell user what bar wants what
tk.Label(start_frame, text='Username').grid(column=2, row=1)
tk.Label(start_frame, text='Password').grid(column=2, row=2)
#Picture for login page
image = ImageTk.PhotoImage(Image.open("toyshop.png"))
login_pic = Label(start_frame, image=image)
login_pic.grid(column=1, row=5, columnspan=4)
#These are the entry bars with their position on the screen below it
entry1 = tk.Entry(start_frame)
entry1.grid(column=3, row=1, columnspan=1)
entry2 = tk.Entry(start_frame)
entry2.grid(column=3, row=2, columnspan=1)
#This is the button next to the entry bars so the user can move on
button = tk.Button(start_frame, text="Enter", fg='black', bg='white', command=login_id)
button.grid(column=4, row=1, rowspan=2)
#------------------------------------------------------------------
#This is the start of the next frame and includes the header, options and the buttons associated with them
tk.Label(second_frame, text='Please Select Task', font=font1).grid(column=3, row=1, columnspan=1)
tk.Label(second_frame, text='Categories').grid(column=2, row=2, columnspan=1)
tk.Label(second_frame, text='Products').grid(column=3, row=2, columnspan=1)
tk.Label(second_frame, text='Stock taking').grid(column=4, row=2, columnspan=1)

#To select option for system
category_button = tk.Button(second_frame, text="Enter", fg='black', bg='white', command=response_to_button1)
category_button.grid(column=2, row=3, rowspan=2)
product_button = tk.Button(second_frame, text="Enter", fg='black', bg='white', command=response_to_button2)
product_button.grid(column=3, row=3, rowspan=2)
stock_button = tk.Button(second_frame, text="Enter", fg='black', bg='white', command=response_to_button3)
stock_button.grid(column=4, row=3, rowspan=2)

#Image for frame
image2 = ImageTk.PhotoImage(Image.open("business.png"))
second_pic = Label(second_frame, image=image2)
second_pic.grid(column=2, row=6, columnspan=3)
#-----------------------------------------------------------------
#This is for the category page
tk.Label(category_frame, text='Add category').grid(column=2, row=2, columnspan=1)
tk.Label(category_frame, text='Edit category').grid(column=3, row=2, columnspan=1)
tk.Label(category_frame, text='Delete category').grid(column=4, row=2, columnspan=1)

#To select option for category
category_add_button = tk.Button(category_frame, text='Enter', fg='black', bg='white', command=category_add_button)
category_add_button.grid(column=2, row=3)
category_edit_button = tk.Button(category_frame, text='Enter',  fg='black', bg='white', command=category_edit_button)
category_edit_button.grid(column=3, row=3)
category_delete_button = tk.Button(category_frame, text='Enter', fg='black', bg='white', command=category_delete_button)
category_delete_button.grid(column=4, row=3)
category_return_page_button = tk.Button(category_frame,
                                        text='Go Back', fg='black', bg='grey', command=category_return_button)
category_return_page_button.grid(column=3, row=6, rowspan=1)

#Image for frame
image3 = ImageTk.PhotoImage(Image.open("categories.png"))
third_pic = Label(category_frame, image=image3)
third_pic.grid(column=2, row=4, columnspan=3, rowspan=1)
#-------------------------------------------------------------------
#This is for the category add page
tk.Label(category_add_frame, text='Please enter the details for your category you want to add').grid(column=1,
                                                                                                     row=0, columnspan=2)
tk.Label(category_add_frame, text='Category Number').grid(column=1, row=1)
tk.Label(category_add_frame, text="Category Name").grid(column=1, row=2)
tk.Label(category_add_frame, text="Age Range").grid(column=1, row=3)
tk.Label(category_add_frame, text="Warehouse Location").grid(column=1, row=4)
tk.Label(category_add_frame, text="""Use mouse scroll or click on box and use arrows to scroll listbox

Age Range example: 4-13, 2-7
Warehouse Location must include either north, east, south or west
followed by number counting upwards
e.g. north1, north2""").grid(column=1, row=8, columnspan=2)

#These are all the entry bars to obtain info from user
category_add_entry1 = tk.Entry(category_add_frame)
category_add_entry1.grid(column=2, row=1, columnspan=1)
category_number = category_add_entry1.get()

category_add_entry2 = tk.Entry(category_add_frame)
category_add_entry2.grid(column=2, row=2, columnspan=1)
category_name = category_add_entry2.get()

category_add_entry3 = tk.Entry(category_add_frame)
category_add_entry3.grid(column=2, row=3, columnspan=1)

category_add_entry4 = tk.Entry(category_add_frame)
category_add_entry4.grid(column=2, row=4, columnspan=1)

#to complete task, must press button
category_add_list = tk.Button(category_add_frame, text='Enter', fg='black', bg='white', command=add_category)
category_add_list.grid(column=2, row=5)
#To return to previous page
category_add_return_page_button = tk.Button(category_add_frame, text='Go Back', fg='black', bg='grey', command=category_add_return_button)
category_add_return_page_button.grid(column=1, row=6, columnspan=2)

#These are for a scrollbar and listbox to display info
add_scrollbar = Scrollbar(category_add_frame)
add_scrollbar.grid(column=3, row=7, sticky="ns")
add_listbox = Listbox(category_add_frame, font=('arial', 12, 'bold'), width=40, yscrollcommand=add_scrollbar.set)
add_listbox.grid(column=1, row=7, columnspan=2)
add_scrollbar.config(command=add_listbox.yview)
for row in view_data():
    add_listbox.insert(END, row, str(""))

#----------------------------------------------------------
#This is for the category edit page
tk.Label(category_edit_frame, text='Enter Change For Category Database', font=font2).grid(column=1, row=0, columnspan=2)
tk.Label(category_edit_frame, text='Updated Value').grid(column=1, row=1)
tk.Label(category_edit_frame, text='Previous Value').grid(column=1, row=2)
tk.Label(category_edit_frame, text='Column Name').grid(column=1, row=3)
tk.Label(category_edit_frame, text="""Use mouse scroll or click on box and use arrows to scroll listbox

Column Names:
CategoryNumber,CategoryName,ProductAgeCategory,LocationInWarehouse.
Make sure to write it exactly as shown!
""").grid(column=1, row=7, columnspan=2)

#Entry bars for obtaining info
category_edit_entry = tk.Entry(category_edit_frame)
category_edit_entry.grid(column=2, row=1, columnspan=1)

category_edit_entry2 = tk.Entry(category_edit_frame)
category_edit_entry2.grid(column=2, row=2, columnspan=1)

category_edit_entry3 = tk.Entry(category_edit_frame)
category_edit_entry3.grid(column=2, row=3, columnspan=1)

#To return back to other page
category_edit_return_page_button = tk.Button(category_edit_frame, text='Go Back', fg='black', bg='grey', command=category_edit_return_button)
category_edit_return_page_button.grid(column=1, row=5, columnspan=2)

#To complete the task
category_edit_list = tk.Button(category_edit_frame, text='Enter', fg='black', bg='white', command=edit_category)
category_edit_list.grid(column=2, row=4)

#Scrollbar and listbox
edit_scrollbar = Scrollbar(category_edit_frame)
edit_scrollbar.grid(column=3, row=6, sticky="ns")
edit_listbox = Listbox(category_edit_frame, font=('arial', 12, 'bold'), width=40, yscrollcommand=edit_scrollbar.set)
edit_listbox.grid(column=1, row=6, columnspan=2)
edit_scrollbar.config(command=edit_listbox.yview)
for row in view_data():
    edit_listbox.insert(END, row, str(""))

#-----------------------------------------------------------
#This is for the category delete page
tk.Label(category_delete_frame, text='Select Category Name to Delete', font=font2).grid(column=1, row=0, columnspan=2)
tk.Label(category_delete_frame, text='Enter CategoryName Here').grid(column=1, row=1)
tk.Label(category_delete_frame, text="""Use mouse scroll or click on box and use arrows to scroll listbox
""").grid(column=1, row=8, columnspan=2)

#Obtain info
category_delete_entry = tk.Entry(category_delete_frame)
category_delete_entry.grid(column=2, row=1, columnspan=1)

#To complete task
category_delete_list = tk.Button(category_delete_frame, text="Enter", fg='black', bg='white', command=delete_category)
category_delete_list.grid(column=2, row=2,)
#To return back to other page
category_delete_return_page_button = tk.Button(category_delete_frame, text='Go Back', fg='black', bg='grey', command=category_delete_return_button)
category_delete_return_page_button.grid(column=1, row=3, columnspan=2)

#scrollbar and listbox
delete_page_scrollbar = Scrollbar(category_delete_frame)
delete_page_scrollbar.grid(column=3, row=7, sticky="ns")
delete_page_listbox = Listbox(category_delete_frame, font=('arial', 12, 'bold'), width=40, yscrollcommand=delete_page_scrollbar.set)
delete_page_listbox.grid(column=1, row=7, columnspan=2)
delete_page_scrollbar.config(command=add_listbox.yview)
for row in view_data():
    delete_page_listbox.insert(END, row, str(""))

#-------------------------------------------------------------
#This is for the product page
tk.Label(product_frame, text='Add product').grid(column=2, row=2, columnspan=1)
tk.Label(product_frame, text='Edit product').grid(column=3, row=2, columnspan=1)
tk.Label(product_frame, text='Delete product').grid(column=4, row=2, columnspan=1)

#All the options for the products
product_return_page_button = tk.Button(product_frame, text='Go Back', fg='black', bg='grey', command=product_return_button)
product_return_page_button.grid(column=3, row=6, rowspan=1)
product_add_button = tk.Button(product_frame, text='Enter', fg='black', bg='white', command=product_add_button)
product_add_button.grid(column=2, row=3)
product_edit_button = tk.Button(product_frame, text='Enter',  fg='black', bg='white', command=product_edit_button)
product_edit_button.grid(column=3, row=3)
product_delete_button = tk.Button(product_frame, text='Enter', fg='black', bg='white', command=product_delete_button)
product_delete_button.grid(column=4, row=3)

#image for frame
image4 = ImageTk.PhotoImage(Image.open("products.png"))
forth_pic = Label(product_frame, image=image4)
forth_pic.grid(column=2, row=5, columnspan=3, rowspan=1)

#--------------------------------------------------
#This is for the product add page
tk.Label(product_add_frame, text='Please enter the details for the product you want to add').grid(column=1, row=0, columnspan=2)
tk.Label(product_add_frame, text='Please enter the details for the product you want to add').grid(column=1, row=0, columnspan=2)
tk.Label(product_add_frame, text="""Use mouse scroll or click on box and use arrows to scroll listbox
""").grid(column=1, row=12, columnspan=2)
product_add_entry1 = tk.Entry(product_add_frame)
product_add_entry1.grid(column=2, row=1, columnspan=1)
tk.Label(product_add_frame, text='Category Number ').grid(column=1, row=1)

product_add_entry2 = tk.Entry(product_add_frame)
product_add_entry2.grid(column=2, row=2, columnspan=1)
tk.Label(product_add_frame, text='Product ID').grid(column=1, row=2)

product_add_entry3 = tk.Entry(product_add_frame)
product_add_entry3.grid(column=2, row=3, columnspan=1)
tk.Label(product_add_frame, text='Product Name').grid(column=1, row=3)

product_add_entry4 = tk.Entry(product_add_frame)
product_add_entry4.grid(column=2, row=4, columnspan=1)
tk.Label(product_add_frame, text='Image').grid(column=1, row=4)

product_add_entry5 = tk.Entry(product_add_frame)
product_add_entry5.grid(column=2, row=5, columnspan=1)
tk.Label(product_add_frame, text='Description').grid(column=1, row=5)

product_add_entry6 = tk.Entry(product_add_frame)
product_add_entry6.grid(column=2, row=6, columnspan=1)
tk.Label(product_add_frame, text='age range').grid(column=1, row=6)

product_add_entry7 = tk.Entry(product_add_frame)
product_add_entry7.grid(column=2, row=7, columnspan=1)
tk.Label(product_add_frame, text='Price').grid(column=1, row=7)

product_add_entry8 = tk.Entry(product_add_frame)
product_add_entry8.grid(column=2, row=8, columnspan=1)
tk.Label(product_add_frame, text='Quantity').grid(column=1, row=8)

product_add_button = tk.Button(product_add_frame, text='Enter', fg='black', bg='white', command=add_product)
product_add_button.grid(column=2, row=9, columnspan=2)

product_add_return_page_button = tk.Button(product_add_frame, text='Go Back', fg='black', bg='grey', command=product_add_return_button)
product_add_return_page_button.grid(column=1, row=13, columnspan=2)

product_add_scrollbar = Scrollbar(product_add_frame)
product_add_scrollbar.grid(column=3, row=11, sticky="ns")

product_add_listbox = Listbox(product_add_frame, font=('arial', 12, 'bold'), width=40, yscrollcommand=product_add_scrollbar.set)
product_add_listbox.grid(column=1, row=11, columnspan=2)
product_add_scrollbar.config(command=product_add_listbox.yview)

for row2 in view_data2():
    product_add_listbox.insert(END, row2, str(""))

#This is for the product edit page
tk.Label(product_edit_frame, text='Enter Change For Product database', font=font2).grid(column=1, row=0, columnspan=2)
tk.Label(product_edit_frame, text='Updated Value').grid(column=1, row=1)
tk.Label(product_edit_frame, text='Previous Value').grid(column=1, row=2)
tk.Label(product_edit_frame, text='Column Name').grid(column=1, row=3)
tk.Label(product_edit_frame, text="""Use mouse scroll or click on box and use arrows to scroll listbox""").grid(column=1, row=8, columnspan=2)
tk.Label(product_edit_frame, text="""Column Names:
CategoryNumber,ProductID,ProductName,ProductImage,ProductDescription,ProductAgeCategory,ProductPrice,
ProductQuantity
Make sure to enter exactly as written above""").grid(column=1, row=9, columnspan=2)

product_edit_entry = tk.Entry(product_edit_frame)
product_edit_entry.grid(column=2, row=1, columnspan=1)
product_edit_entry2 = tk.Entry(product_edit_frame)
product_edit_entry2.grid(column=2, row=2, columnspan=1)
product_edit_entry3 = tk.Entry(product_edit_frame)
product_edit_entry3.grid(column=2, row=3, columnspan=1)

product_edit_list = tk.Button(product_edit_frame, text='Enter', fg='black', bg='white', command=edit_product)
product_edit_list.grid(column=2, row=4, columnspan=1)

product_edit_return_page_button = tk.Button(product_edit_frame, text='Go Back', fg='black', bg='grey', command=product_edit_return_button)
product_edit_return_page_button.grid(column=1, row=5, columnspan=2)

product_edit_scrollbar = Scrollbar(product_edit_frame)
product_edit_scrollbar.grid(column=3, row=6, sticky="ns")
product_edit_scrollbar2 = Scrollbar(product_edit_frame, orient='horizontal')
product_edit_scrollbar2.grid(column=1, row=7, columnspan=2, sticky="n")


product_edit_listbox = Listbox(product_edit_frame, font=('arial', 12, 'bold'), width=40, xscrollcommand=product_edit_scrollbar2, yscrollcommand=product_edit_scrollbar.set)
product_edit_listbox.grid(column=1, row=6, columnspan=2)
product_edit_scrollbar.config(command=product_edit_listbox.yview)
product_edit_scrollbar2.config(command=product_edit_listbox.xview)

for row2 in view_data2():
    product_edit_listbox.insert(END, row2, str(""))

#This is for the product delete page
tk.Label(product_delete_frame, text='Please Product name to delete', font=font2).grid(column=1, row=0, columnspan=2)
tk.Label(product_delete_frame, text='Enter product name here').grid(column=1, row=1)
tk.Label(product_delete_frame, text="""Use mouse scroll or click on box and use arrows to scroll listbox
""").grid(column=1, row=6, columnspan=2)
tk.Label(product_delete_frame, text="Ensure details are correct or impact will not be seen").grid(column=1, row=7, columnspan=2)

product_delete_entry = tk.Entry(product_delete_frame)
product_delete_entry.grid(column=2, row=1, columnspan=1)

product_delete_list = tk.Button(product_delete_frame, text='Enter', fg='black', bg='white', command=delete_product)
product_delete_list.grid(column=2, row=2)

product_delete_return_page_button = tk.Button(product_delete_frame, text='Go Back', fg='black', bg='grey', command=product_delete_return_button)
product_delete_return_page_button.grid(column=1, row=3, columnspan=2)

product_delete_scrollbar = Scrollbar(product_delete_frame)
product_delete_scrollbar.grid(column=3, row=5, sticky="ns")
product_delete_listbox = Listbox(product_delete_frame, font=('arial', 12, 'bold'), width=40, yscrollcommand=product_delete_scrollbar.set)
product_delete_listbox.grid(column=1, row=5, columnspan=2)
product_delete_scrollbar.config(command=product_delete_listbox.yview)
for row2 in view_data2():
    product_delete_listbox.insert(END, row2, str(""))

#This is for the Stock taking page
stock_return_page_button = tk.Button(stock_frame, text='Go Back', fg='black', bg='grey', command=stock_return_button)
stock_return_page_button.grid(column=0, row=5, columnspan=2)
make_stock_file_button = tk.Button(stock_frame, text='Yes', fg='black', bg='white', command=for_stock_file)
make_stock_file_button.grid(column=0, row=2)
view_understocked = tk.Button(stock_frame, text="View Low Stock", fg='black', bg='white', command=stock_frame_swap)
view_understocked.grid(column=0, row=3)
stock_question = tk.Label(stock_frame, text="""Would you like to create a stock file containing Products, 
Quantities and Prices from the Database?""")
stock_question.grid(column=0, row=1)
image5 = ImageTk.PhotoImage(Image.open("stock_take.png"))
fifth_pic = Label(stock_frame, image=image5)
fifth_pic.grid(column=0, row=4, columnspan=3, rowspan=1)

#This is the low stock page
tk.Label(low_stock_frame, text='Here are all the low stocked products', font=font2).grid(column=0, row=0)
tk.Label(low_stock_frame, text="""Use mouse scroll or click on box and use arrows to scroll listbox
""").grid(column=0, row=6)
tk.Label(low_stock_frame, text="""Press make file to create a file containing all products with low stock
""").grid(column=0, row=7)
stock_scrollbar = Scrollbar(low_stock_frame)
stock_scrollbar.grid(column=1, row=2, sticky="ns")
stock_listbox = Listbox(low_stock_frame, font=('arial', 12, 'bold'), width=40, yscrollcommand=product_edit_scrollbar.set)
stock_listbox.grid(column=0, row=2,)
stock_scrollbar.config(command=stock_listbox.yview)


low_stock_file = tk.Button(low_stock_frame, text="Make File", fg='black', bg='white', command=low_stock_file)
low_stock_file.grid(column=0, row=4)
stock_exit = tk.Button(low_stock_frame, text="Back", fg='black', bg='grey', command=stock_return)
stock_exit.grid(column=0, row=5)

#Lastly to make sure everything applies to the programme, mainloop() must be written
root.mainloop()
