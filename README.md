# Gas Utility Web App

Welcome to the Gas Utility Web App! This Django-based application allows customers to submit service requests online, track the status of their requests, view their account information, and provides customer support representatives with tools to manage requests and provide support.

## Table of Contents
- [Features](Features)
- [Setup](#setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Features
- Customers can submit service requests online.
- Customers can track the status of their service requests.
- Customers can view their account information.
- Customer support representatives can manage requests and provide support.

## Setup
1. Clone the repository:
     ```bash
     git clone https://github.com/Sagarkeshave/GasUtilityApp.git
     cd GasUtilityApp
2. Create a virtual environment:
   ```
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```
     pip install -r requirements.txt
4. Set up the database:
   ```
     python manage.py migrate
5. Create a superuser for admin access:
   ```
     python manage.py createsuperuser
6. Start the development server:
    ```
     python manage.py runserver

## Usage

* Visit http://localhost:8000 in your browser to access the app.
* Customers can submit requests, track requests, and view account information.
* Customer support representatives can log in to manage requests using their credentials.

Screenshots
>* Showcasing the different features and aspects of app.

