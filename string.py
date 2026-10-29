str1 = "vaibhav shffakj%^fhfk"

print ("1+2*3")
print("5"+"8") # concatination

message = "Din't worry about errors."
print(message)

dialogue = 'She said "Python is amazing".'

# escape siqence characters

message = 'Don\'t worry about errors.' #\\\\
print(message)

dialogue = 'She said - \n"Python is amazing".' # new line
print(dialogue)

message = 'Don\'t worry \tabout errors.' # tab
print(message)

print("C:\\Users\\Vipul\\Documents")


city = "New York"
temp = 75
weather_report = "Temperature of"+ " " + city + " " + "is"+ " " + str(temp) + " " + "degrees."
print(weather_report)

# ---------------f string------------------

weather_report = f"The Temperature in {city} is {temp} degrees"
print(weather_report)


print("py"*2 + "thon"*2)