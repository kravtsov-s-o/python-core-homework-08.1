from datetime import date, datetime


def get_birthdays_per_week(users):
    weekends = ['Saturday', 'Sunday']
    birthdays_per_week = dict()
    current_date = date.today()

    if not users:
        return birthdays_per_week

    for user in users:
        name = user['name']
        birthday = user['birthday']

        if birthday.year < current_date.year:
            birthday = birthday.replace(year=current_date.year + 1)

        if birthday < current_date:
            continue

        birthday_weekday = birthday.strftime('%A')

        if birthday_weekday in weekends:
            birthday_weekday = 'Monday'

        birthdays_per_week.setdefault(birthday_weekday, []).append(name)

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
