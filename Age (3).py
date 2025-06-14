try:
    current_year = int(input('Enter the current year: '))
    yoyb = int(input('Enter the year of your birth: '))
    if current_year > yoyb:
        age = current_year-yoyb
        print(f"you're {age} years old.")
    else:
        print('impossible...')
except:
    print('Enter integers')