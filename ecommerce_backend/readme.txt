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
o	python -m venv venv
o	venv\Scripts\activate
-	pip install -r requirements.txt
-	python manage.py makemigrations
-	python manage.py migrate
-	python manage.py runserver
(Frontend)
-	flutter pub get
-	flutter run -d chrome   # For web
-	flutter run             # For mobile
