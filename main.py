import re

# при запуске программы и при выборе соответствующего пункта меню функция display_entries_per_page открывает
# файл database.txt, считывает записи из него и выводит постранично на экран с помощью функции
# Пользователю предлагается нажимать Enter для просмотра следующей страницы или вводить q для выхода из отображения записей.

# В случае отсутствия записей в файле будет выведено сообщение "Нет записей в файле".
def display_entries_per_page(entries, page_num, per_page=5):
    start_index = (page_num - 1) * per_page
    end_index = min(start_index + per_page, len(entries))

    for entry in entries[start_index:end_index]:
        print(", ".join(entry))


file_name = "database.txt"

with open(file_name, "r") as file:
    entries = [line.strip().split(", ") for line in file]

if not entries:
    print("Нет записей в файле.")
else:
    page_num = 1
    per_page = 5

    while True:
        print(f"Страница {page_num}:")
        display_entries_per_page(entries, page_num, per_page)

        user_input = input("Нажмите Enter для продолжения или 'q' для выхода: ")
        if user_input.lower() == 'q':
            break

        page_num += 1

#при выборе соответствующего пункта меню добавляем новый контакт в список
def add_contact():
    with open("database.txt", "a") as file:
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        organization = input("Введите название организации: ")
# при помощи регулярных выражений проверяем рабочий номер телефона на валидность
        while True:
            work_phone = input("Введите телефон рабочий: ")
            result_work_phone = re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                              work_phone)
            if bool(result_work_phone) == False:
                print("Вы ввели не корректный номер. Попробуйте снова: ")
            else:
# при помощи регулярных выражений проверяем личный номер телефона на валидность
                while True:
                    personal_phone = input("Введите телефон личный: ")
                    result_personal_phone = re.match(
                        r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                        personal_phone)
                    if bool(result_personal_phone) == False:
                        print("Вы ввели не корректный номер. Попробуйте снова: ")
                    else:
                        new_contact = f"{surname},{name},{middle_name},{organization},{work_phone},{personal_phone}\n"
                        file.write(new_contact)
                        print("Запись добавлена успешно.\n")
                        break
                break


# при выборе соответствующего пункта меню находим нужную запись редактируем её
def edit_contact():
    contact_number = input("Введите номер записи для редактирования: ")
    with open("database.txt", "r") as file:
        lines = file.readlines()

    if int(contact_number) <= len(lines):
        field_to_edit = input(
            "Выберите поле для редактирования (1 - Фамилия, 2 - Имя, 3 - Отчество, 4 - Название организации, 5 - Телефон рабочий, 6 - Телефон личный): ")
        new_value = input(f"Введите новое значение для поля {field_to_edit}: ")

        contact = lines[int(contact_number) - 1].split(",")
        contact[int(field_to_edit) - 1] = new_value
        lines[int(contact_number) - 1] = ",".join(contact) + "\n"

        with open("database.txt", "w") as file:
            file.writelines(lines)
        print("Запись успешно отредактирована.\n")
    else:
        print("Неверный номер записи.\n")


# при выборе соответствующего пункта меню находим нужный контакт по фамилии
def search_contact():
    search_query = input("Введите фамилию для поиска: ")
    with open("database.txt", "r") as file:
        for line in file:
            contact = line.split(",")
            if search_query in contact:
                print(", ".join(contact))
        print()

# выводим меню на экран
while True:
        print("\nМеню:")
        print("1. Добавить новую запись")
        print("2. Редактировать запись")
        print("3. Поиск записи")
        print("4. Вывести записи постранично")
        print("5. Выйти\n")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
             display_entries_per_page(entries, page_num, per_page=5)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.\n")
