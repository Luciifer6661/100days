letter="Hey! My name is {} and I am from {}"
country="India"
name="Shikhar"
print(letter.format(name,country))
print(f"Hey, My name is {{name}} and I am going to {{country}}")
print(f"Hey, My name is {name} and I am going to {country}")

txt="for only {price:.3f} dollars!"
print(txt.format(price=49.009978))

print(f"for only {29.00923:.3f} dollars")