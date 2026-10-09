# CodeAlpha_SQL_Injection_Security
A Python-based secure login system using SQLite, parameterized queries, and password hashing to prevent SQL injection attacks.

# CodeAlpha SQL Injection Security

## Project Overview
This project is a Python-based secure login system designed to protect user information from SQL injection attacks.

## Objective
The main objective is to secure user login details and prevent unauthorized access to the database.

## Technologies Used
- Python
- SQLite Database
- Bcrypt Password Hashing
- Parameterized SQL Queries

## Features
- Secure user registration.
- Password hashing for better security.
- Protection against SQL injection attacks.
- Validation of login credentials.
- Secure database operations.
- Prevention of unauthorized access.

## How It Works
1. Creates a user database.
2. Registers users with hashed passwords.
3. Stores user details securely.
4. Checks login credentials using parameterized SQL queries.
5. Allows access only when the username and password are correct.

## Installation
Install Python and run the following command:

pip install bcrypt

## How to Run
1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run the following command:

   python main.py

4. Enter the username and password when prompted.

## Expected Result
The system displays a success message for valid login credentials and an error message for invalid credentials.

## Security Note
This project demonstrates basic SQL injection prevention and password hashing. It is a learning project and does not represent a complete cloud security solution.

## Conclusion
This project demonstrates how parameterized SQL queries and password hashing can improve the security of a login system.

## Developed For
CodeAlpha Cloud Computing Internship
