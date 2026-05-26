🌍 Flight, Hotel and package booking platform (Django)

A full-featured Travel Booking Platform that allows users to book flights, hotels, and travel packages in one unified system.

✨ Features

👤 User System
User registration & login
Django session-based authentication
Profile management
Booking history for each user

✈️ Flight Booking
Search flights by source and destination
View available flights with details
Book flights instantly
View and manage flight bookings

🏨 Hotel Booking
Browse available hotels
View room types, prices, and availability
Book hotel rooms
Track hotel bookings

🧳 Travel Packages
Explore curated travel packages
View package details (price, duration, itinerary)
Book travel packages
Manage package bookings

🧾 Booking System
Unified booking management for:
Flights
Hotels
Packages
View all bookings in one dashboard

🛠️ Admin Panel
Add/update/delete flights
Manage hotels and rooms
Manage travel packages
View all bookings and users

🧰 Tech Stack
Backend: Python, Django
Frontend: HTML, CSS, JavaScript
Database: MySQL
Authentication: Django Auth System
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/travel.git
cd travel
2. Create virtual environment
python -m venv venv

Activate it:

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

3. Install dependencies
pip install django

(If you have requirements.txt)

pip install -r requirements.txt

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Create superuser (admin)
python manage.py createsuperuser

6. Run development server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/

Admin panel:

http://127.0.0.1:8000/admin/
📁 Project Structure
travel_portal/
│
├── users/              # Authentication system
├── flights/           # Flight booking module
├── hotels/            # Hotel booking module
├── packages/          # Travel packages module
├── bookings/          # Unified booking system
│
├── templates/         # HTML templates
├── static/            # CSS, JS, images
│
├── models.py          # Database models
├── views.py           # Business logic
├── urls.py            # URL routing
├── settings.py        # Django settings
└── manage.py          # Project entry point
🧩 Modules Overview

✈️ Flights Module
Flight search engine
Booking system
Flight details page

🏨 Hotels Module
Hotel listings
Room selection
Date-based booking

🧳 Packages Module
Travel package catalog
One-click booking
Package details page

👤 Users Module
Login / Register
Authentication handling
Profile & booking history

🧾 Bookings Module
Central booking manager
Handles all booking types
Tracks status (confirmed/cancelled)

🔐 Authentication
Django built-in authentication system
Login required for booking actions
Session-based secure login

🎯 Future Improvements
Payment gateway integration (Razorpay/Stripe)
Email/SMS booking confirmations
Advanced search filters
Seat/room selection UI
REST API (Django REST Framework)
React frontend upgrade

👨‍💻 Tech Summary
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: SQLite
Architecture: MVT (Model–View–Template)
📜 License

MIT License © 2026
