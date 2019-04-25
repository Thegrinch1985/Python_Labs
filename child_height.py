# convert feet and inches to centimetres
def feet_inches_to_inches(feet, inches):
    total_inches = feet * 12 + inches
    return total_inches

print (feet_inches_to_inches(6, 0))

# gender
from enum import Enum
class Gender(Enum):
    MALE = 1
    FEMALE = 2

# predict child height in inches
def child_height(father_height, mother_height, gender):
    prediction = (father_height + mother_height) / 2
    if gender == Gender.MALE:
        prediction = prediction + 5
    else:
        prediction = prediction - 5
    return int(round(prediction * 2.54,0))

print (child_height(72, 65, Gender.MALE))
print (child_height(70, 62, Gender.FEMALE))


# parents
parents = [{'gender': Gender.MALE, 'feet': 6, 'inches': 0}, {'gender': Gender.FEMALE,'feet': 5, 'inches': 5} ]

# extract heights in centimetres and print
heights = map(lambda p: feet_inches_to_inches(p['feet'], p['inches']) * 2.54, parents)
heights = list(heights)
print (heights)

# predict height for boy and girl
print (child_height(heights[0] * 0.39, heights[1] * 0.39, Gender.FEMALE))
print (child_height(heights[0] * 0.39, heights[1] * 0.39, Gender.MALE))
