dic={"Shikhar":1, "Gunjika":2, "Age":29}
print(dic["Shikhar"])
print(dic.get("Gunjika"))

print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(dic[key])
    
for key, value in dic.items():
    print(f"The key:value pair is {key}:{value} ")
    
