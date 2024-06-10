'''Q1'''
class employee:
    def __init__(self):
        self.empname='Sahu'
        self.empdept='waves'
        self.empaddress='E-49'
    def display(self):
        print(self.empname,self.empdept,self.empaddress)
class manager(employee):
    def __init__(self):
        super().__init__()
        self.manid='17193'
        self.mandept='waves'
        self.juniors=17
    def case(self):
        self.display()
        print(self.manid,self.mandept,self.juniors)
b=manager()
b.case()

'''Q2'''
class person:
    def __init__(self):
        self.name='uja'
        self.age=16
        self.place='laplace'
    def case(self):
        print(self.age,self.name,self.place)
class hospital:
    def get(self):
        self.bed_no=9
        self.illness='mental patient'
    def show(self):
        print(self.bed_no,self.illness)
class patient(person,hospital):
    def __init__(self):
        super().__init__()
        self.get()
        self.dob=10
        self.patient_id=17193
    def display(self):
        self.case()
        self.show()
        print(self.dob,self.patient_id,sep='\n')
a=patient()
a.display()