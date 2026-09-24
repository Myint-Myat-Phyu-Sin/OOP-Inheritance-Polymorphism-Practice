class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id
    def work(self):
        print(f"Working on {self.name}")
class Doctor(Staff):
      def __init__(self, name, staff_id, specialization):
        super().__init__(name,staff_id)
        self.specialization = specialization
      def work(self):
        print(f"Dr. {self.name} is  {self.specialization}")
class Nurse(Staff):
    def __init__(self, name, staff_id, ward):
        super().__init__(name,staff_id)
        self.ward = ward
    def work(self):
        print(f"Nurse {self.name} is  {self.ward}")
class Receptionist(Staff):
    def __init__(self, name, staff_id, shift):
        super().__init__(name,staff_id)
        self.shift = shift
    def work(self):
        print(f"{self.name} is  {self.shift}")
staff1 = Doctor("Sara", 1, "examining patients")
staff1.work()
staff2 = Nurse(" Ali", 2, "caring for patients")
staff3 = Receptionist("Mia", 3, "managing appointments")
staff2.work()
staff3.work()