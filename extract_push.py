import pandas as pd
from faker import Faker
import random
import string
from google.cloud import storage
import csv


fake = Faker()


def generate_password(length=8):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for _ in range(length))


def generate_employee_data(num_employees):
    data = []
    for _ in range(num_employees):
        employee = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'job_title': fake.job().replace(',', ''),  # Remove commas from job titles
            'department': fake.job().replace(',', ''),  # Remove commas from departments
            'phone_number': fake.phone_number(),
            'password': generate_password(),  # Generate a secure password
            'salary': int(fake.random_number(digits=5))  # Salary as integer
        }
        data.append(employee)
    
    return pd.DataFrame(data)


employee_data = generate_employee_data(100)

employee_data.to_csv('employee_data.csv', index=False)

def upload_to_gcs(df, bucket_name, filename):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    csv_data = df.to_csv(index=False, quoting=csv.QUOTE_MINIMAL)  # Use minimal quoting

    blob = bucket.blob(filename)
    blob.upload_from_string(csv_data)
    print(f"Employee data uploaded to GCS bucket: {bucket_name}/{filename}")

if __name__ == "__main__":
    num_employees = 100
    bucket_name = "bkt-employee-dat"  # Replace with your GCS bucket name
    filename = "employee_data.csv"
    df = generate_employee_data(num_employees)
    upload_to_gcs(df, bucket_name, filename)