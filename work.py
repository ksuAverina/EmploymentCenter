class User:
    def __init__(self):
        self.login = ""
        self.password = ""
        self.email = ""
        self.role = 0;

    def log_in(self):
        print("Введите логин")
        self.login = input()
        print("Введите пароль")
        self.password = input()
        print("Введите почту")
        self.email = input()
        print("Выберите роль")
        self.role = int(input())
        if self.role == 1:
            print("Введите Фамилию")
            last_name = input()
            print("Введите Имя")
            name = input()
            print("Введите Отчество")
            middle_name = input()
            print("Введите Дату рождения в формате MM/DD/YY")
            date_of_birthday = input()
            print("Введите телефон")
            telephone = input()
            unemployed = Unemployed(last_name, name, middle_name, date_of_birthday, telephone)
        elif self.role == 2:
            print("Введите Наименование компании")
            name = input()
            print("Расскажите кратко о компании")
            about_company = input()
            print("Введите телефон")
            telephone = input()
            hirer = Hirer(name, about_company, )

    def log_up(self, login, password):
        pass

    def exit(self):
        pass


class Unemployed:
    def __init__(self, last_name, name, middle_name, date_of_birthday, telephone):
        self.last_name = last_name
        self.name = name
        self.middle_name = middle_name
        self.date_of_birthday = date_of_birthday
        self.telephone = telephone


    def create_resume(self):
        print("Введите уровень вашего образования")
        type_education = input()
        print("Введите город")
        city = input()
        print("Введите желаемую позицию")
        position = input()
        print("Введите опыт работы")
        experience = input()
        print("Введите ваш уровень знаний английского языка")
        knowledge_of_english = input()
        print("Введите график работы")
        work_schedule = input()
        print("Напишите о себе")
        about_self = input()
        resume = Document(type_education, city, position, experience, knowledge_of_english, work_schedule, about_self, 1)


    def update_resume(self):
        pass


class Hirer:
    def __init__(self, name, about_company, telephone):
        self.name = name
        self.about_company = about_company
        self.telephone = telephone

    def create_vacancy(self):
        print("Введите уровень желаемого образования")
        type_education = input()
        print("Введите город")
        city = input()
        print("Введите должность")
        position = input()
        print("Введите требуемый опыт работы")
        experience = input()
        print("Введите требуемый уровень знаний английского языка")
        knowledge_of_english = input()
        print("Введите график работы")
        work_schedule = input()
        print("Напишите дополнительно о вакансии")
        about_self = input()
        resume = Document(type_education, city, position, experience, knowledge_of_english, work_schedule, about_self, 2)


    def update_vacancy(self):
        pass


class Document:
    def __init__(self, type_education, city, position, experience, knowledge_of_english, work_schedule, about_self, document_type):
        self.type_education = type_education
        self.city = city
        self.position = position
        self.experience = experience
        self.knowledge_of_english = knowledge_of_english
        self.work_schedule = work_schedule
        self.about_self = about_self
        self.document_type = document_type


user1 = User()
user1.log_in()
print(user1.login)
print(user1.password)
print(user1.email)