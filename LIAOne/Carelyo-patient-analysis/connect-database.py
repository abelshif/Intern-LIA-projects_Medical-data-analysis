
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt



class Carelyo_analysis_Database:

    def __init__(self):
        """ Reads the Patient data clean.csv file and displays it as 
        a dataframe table called patient_df.
        """

        self.patient_df = pd.read_csv('./LIAOne/Carelyo data analysis/Patient_data_clean.csv') 

               
    def Create_cleaned_Patient_data_in_carelyo_new_api_database(self):
        """ Creats a connection to the carelyo_new_api.db and import the Patient data clean.csv 
        in to carelyo_new_api.db

        Returns:
            The Patient_data_clean table in the carelyo_new_api.db. 

        """

        self.db_conn = sqlite3.connect('carelyo_new_api.db') # connects to carelyo_new_api database 
        self.cur = self.db_conn.cursor()
        Patient_data_clean = self.patient_df.to_sql('Patient_data_clean', self.db_conn) # creates "Patient_data_clean" table in carelyo_new_api database  
                                                              
        return Patient_data_clean 

    def _extract_patient_medical_problems(self, medical_problems):
        """ Extracts  Patients of a specific medical_problems  
        from patient_data_clean table in carelyo_new_api.db

        Args:
            medical_problems: medical_problems related to patients to be extracted

        Returns:
            medical_problems: Patient_data_clean table to a specified medical_problems 
        """
        medical_problems = pd.read_sql("SELECT * FROM Patient_data_clean WHERE medical_problems = 'overweight'", self.db_conn)
        
        return medical_problems.head()
        

    def _extract_patient_community(self, community):
        """ Extracts  Patients of a specific community  
        from patient_data_clean table in carelyo_new_api.db

        Args:
            community: community related to patients to be extracted

        Returns:
            community: Patient_data_clean table to a specified community 
        """
        community = pd.read_sql("SELECT * FROM Patient_data_clean WHERE community = 'urban'", self.db_conn)
        
        return community.head()


    def plot_medical_problems(self):
        """ Histogram plot of medical_problems from 
        patient_data_clean table in carelyo_new_api.db
        """
        
        sns.histplot(self.patient_df['medical_problems'])
        plt.show()   

    def plot_community(self):
        """ Histogram plot of community from 
        patient_data_clean table in carelyo_new_api.db
        """
        
        sns.histplot(self.patient_df['community'])
        plt.show()                


def main():
    """ Creats an object of "Carelyo_analysis_Database" and implement its 
    methods.
    """
    database = Carelyo_analysis_Database() 
    database.Create_cleaned_Patient_data_in_carelyo_new_api_database() 
    print(" ")
    print(database._extract_patient_medical_problems('overweight'))
    print(" ")
    print(database._extract_patient_community('urban'))
    database.plot_medical_problems()
    database.plot_community()

    
if __name__ == "__main__":
    main() # call on the main function