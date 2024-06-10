# class student:
#     def __init__(self):
#         self.name=input('enter the name:')
#         self.rollno=int(input('enter roll no.:'))
#         self.dob=student.day()
#     def display(self):
#            print('name:',self.name,'roll no.:',self.rollno,'day:',self.dob.date,'month:',self.dob.month,'year:',self.dob.year)
#     class day:    #nested class
#         def __init__(self):
#             self.date=int(input('enter the date:'))
#             self.month=input('enter the month:')
#             self.year=int(input('enter the year:'))
# a=student()
# a.display()

# d={}
# class country:
#     def __init__(self):
#             self.country=input('enter the country:')
#             self.capital=input('enter the capital:')
#             self.currency=input('enter the currency:')
# for i in range(2):
#     a=country()
#     d[a.country]=(a.country,a.capital,a.currency)
# ask=input("enter which country's data:")
# print(d[ask])

class student:
    def __init__(self):
        self.name=input('enter the name:')
        self.rollno=int(input('enter roll no.:'))
        self.dob=student.day()
    def display(self):
           print('name:',self.name,'roll no.:',self.rollno,'day:',self.dob.date,'month:',self.dob.month,'year:',self.dob.year)
    class day:    
        def __init__(self):
            self.date=int(input('enter the date:'))
            self.month=input('enter the month:')
            self.year=int(input('enter the year:'))
a=student()
a.display()