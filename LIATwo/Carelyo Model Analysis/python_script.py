import pymysql
import pandas as pd
from datetime import datetime

# Replace the following with your MySQL database credentials

host="127.0.0.1",
user="root",
password="Lovewins1234567",
db_name="carelyo_new_api"


# # Establish a connection to the MySQL database

mydb = pymysql.connect(host=host, user=user, password=password, db=db_name)


# Read the tables into pandas DataFrames
doctor_df = pd.read_sql("SELECT * FROM doctor", mydb)
patient_df = pd.read_sql("SELECT * FROM patient", mydb)

# Calculate the years of experience for each doctor
current_year = datetime.now().year
doctor_df['graduation_date'] = pd.to_datetime(doctor_df['graduation_date'])
doctor_df['years_of_experience'] = current_year - doctor_df['graduation_date'].dt.year

# Calculate the age of each patient
patient_df['date_of_birth'] = pd.to_datetime(patient_df['date_of_birth'])
patient_df['age'] = current_year - patient_df['date_of_birth'].dt.year

# Update the doctor and patient tables with the new data
mycursor = mydb.cursor()

for index, row in doctor_df.iterrows():
    update_query = f"UPDATE doctor SET years_of_experience = {row['years_of_experience']} WHERE id = {row['id']}"
    mycursor.execute(update_query)

for index, row in patient_df.iterrows():
    update_query = f"UPDATE patient SET age = {row['age']} WHERE patient_id = {row['patient_id']}"
    mycursor.execute(update_query)

# Commit the changes and close the connection
mydb.commit()
mycursor.close()
mydb.close()
