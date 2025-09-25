Flutter-Django E-Commerce Application

Project Overview
This is a full-stack E-commerce application built with Flutter (Web & Mobile) for the frontend and Django for the backend.  
It includes a Customer App and a Separate Admin Dashboard, allowing users to browse products, manage cart, place orders, and enabling admins to manage products and orders efficiently.

Features
User (Customer) App
- Login / Signup using email & password
- Browse product catalog (image, name, price, description)
- Add / remove products in cart
- Checkout and place orders (simulated payment)

Admin Dashboard
- Secure admin login
- Add, edit, and delete products
- View orders placed by users

Tech Stack
- Frontend: Flutter (Web & Mobile)
- Backend: Django (Python)
- Database: MySQL
- State Management: setState

Setup Instructions (Backend)
-	Create a virtual environment
-   python -m venv venv
-   venv\Scripts\activate

-	pip install -r requirements.txt

-   connect your MySQL Database to settings.py

-	python manage.py makemigrations
-	python manage.py migrate
-	python manage.py runserver

-   Create superuser
    python manage.py createsuperuser

-   Login as default django admin 

-   Create Groups as ('user' and 'admin' - remmeber all in small letters)
-   Create Project Admin (Seperate admin as mentioned in the task ) 
    -   Click plus icon near User in Dashboard
    -   Create Admin username and password and save
    -   Add this User to admin group
    -   save

(Frontend)
-	flutter pub get
-   Set your wifi IP address in main.dart
-	flutter run -d chrome   # For web
-	flutter run             # For mobile
