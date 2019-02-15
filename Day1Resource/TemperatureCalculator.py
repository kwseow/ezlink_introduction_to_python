name = input("Enter patient's name:")
temperature = float(input("Enter patient's temperature:"))
norm_temp=36.9
print("%s's temperature is %.1f degree celsius from %.1f." %(name,temperature-norm_temp, norm_temp))