def life_in_weeks(age):
    days_in_year = 364
    day_in_week = 7
    life_expectancy = 90
    total_weeks = round((life_expectancy - age) * days_in_year / day_in_week)
    print(f"You have {total_weeks} weeks left")
    
life_in_weeks(20)
    