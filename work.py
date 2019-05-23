import pyodbc


class User:

    def __init__(self):
        self.id = 0
        self.login = ""
        self.password = ""
        self.email = ""
        self.role = 0

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

            cursor.execute("""INSERT INTO Unemployed 
                              (userId, lastName, name, middleName, dateOfBirthday, telephone, universityName, specialty, startYear, endYear) 
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                              (self.id, last_name, name, middle_name, date_of_birthday, telephone, university_name, specialty, start_year, end_year))
            conn.commit

            res = cursor.execute("SELECT TOP 1 id FROM Unemployed ORDER BY id DESC")
            result = res.fetchone()
            emp_id = result[0]

            self.unemployed = Unemployed(emp_id, last_name, name, middle_name, date_of_birthday, telephone)

        elif self.role == 2:
            print("Введите Наименование компании")
            name = input()

            print("Расскажите кратко о компании")
            about_company = input()

            print("Введите телефон")
            telephone = input()

            cursor.execute("""INSERT INTO Hirer 
                              (userId, companyName, aboutCompany, telephone) 
                              VALUES (?, ?, ?, ?)""",
                              (self.id, name, about_company, telephone))
            conn.commit

            res = cursor.execute("SELECT TOP 1 id FROM Hirer ORDER BY id DESC")
            result = res.fetchone()
            hir_id = result[0]

            self.hirer = Hirer(hir_id, name, about_company, telephone)

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
                    emp_id = result[0]
                    last_name = result[2]
                    name = result[3]
                    middle_name = result[4]
                    date_of_birthday = result[5]
                    telephone = result[6]
                    self.unemployed = Unemployed(emp_id, last_name, name, middle_name, date_of_birthday, telephone)

                else:
                    res = cursor.execute('SELECT * FROM Hirer WHERE userId =?', self.id)
                    result = res.fetchone()
                    hir_id = result[0]
                    name = result[2]
                    about_company = result[3]
                    telephone = result[4]
                    self.hirer = Hirer(hir_id, name, about_company, telephone)
                break
            else:
                print("Такого пользователя не существует. Введите корректные данные.")

    def exit(self):
        cursor.close()


class Unemployed:

    def __init__(self, id, last_name, name, middle_name, date_of_birthday, telephone):
        self.id = id
        self.last_name = last_name
        self.name = name
        self.middle_name = middle_name
        self.date_of_birthday = date_of_birthday
        self.telephone = telephone

    def create_resume(self):
        print("Введите уровень вашего образования")
        type_education = int(input())
        print("Введите город")
        city = input()
        print("Введите желаемую позицию")
        position = input()
        print("Введите опыт работы")
        experience = int(input())
        print("Введите ваш уровень знаний английского языка")
        knowledge_of_english = int(input())
        print("Введите график работы")
        work_schedule = int(input())
        print("Напишите о себе")
        about_self = input()

        self.resume = Document(type_education, city, position, experience, knowledge_of_english, work_schedule, about_self,
                          1)
        cursor.execute("""INSERT INTO Document
                          (typeEducation, city, position, experience, knowledgeOfEnglish, workSchedule, aboutSelf, typeDocument) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                         (type_education, city, position, experience, knowledge_of_english, work_schedule, about_self, 1))
        conn.commit()

        res = cursor.execute("SELECT TOP 1 id FROM Document ORDER BY id DESC")
        result = res.fetchone()
        resumeId = result[0]
        cursor.execute("UPDATE Unemployed SET resumeId = ? WHERE id = ?", (resumeId, self.id))
        conn.commit()

    def update_resume(self):
        pass


class Hirer:

    def __init__(self, id, name, about_company, telephone):
        self.id = id
        self.name = name
        self.about_company = about_company
        self.telephone = telephone

    def create_vacancy(self):
        print("Введите уровень желаемог о образования")
        type_education = int(input())

        print("Введите город")
        city = input()

        print("Введите должность")
        position = input()

        print("Введите требуемый опыт работы")
        experience = int(input())

        print("Введите требуемый уровень знаний английского языка")
        knowledge_of_english = int(input())

        print("Введите график работы")
        work_schedule = int(input())

        print("Напишите дополнительно о вакансии")
        about_self = input()

        cursor.execute("""INSERT INTO Document
                          (typeEducation, city, position, experience, knowledgeOfEnglish, workSchedule, 
                          aboutSelf, typeDocument) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                          (type_education, city, position, experience, knowledge_of_english, work_schedule,
                           about_self, 2))
        conn.commit

        self.resume = Document(type_education, city, position, experience, knowledge_of_english, work_schedule, about_self, 2)

        res = cursor.execute("SELECT TOP 1 id FROM Document ORDER BY id DESC")
        result = res.fetchone()
        vacancyId = result[0]
        cursor.execute("INSERT INTO VacancyCompany (hirerId, vacancyId) VALUES (?, ?)", (self.id, vacancyId))
        conn.commit()

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


if __name__ == '__main__':
    user = User()
    conn = pyodbc.connect(driver='{SQL Server}',
                          server='DESKTOP-UP524EV', database='EmploymentCenter',
                          trusted_connection='yes', autocommit=True)

    cursor = conn.cursor()

    print("Если вы зарегестрированы, то введите 1, чтобы войти.")
    print("Если вы не зарегестрированы, то введите 2, чтобы зарегестрироваться.")
    choice = int(input())
    if choice == 1:
        user.log_up()
    elif choice == 2:
        user.log_in()

    if user.role == 1:
        employee = user.unemployed
        print(employee.last_name)
        print(employee.name)
        print(employee.middle_name)
        print(employee.date_of_birthday)
        print(employee.telephone)

        employee.create_resume()
    else:
        hirer = user.hirer
        print(hirer.name)
        print(hirer.about_company)
        print(hirer.telephone)

        hirer.create_vacancy()