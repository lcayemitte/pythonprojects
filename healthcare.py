class Patient:

    def __init__(self, patient_id, name, age, gender, medical_history = None):

        self.patient_id = patient_id

        self.name = name

        self.age = age

        self.gender = gender

        self.medical_history = medical_history or []



        def add_medical_record(self, record):

            self.medical_history.append(record)



        def display_info(self):

            print(f"\nPatient ID: {self.patient_id}")
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Gender: {self.gender}")
            print ("Medical History")

            for record in self.medical_history:

                print(f" - {record}")



class HealthCareSystem: 

    def __init__(self):


        self.patients = {}

        def add_patient(self):

            patient_id = input("Enter patient ID: ")

            name = input("Enter patient name: ")

            age = input("Enter patient age: ")

            gender = input("Enter patient gender: ")

            patient = Patient(patient_id, name, age, gender)

            self.patients[patient_id] = patient

            print(f"\nPatient {name} added successfully.")


            def view_patient(self):

                patient_id = input("\nEnter Patient ID to view: ")

                patient = self.patients.get(patient_id)

                if patient:

                    patient.display_info()

                else: 

                    print("Patient not found")


            def add_medical_record(self):

                patient_id = input("\nEnter patient Id to add medical record: ")

                patient = self.patients.get(patient_id)

                if patient:

                    record = input("Enter medical record: ")
                    patient.add_medical_record(record)
                    print("Medical record added successfully.")

                else:

                    print("Patient not found.")



    def run(self):

        while True:

            print("\nHealthCare Management System")

            print("1. Add Patient")
            print("2. View Patient")
            print("3. Add Medical Record")
            print("4. Exit")
            

            choice = input("Enter your choice: ")

            if choice == "1":

                self.add_patient()


            elif choice == "2":

                self.view_patient()


            elif choice == "3":
                self.add_medical_record()



            elif choice == "4":

                print("Existing ....")
                break

            else:

                print("Invalid choice. Please try again.")




if __name__  == "__main__":

    system = HealthCareSystem()

    system.run()






    