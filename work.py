import pyodbc


class User:
    def __init__(self):
        self.id = 0
        self.login = ""
        self.password = ""
        self.email = ""
        self.role = 0
        #self.unemployed = Unemployed()
        #self.hirer = Hirer()

    def log_in(self):
        print("Введите логин")
        self.login = input()
        print("Введите пароль")
        self.password = input()
        print("Введите почту")
        self.email = input()
        print("Выберите роль")
        self.role = int(input())
        cursor.execute("""INSERT INTO Users (login, password, email, roleId) 
                          VALUES (?, ?, ?, ?)""", (self.login, self.password, self.email, self.role))
        conn.commit()
        res = cursor.execute('SELECT id FROM Users WHERE login =? AND password =?', (self.login, self.password))
        result = res.fetchone()
        self.id = result[0]
        if self.role == 1:
            print("Введите Фамилию")
            last_name = input()
            print("Введите Имя")
            name = input()
            print("Введите Отчество")
            middle_name = input()
            print("Введите Дату рождения в формате YYYY-MM-DD")
            date_of_birthday = input()
            print("Введите телефон")
            telephone = input()
            print("Введите название университета")
            university_name = input()
            print("Введите специальность")
            specialty = input()
            print("Введите год начала обучения в формате YYYY")
            start_year = input()
            print("Введите год окончания обучения в формате YYYY")
            end_year = input()
            self.unemployed = Unemployed(last_name, name, middle_name, date_of_birthday, telephone)
            cursor.execute("""INSERT INTO Unemployed 
                              (userId, lastName, name, middleName, dateOfBirthday, telephone, universityName, specialty, startYear, endYear) 
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                              (self.id, last_name, name, middle_name, date_of_birthday, telephone, university_name, specialty, start_year, end_year))
            conn.commit
        elif self.role == 2:
            print("Введите Наименование компании")
            name = input()
            print("Расскажите кратко о компании")
            about_company = input()
            print("Введите телефон")
            telephone = input()
            self.hirer = Hirer(name, about_company, telephone)
            cursor.execute("""INSERT INTO Hirer 
                              (userId, companyName, aboutCompany, telephone) 
                              VALUES (?, ?, ?, ?)""",
                              (self.id, name, about_company, telephone))
            conn.commit
        cursor.close()

    #вход
    def log_up(self):
        while True:
            print("Введите логин")
            login = input()
            print("Введите пароль")
            password = input()

            res = cursor.execute('SELECT * FROM Users WHERE login =? AND password =?', (login, password))
            result = res.fetchone()
            if result:
                self.id = result[0]
                self.login = result[1]
                self.password = result[2]
                self.email = result[3]
                self.role = result[4]
                if self.role == 1:
                    res = cursor.execute('SELECT * FROM Unemployed WHERE userId =?', self.id)
                    result = res.fetchone()
                    last_name = result[2]
                    name = result[3]
                    middle_name = result[4]
                    date_of_birthday = result[5]
                    telephone = result[6]
                    self.unemployed = Unemployed(last_name, name, middle_name, date_of_birthday, telephone)
                else:
                    res = cursor.execute('SELECT * FROM Hirer WHERE userId =?', self.id)
                    result = res.fetchone()
                    name = result[2]
                    about_company = result[3]
                    telephone = result[4]
                    self.hirer = Hirer(name, about_company, telephone)
                cursor.close()
                break
            else:
                print("Такого пользователя не существует. Введите корректные данные.")


    def exit(self):
        pass


class Unemployed:
    # def __init__(self):
    #     self.last_name = ""
    #     self.name = ""
    #     self.middle_name = ""
    #     self.date_of_birthday = ""
    #     self.telephone = ""

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
        resume = Document(type_education, city, position, experience, knowledge_of_english, work_schedule, about_self,
                          1)

    def update_resume(self):
        pass


class Hirer:
    # def __init__(self):
    #     self.name = ""
    #     self.about_company = ""
    #     self.telephone = ""


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
        resume = Document(type_education, city, position, experience, knowledge_of_english, work_schedule, about_self,
                          2)

    def update_vacancy(self):
        pass


class Document:
    def __init__(self, type_education, city, position, experience, knowledge_of_english, work_schedule, about_self,
                 document_type):
        self.type_education = type_education
        self.city = city
        self.position = position
        self.experience = experience
        self.knowledge_of_english = knowledge_of_english
        self.work_schedule = work_schedule
        self.about_self = about_self
        self.document_type = document_type


if __name__ == '__main__':
    user = User()
    conn = pyodbc.connect(driver='{SQL Server}',
                          server='DESKTOP-UP524EV', database='EmploymentCenter',
                          trusted_connection='yes', autocommit=True)

    cursor = conn.cursor()

    print("Если вы зарегестрированы, то введите 1, чтобы войти.")
    print("Если вы не зарегестрированы, то введите 2, чтобы войти.")
    choice = int(input())
    if choice == 1:
        user.log_up()
    elif choice == 2:
        user.log_in()
    # print(user.login)
    # print(user.password)
    # print(user.role)
    if user.role == 1:
        employee = user.unemployed
        print(employee.last_name)
        print(employee.name)
        print(employee.middle_name)
        print(employee.date_of_birthday)
        print(employee.telephone)
    else:
        hirer = user.hirer
        print(hirer.name)
        print(hirer.about_company)
        print(hirer.telephone)