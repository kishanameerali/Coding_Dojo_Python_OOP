class Patient(object):
    def __init__ (self, id, patient_name, allergies):
        self.id = id
        self.patient_name = patient_name
        self.allergies = allergies
        self.bed_num = 'none'

class Hospital(object):
    def __init__ (self, hospital_name):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = 5

    def admit(Patient):
        if len(self.patients) >= self.capacity:
            print "Sorry Hospital is full"
        else:
            self.patients += 1
            self.bed_num = ((self.patients).index(Patient)) + 1
            print "Patient has been admitted"

    def discharge(Patient):
        (self.patients).remove(Patient)

patient1 = Patient(1, 'Bruce Wayne', 'peanuts')
patient2 = Patient(2, 'Clark Kent', 'kryptonite')
patient3 = Patient(3, 'Peter Parker', 'bug spray')

Hospital1 = Hospital('North York General')
Hospital2 = Hospital('Scarborough General')
Hospital3 = Hospital('St Mikes')

Hospital1.admit(patient1)
Hospital1.admit(patient2)
Hospital1.admit(patient3)
