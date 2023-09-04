# Учебный проект GoIT - домашнее задание

## Задание
Вам нужно реализовать функцию для вывода списка коллег, которых нужно поздравить с днем рождения в неделю.

У вас есть список словарей users, каждый в нем обязательно имеет ключи `name` и `birthday`.
Такая структура представляет модель списка пользователей с их именами и днями рождения.
Где:
- `name` – это строка с именем пользователя
- `birthday` – это `datetime.date` объект, в котором записан день рождения.

### Пример:

```{"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()}```

Ваша задача написать функцию `get_birthdays_per_week`, которая получает на вход список `users` и возвращает словарь пользователей, которых нужно поздравить по дням на следующей неделе.

Формат словаря, возвращающий функция `get_birthdays_per_week` у нас будет следующим:

```{'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}```

Ключи словаря это дни недели: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday".
Значение это списки пользователей с днями рождения в неделю вперед от текущего дня, включая текущий день.

### Примечание
> Например, если я запускаю скрипт в среду, то в ключах "Wednesday", "Thursday", "Friday"
> дни рождения этой недели, а в ключах "Monday", "Tuesday" сохраняются дни рождения на следующей неделе.
> В ключе "Monday" всегда дни рождения этой недели пришедшиеся на выходные.

### Критерии оценивания:
- Код должен быть чистым и соблюдать стандарты PEP 8.
– Функция должна корректно обрабатывать все дни недели.
- функция должна корректно учитывать выходные дни и переносить их на понедельник.
- Функция должна учитывать случаи, когда день рождения уже истек в этом году.
- функция должна корректно работать с пустым списком пользователей.
– Функция должна корректно учитывать ситуации, когда все дни рождения уже прошли в этом году.
- Файл с домашним заданием: `main.py` имеет импорт `from datetime import date`
- Для определения какая сегодня дата используется только `date.today()`
- Неделя начинается с понедельника

Чтобы проверить правильность выполнения функции `get_birthdays_per_week`,
вам нужно запустить файл `check_homework.py`, проверяющий пять основных тестовых случаев,
для вашей реализации функции `get_birthdays_per_week`:

- Тест, когда все дни рождения пользователей есть в будущем и не бросаются на выходные.
- тест когда дни рождения некоторых пользователей выпадают на выходные.
- Тест, когда некоторые дни рождения пользователей уже прошли в этом году.
- тест когда в списке нет пользователей.
- Тест, когда все дни рождения пользователей уже прошли в этом году.