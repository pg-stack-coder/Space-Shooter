class a:
    def get(self):
        self.no=int(input('enter the number:'))
        self.no2=int(input('enter the number:'))
    # def __add__(self,o):
    #     z=a()
    #     z.no=self.no+o.no
    #     z.no2=self.no2+o.no2
    #     print(z.no,z.no2)
    def __str__(self):
         return self.no+self.no2
    def __gt__(self,p):
        if self.no> p.no :
            return True
        else:
            return False
j=a();k=a()
j.get();k.get()
print(j>k)
# print(j+k)