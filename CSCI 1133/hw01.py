
import platform

vers = platform.python_version()
assert vers[0] == '3', "You must use Python 3, "+vers+" is not acceptable"
print("Python 3 confirmed.")


num_cookies = int(input("How many cookies do you want to make? "))
recipe_mult = num_cookies/12
butter = str(125*recipe_mult)+"g butter"
sugar = str(225*recipe_mult)+"g sugar"
eggs = str(max(1,round(recipe_mult)))+" eggs"
vanilla = str(recipe_mult)+" tsp vanilla extract"
flour = str(225*recipe_mult)+"g flour"
salt = str(0.5*recipe_mult)+" tsp salt"
chips = str(200*recipe_mult)+"g chocolate chips"

print("num_cookies is", num_cookies)
print("recipe_mult is", recipe_mult)


print(butter)
print(sugar)
print(eggs)
print(vanilla)
print(flour)
print(salt)
print(chips)


amt = float(input("Enter the loan amount in dollars: "))
n = int(input("Enter the loan duration in months: "))
r = int((input("Enter the annual interest rate: ")))
r = r/100/12
payment = (r*amt)/(1-(1+r)**(-n))
print("Your monthly payment is: " + str(round(payment,2)))


# Office Hours (leave these lines commented out, this isn't Python code)
# Name of the TA who you visited in office hours: I VISITED EMILY WELP
# Above TA's favorite color: HER FAVORITE COLOR IS PINK
