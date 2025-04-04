# Hotel Booking System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)  
[![GitHub Stars](https://img.shields.io/github/stars/NevigChanuka/Hotel-Booking-System?style=social)](https://github.com/NevigChanuka/Hotel-Booking-System)  

## Overview

This is a Python-based Hotel Room Booking System that allows users to search, book, update, and cancel hotel room reservations. The system also includes an admin panel for managing hotel rooms.

## Prerequisites

- Python 3.x installed


### Installing Java

1. Download Python from **[python.org](https://www.python.org/)**.
2. Run the installer and ensure Python is added to PATH.


## How to Run

1. Download the project files.
2. Run the application:
```cmd
python main.py
```

## Features

### User Features:

1. Search rooms by type, price, or availability
2. View available rooms
3. Book a room with customer details
4. Update existing reservations
5. Cancel reservations
6. Generate booking receipts

### Admin Features:

1. Add new hotel rooms
2. Remove hotel rooms


## Technical Details

### Data Storage
The system stores data in three text files:

1. `Customers.txt` - Stores customer information
2. `Hotel Rooms.txt` - Stores room information 
3. `Hotel Reservations.txt` - Stores booking information

### Validation
1. __Customer Information__
    - Names are validated to contain only alphabetic characters and spaces.
    - Ages are validated to be between 18 and 120 years.
    - Phone numbers are validated to contain exactly 10 digits.
2. Room Management
    - Room numbers are validated to be unique within each hotel.
    - Prices are validated to be positive numbers with minimum value of $10.
3. Booking System
    - Dates are validated to be in YYYY-MM-DD format.
    - Check-in dates are validated to not be in the past.
    - Check-out dates are validated to be after check-in dates.
    - Room types are validated to be either "single", "double", or "family".
4. Admin Panel
    - Passwords are validated to match the exact case-sensitive value.
    - Hotel names are validated to prevent duplicate entries.
5. Reservation System
    - Rooms are validated for availability before booking.
    - Customer reservations are validated against existing bookings to prevent overlaps.

## License
MIT © Nevig Chanuka
