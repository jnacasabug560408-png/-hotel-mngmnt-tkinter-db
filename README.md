# 🏨 Hotel Inventory Management System

A desktop application built with **Python (Tkinter)** and **MySQL** for managing hotel operations — including inventory, customers, bookings, and rooms.  
This project was developed for learning and demonstration purposes.

<img width="1919" height="1005" alt="Screenshot 2025-10-17 210619" src="https://github.com/user-attachments/assets/15e6a293-5ba2-420c-a851-a9ee59f24762" />




## 🚀 Features

- 🔐 **Login system** (Admin / Staff)
- 📊 **Dashboard** with real-time counts of customers, bookings, inventory, and rooms
- 📦 **Inventory Management**
  - Add, update, delete items
  - Auto-calculate total value = quantity × price
- 👥 **Customer Management**
  - Add, update, and delete customers
- 🏠 **Room Management**
  - Manage room details (number, type, and status)
- 📅 **Booking Management**
  - Record customer bookings and check-in/check-out details
- 🔁 **Auto-refresh dashboard** every 10 seconds
- 🧾 **Simple, clean UI** with sidebar navigation



## 🧩 Tools and Technologies

| Tool | Purpose |
|------|----------|
| **Python 3.x** | Programming language |
| **Tkinter** | GUI framework |
| **MySQL** | Database |
| **mysql-connector-python** | Connects Python to MySQL |
| **tkcalendar** | Calendar widget |
| **Pillow (PIL)** | Image handling |





<h2 style="color:red;"><b>⚙️ Setup & Installation</b></h2>

1. Clone the repository  
   [https://github.com/jnacasabug560408-png/-hotel-mngmnt-tkinter-db/](https://github.com/jnacasabug560408-png/-hotel-mngmnt-tkinter-db/)

2. Create the database  
   Open MySQL and create a database (e.g. `hotel_db`)

   Create the necessary tables: `customers`, `inventory`, `booking`, and `room_list`

   Match all column names to those used in the code (e.g. `item_name`, `category`, `quantity`, etc.)

3. Update database connection  
   ```python
   host="localhost",
   user="root",
   password="",
   database="hotel_db"


<h2 style="color:red;"><b>🧠 System Flow</b></h2>

Login Page → User logs in based on role (admin)

Main Dashboard → Displays real-time summary (customers, bookings, inventory, rooms)

Navigation Sidebar → Allows access to:

Customer Management

Booking Management

Inventory Management

Room Management

System Details
Dashboard Auto-Refresh → Updates every 10 seconds


<h2 style="color:red;"><b>🧾 Example Database Tables</b></h2> <h3 style="color:red;"><b>📦 Inventory Table</b></h3>
| Column     | Type         |
| ---------- | ------------ |
| item_name  | VARCHAR(255) |
| category   | VARCHAR(255) |
| quantity   | INT          |
| unit_price | FLOAT        |

<h3 style="color:red;"><b>👥 Customer Table</b></h3>
| Column  | Type         |
| ------- | ------------ |
| name    | VARCHAR(255) |
| contact | VARCHAR(255) |
| email   | VARCHAR(255) |


<h2 style="color:red;"><b>📸 Screenshots</b></h2>

Add screenshots of your system interface here (e.g. dashboard, inventory, login page).

Login page
<img width="594" height="790" alt="Screenshot 2025-10-09 080535" src="https://github.com/user-attachments/assets/0c478c81-5114-46d0-a6ac-963d3441cff7" />

Dashboard
<img width="1919" height="1004" alt="Screenshot 2025-10-09 080724" src="https://github.com/user-attachments/assets/1855c31a-a2b9-40d0-8d84-5c4f89f4cac0" />

Inventory
<img width="1919" height="1005" alt="Screenshot 2025-10-17 210619" src="https://github.com/user-attachments/assets/1a184d5d-f4a3-4050-92a2-48e2fe789c42" />


<h2 style="color:red;"><b>📋 Limitations</b></h2>

Some tables may not have full search/filter functions

Requires MySQL to be running locally

Minor validation improvements can be added for better error handling

<h2 style="color:red;"><b>🧱 Future Enhancements</b></h2>

Add export to CSV or PDF

Add search and filter options

Add booking receipts and reports

Improve login security with hashed passwords


<h2 style="color:red;"><b>📚 Authors & Credits</b></h2>

Developed by [Jillian Grace C. Nacasabug]
For academic and educational purposes.


<h2 style="color:red;"><b>✅ Summary</b></h2>

The Hotel Inventory Management System simplifies hotel operations by integrating booking, room, customer, and inventory management in one application.
It demonstrates the use of Python + Tkinter + MySQL for building real-world management systems.
