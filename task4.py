def age (dog_age):
    if dog_age <= 2:
        human_age = dog_age * 10.5
    else:
        human_age = 2 * 10.5 + (dog_age - 2) * 4
    print(human_age)
age(23)