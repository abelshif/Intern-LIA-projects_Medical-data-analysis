
import pandas as pd
import pymysql
import sqlite3
from datetime import datetime

# # cleaned dataset
# patient_dataframe = pd.read_csv('./LIATwo/Carelyo Model Analysis/cleaned_patient.csv')
# doctor_dataframe = pd.read_csv('./LIATwo/Carelyo Model Analysis/cleaned_doctor.csv')
# consultation_dataframe = pd.read_csv('./LIATwo/Carelyo Model Analysis/cleaned_consultation.csv')


# #Calculating the age variable(column) based from the date_of_birth column in the patient_datafram
# patient_dataframe['date_of_birth'] = pd.to_datetime(patient_dataframe['date_of_birth']) # Convert date_of_birth column to datetime
# patient_dataframe['age'] = (datetime.now() - patient_dataframe['date_of_birth']) // pd.Timedelta(days=365) # Calculate age by subtracting date_of_birth from current date

# #Calculating years_of_experience variable based from graduation_date column in doctor_datafram
# doctor_dataframe['graduation_date'] = pd.to_datetime(doctor_dataframe['graduation_date']) # Convert graduation_date column to datetime
# doctor_dataframe['years_of_experience'] = (datetime.now() - doctor_dataframe['graduation_date']) // pd.Timedelta(days=365) # Calculate years_of_experience by subtracting
#                                                                                                                            # graduation_date from current date


# #Merging patient_datafram and doctor_datafram to consultation_datafram
# patient_consultation = pd.merge(consultation_dataframe, patient_dataframe[["patient_id", "age", "gender", "post_code"]], on="patient_id", how="left")
# doctor_patient_consultation = pd.merge(patient_consultation, doctor_dataframe[["doctor_id", "years_of_experience"]], on="doctor_id", how="left")

# #The newly merged Simulated_dataframe
# simulated_dataframe = doctor_patient_consultation.drop(["doctor_id", "patient_id"], axis=1)

simulated_dataframe = pd.read_csv('./LIATwo/Carelyo Model Analysis/simulated_data.csv')
# Connect to MySQL database

# mydb = pymysql.connect(
#   host='127.0.0.1',
#   user='root',
#   password='Lovewins1234567',
#   database='carelyo_new_api'
# )

mydb = sqlite3.connect('Carelyo_.db')

# Create table in the database
consultation = simulated_dataframe.to_sql('consultation', mydb)

# Create a cursor object
# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM consultation")

# # Fetch all rows
# rows = mycursor.fetchall()

# # # Add columns to the table
# # mycursor.execute("ALTER TABLE consultation ADD COLUMN age INT")
# # mycursor.execute("ALTER TABLE consultation ADD COLUMN years_of_experience INT")

# # Push the updated table back to MySQL
# for row in rows:
#   #mycursor.execute("UPDATE consultation SET age = %s, years_of_experience = %s WHERE id = %s", (row[3], row[4], row[0]))
#   mycursor.execute(f"UPDATE consultation SET age = {row['age']} WHERE id = {row['id']}")
#   mycursor.execute(f"UPDATE consultation SET years_of_experience = {row['years_of_experience']} WHERE id = {row['id']}")
  
# Commit the changes
mydb.commit()

# Close the connection
mydb.close()
