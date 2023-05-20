# Workflow documentation

1. Connect to Carelyo via github invitation.
2. Clone carelyo-api repository and connect to Carelyo workbench locally.
3. Run carelyo-api.sql on the Carelyo workbench and study relations beteween tables.
4. Create an ER diagrams for selected tables in the carelyo-api database.
5. Create and Populate a new carelyo database locally using the original carelyo-api. 
6. Do analysis and visualization using the new populated database (carelyo_new_api) tables on Jupyter Notebook, python and Powwer BI.
 

## ER diagrams documentation

The ERDs are created to examine relationship between tables created in the carelyo_api database. 

These ERDs focus on the 6 main relationship in the carelyo_api database tables namely: body_area ERD, consultation ERD, dependent-Patient-child-hospital ERD, doctor ERD, hospital ERD and illness-symptom ERD.

1. The body_area ERD shows the one to many relation between the body_area and the body_area_associated_symptoms using the foreign key body_area_id.

2. The consultation ERD show the one to many relation between consultation and consultation_symptoms using the foreign key consultation_id.

3. The dependent-Patient-child-hospital ERD reveals the one to many relation of dependent with patient_dependents, patient with patient_journal, patient_journal with patient_journal_doctornotes, child with patient_children and hospital with patient using foreign keys dependents_id, patient_id, patient_journal_id, children_child_id and hospital_id respectively. Moreover, it can be revealed that by the trastivity theory there is a one to one relation between dependent and patient, child and patient, patient_dependents and patient_children, dependent and child. In addition by trastivity there also exist a many to one relation between dependent and hospital, child and hospital, patient_journal_doctornotes and patient.   

4. The doctor ERD show the one to many relation between doctor and dctor_academic_qualifications, doctor_clinical_focuses,  doctor_conference_presentation, doctor_attached_doc,  doctor_current_apointments and doctor_hospital_accreditations using the foreign key doctor_id.

5. The hospital ERD show the one to many relation between hospital and hospital_departments, hospital_hospital_Staff_ids and hospital_Staff using the foreign key hospital_id.

6. The illness-symptom ERD reveals the one to many relation of illness with illness_symptoms and symptom with illness_symptom using the foreign keys illness_id and symptom_id respectively. Moreover, it can also be seen that by transitivity there exists a one to one relation between illness and symptom. 

 
 
