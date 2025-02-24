# Bynry_jobs_assignment

This is a Django-based web application for managing consumer services for gas utilities

# Installation and Setup

#1️. Clone the Repository

git clone https://github.com/Sk9singh/Bynry_jobs_assignment.git
cd Bynry_jobs_assignment

#2. Install Dependencies

pip install -r requirements.txt

#3. Configure the Database

Update the DATABASES section in settings.py:

#4. Apply Migrations

python manage.py migrate

#5. Create a Superuser (For Admin Access)

python manage.py createsuperuser
 Enter username, email, and password as prompted.

#6. Run the Development Server

python manage.py runserver

# API Endpoints

POST
/api/service-request/

GET
/api/service-request/{id}/

PUT
/api/service-request/{id}/

DELETE
/api/service-request/{id}/

GETALL
/api/service-request/

