# class hats:
#     def __init__(self):
#         self.first=10
#         self.second=20
#     def print2(self):
#         print(self,self.second)    
# x=hats()
# x.print2()
# print(type(x))
# list1=['maths','cs','english','chemistry','physics'];d={}
# class XI_CS:
#     def __init__(self):
#         list2=list3=[];ans=''
#         while ans!='no':
#             list2=[]
#             self.name=input('enter your name:')
#             self.roll_no=int(input('enter your Roll No.:'))
#             for i in range(5):
#                 self.marks=input(f"enter your marks in {list1[i]}:")
#                 list2.append(self.marks)
#             h=(self.name,self.roll_no,list2)
#             d[self.name]=h
#             ans=input('Do you want to add another student yes/no:')
#     def display(self):#create while loop
#         ask=input('enter whose data you want:')
#         if ask in d.keys():
#             #print('Name:',d[ask],'\n','class:',self.roll_no,'\n','marks scored:',list2)
#             print(d[ask])
#         else:
#             print('student not registered:')
# pg=XI_CS()
# pg.display()

'''class below class'''
# class student:
#     x=10
#     def __init__(self):
#         self.name=input('Enter the name:')
#         self.laptop=laptop()
#     def display(self):
#         print(self.name,'is awarded a laptop of',self.laptop.ram,self.laptop.processor,self.laptop.make,'attributes')
# class laptop:
#     def __init__(self):
#         self.ram=64
#         self.processor='i9'
#         self.make='acer'

# a=student()
# a.display()

'''class in class'''
class student:
    class laptop:
        def __init__(self):
            self.ram=64
            self.processor='i9'
            self.make='acer'
        def display(self):
            print('i am a laptop')
    def __init__(self):
        self.name=input('Enter the name:')
        self.lapt=student.laptop()
    def display(self):
        print(self.name,'is awarded a laptop of',self.lapt.ram,self.lapt.processor,self.lapt.make,'attributes')
a=student()
b=student.laptop()
a.display()
b.display()
print(type(a),type(b))

