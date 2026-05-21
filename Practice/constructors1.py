class person:
    employees=0
    company="UBS" #class variable
    def __init__(self,n,o):
        self.name=n
        self.occ=o    
        person.employees+=1
        
    def info(self):
        
        print(f"{self.name} is an {self.occ} in {self.company} with {self.employees} employee")

a=person("Shikhar", "Engineer")



print(person.company)
person.company="Google"
print(a.name)
a.info()

b=person("Gunjika","Analyst")
b.company="Capgimini"
print(b.occ)
b.info()
person.info(a)