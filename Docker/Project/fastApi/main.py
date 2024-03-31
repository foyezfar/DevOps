from fastapi import FastAPI
#import psycopg2
#from fastapi.middleware.cors import CORSMiddleware

# FastAPI app instance
app = FastAPI()

# Allow CORS for all origins during development
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# Database connection
# conn = psycopg2.connect(
#     dbname="postgres",
#     user="postgres",
#     password="password",
#     host="localhost"
# )
# cursor = conn.cursor()

# Endpoint to get all employees
# @app.get("/employees/")
# async def get_employees():
#     cursor.execute("SELECT * FROM employee")
#     employees = cursor.fetchall()
#     return {"employees": employees}

# Sample employee data
sample_employees = [
    {"id": 5, "first_name": "John", "last_name": "Doe", "department": "Engineering", "position": "Software Engineer", "salary": 75000.00},
    {"id": 6, "first_name": "Jane", "last_name": "Smith", "department": "Human Resources", "position": "HR Manager", "salary": 85000.00},
    {"id": 7, "first_name": "Michael", "last_name": "Johnson", "department": "Finance", "position": "Financial Analyst", "salary": 70000.00},
    {"id": 8, "first_name": "Emily", "last_name": "Williams", "department": "Marketing", "position": "Marketing Specialist", "salary": 65000.00}
]

# Endpoint to get all employees
# @app.get("/employee_sample/")
# async def get_employees():
#     return {"employees": sample_employees}

@app.get("/employee_sample/")
async def get_employees():
    return {"employees": sample_employees}