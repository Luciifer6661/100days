class person:
    name="Shikhar"
    occupation="Engineer"
    
    def info(self):
        
        print(f"{self.name} is an {self.occupation}")
        
a=person()
b=person()
c=person()
print(a.name)
a.name="Gunjika"
b.name="Prakhar"

a.info()
b.info()
c.info()