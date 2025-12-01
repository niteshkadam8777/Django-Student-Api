# Django-Student-API

*A foundational RESTful API built with Django REST Framework (DRF) for performing basic CRUD (Create, Read, Update, Delete) operations on student records. 
This project demonstrates the use of function-based API views.*
---
## ✨ Key Features
* RESTful Architecture: Uses Django REST Framework's @api_view decorators for function-based views.
* Data Modeling: Simple Django model (StudentModel) to represent student data (name, rollno, course).
* Serialization: Utilizes DRF's ModelSerializer for easy conversion between Python objects and JSON data.
* CRUD Operations: Full implementation for listing, creating, retrieving, updating, and deleting records.
---
## 🛠️ Technology Stack
* Backend Framework: Django
* API Framework: Django REST Framework (DRF)
* Language: Python
* Database: SQLite (default for development)
---

## 🚀 Setup and Installation
Follow these steps to get the project running locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/Django-Student-API.git](https://github.com/your-username/Django-Student-API.git)
cd Django-Student-API
cd backend

2. Create and Activate Virtual Environment
​It's recommended to use a virtual environment to manage dependencies.

# Create a virtual environment
python -m venv venv
# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
​Install Django and Django REST Framework.
pip install django
pip install djangorestframework

4. Run Migrations
​Apply the database schema changes for the StudentModel.
python manage.py makemigrations students_api
python manage.py migrate

5.Start the Server
python manage.py runserver
The API will now be running at http://127.0.0.1:8000/.


🚦 API Endpoints
​The root API path is /api/. All endpoints are accessed relative to this path.

1.Collection Endpoint (/api/students)
Path:/api/students

---------------------------------------------------------------------------------
| Method |      Path   |                Description                             |
| :----- | :-----------| :---------------------------------------------------   |
| GET  | /api/students | List All: Retrieves a list of all student records.     |
| POST | /api/students | Create: Adds a new student record to the database.     |
|DELETE| /api/students | *Warning: Deletes all student records.                 |
---------------------------------------------------------------------------------

2.Detail Endpoint (Retrieve/Update/Delete Single)
​Path: /api/student/<int:pk> (where <int:pk> is the student's ID)

-------------------------------------------------------------------------------------------
| Method | Path Example    |                 Description                                   |
| :---   | :---- ----------| :------------------------------------------------------------ |
| GET    | /api/student/10 | Retrieve: Retrieves the specific student record with ID 10.   |
| PUT    | /api/student/10 | Update: Updates the student record with ID 10.                |
| DELETE | /api/student/10 | **Delete: Removes the specific student record with ID 10.     |
--------------------------------------------------------------------------------------------
