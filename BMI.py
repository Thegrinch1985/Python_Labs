
# height = metres
# weight = kilogram
def calculate_bmi(weight, height):
	bmi = float(weight/(height * height))
	return round(bmi,2)
    
print("Your body mass index is:",calculate_bmi(85, 5.8))


def calculate_bmi_cat(bmi):
	if(bmi <= 18.4):
		category = "Underweight"
	elif(bmi <= 24.9):
		category = "Normal"
	elif(bmi <= 29.9):
		category = "Overweight"
	elif(bmi >= 30):
		category = "Obese"
	else:
		print("Invalid bmi")
	return category

print(calculate_bmi_cat(18.0))
print(calculate_bmi_cat(22.8))
print(calculate_bmi_cat(25.2))
print(calculate_bmi_cat(30.3))

# convert weight in stones and pounds into kgs
def convert_weight(s, p):
	st = p * 0.0714286
	stones = st + s
	kilograms = stones * 6.35029
	return kilograms

print(convert_weight(1,1))

def convert_height(f, i):
	he = i * 0.0833333
	height = he + f
	metres = height * 0.3048
	return metres

print(convert_height(5,6))

# Dictionary
person = { "feet":6, "inches":0 }

# Calculate BMI & 
print(calculate_bmi(convert_weight(13,0), convert_height(person["feet"], person["inches"])))

# Calculate BMI Category
print(calculate_bmi_cat(calculate_bmi(convert_weight(13,0), convert_height(person["feet"], person["inches"]))))

# add new key to dictionary to store a list of weights
# used to track a person over time
person2 = { "weights" : [[10,5], [11,0], [10,9]] }
person.update(person2)

# calculate bmis for each of the weights for the person
bmis = list(map(lambda weight: calculate_bmi(convert_weight(weight[0], weight[1]), 
											 convert_height(person["feet"], person["inches"])), person["weights"]))
print(bmis)

# Calculate category for each of the weights
categories = list(map(lambda bmi: calculate_bmi_cat(bmi), bmis))
print(categories)
