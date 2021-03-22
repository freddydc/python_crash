
""" Notas:
        int()
        float()
        bool()
"""
def first():
    birth = input('Your birth year: ')
    print(type(birth))
    age = 2021 - int(birth)
    print(type(age))
    print(age)

# first()

def lbs_kg():
    weight_lbs = input('weight to (lbs): ')
    weight_kg = int(weight_lbs) * 0.45
    print(str(weight_kg) + ' Kg')

# lbs_kg()

my_bool = 'freddy'
print(bool(my_bool))

course = 'Space for Navigation'
print(course[6:])
