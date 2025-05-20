# coffee_shop

This project implements a domain model for a Coffee Shop using Python. It consists of three main entities: Customer, Coffee, and Order, with defined relationships and functionality to manage a coffee shop's operations.

#Structure
coffee_shop/
├── customer.py
├── coffee.py
├── order.py
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   ├── test_order.py
├── README.md
├── Pipfile
├── Pipfile.lock

Entities and Relationships

Customer: Represents a customer who can place multiple orders. Attributes include name (1-15 characters).
Coffee: Represents a coffee type available for order. Attributes include name (minimum 3 characters).
Order: Represents a transaction linking a customer to a coffee with a price (1.0-10.0).

Relationships:

A Customer can have many Orders.
A Coffee can be part of many Orders.
An Order belongs to one Customer and one Coffee.
Customer and Coffee have a many-to-many relationship through Order.

Setup Instructions

1. Create Project Directory:
mkdir coffee_shop
cd coffee_shop

2. Set Up Virtual Environment:
pip install pipenv
pipenv install
pipenv shell

3. Install Testing Dependencies:
pipenv install pytest

4. Create Files:
Place customer.py, coffee.py, and order.py in the root directory.
Create a tests directory and add test_customer.py, test_coffee.py, and test_order.py.

Features

Input Validation: All setters validate input types and ranges, raising ValueError for invalid inputs.
Single Source of Truth: Uses properties to ensure data integrity.
Relationships: Properly manages one-to-many and many-to-many relationships.
Exception Handling: Raises exceptions for invalid operations or inputs.

Requirements

Python 3.3+
Pipenv
Pytest (for running tests)