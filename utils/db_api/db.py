import sqlite3  # Импортируем модуль для работы с базой данных SQLite
from aiogram.fsm.context import FSMContext  # Импортируем контекст для управления состояниями FSM

# Класс для работы с основной базой данных
class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):   
        return sqlite3.connect(self.path_to_db)  # Метод возвращает соединение с базой данных

    # Метод для выполнения SQL-запросов
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()  # Создаем курсор для выполнения запросов
        data = None
        cursor.execute(sql, parameters)  # Выполняем SQL-запрос с параметрами
        if commit:
            connection.commit()  # Если установлен флаг commit, фиксируем изменения в базе данных
        if fetchall:
            data = cursor.fetchall()  # Если установлен флаг fetchall, получаем все строки результата
        if fetchone:
            data = cursor.fetchone()  # Если установлен флаг fetchone, получаем одну строку результата
        connection.close()  # Закрываем соединение с базой данных
        return data  # Возвращаем результат выполнения запроса

    # Метод для создания таблицы USERS
    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS USERS(
        full_name TEXT,
        telegram_id INTEGER unique );
              """
        self.execute(sql, commit=True)  # Выполняем SQL-запрос для создания таблицы

    # Вспомогательный метод для форматирования аргументов SQL-запроса
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    # Метод для добавления пользователя в таблицу USERS
    def add_user(self, telegram_id:int, full_name:str):
        sql = """
        INSERT INTO Users(telegram_id, full_name) VALUES(?, ?);
        """
        self.execute(sql, parameters=(telegram_id, full_name), commit=True)  # Выполняем SQL-запрос для добавления пользователя

    # Методы для выборки данных из таблицы USERS
    def select_all_users(self):
        sql = """
        SELECT * FROM Users;
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE;"
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    # Метод для подсчета количества пользователей в таблице USERS
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    # Метод для удаления всех записей из таблицы USERS
    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE;", commit=True)

    # Метод для выборки всех telegram_id пользователей
    def all_users_id(self):
        return self.execute("SELECT telegram_id FROM Users;", fetchall=True)

# Класс для работы с базой данных ответов пользователей
class AnswersDatabase:
    def __init__(self, path_to_db="answers.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)  # Метод возвращает соединение с базой данных

    # Метод для выполнения SQL-запросов
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()  # Создаем курсор для выполнения запросов
        data = None
        cursor.execute(sql, parameters)  # Выполняем SQL-запрос с параметрами
        if commit:
            connection.commit()  # Если установлен флаг commit, фиксируем изменения в базе данных
        if fetchall:
            data = cursor.fetchall()  # Если установлен флаг fetchall, получаем все строки результата
        if fetchone:
            data = cursor.fetchone()  # Если установлен флаг fetchone, получаем одну строку результата
        connection.close()  # Закрываем соединение с базой данных
        return data  # Возвращаем результат выполнения запроса

    # Метод для создания таблицы ANSWERS
    def create_table_user_answers(self):
        sql = """
        CREATE TABLE IF NOT EXISTS ANSWERS(
            full_name TEXT,
            telegram_id INTEGER unique,
            count INTEGER unique
        );
        """
        return self.execute(sql, commit=True)  # Выполняем SQL-запрос для создания таблицы

    # Метод для добавления ответов пользователя в таблицу ANSWERS
    def add_user_answers(self, telegram_id:int, full_name:str, count:int):
        sql = """
        INSERT INTO ANSWERS(telegram_id, full_name, count) VALUES(?, ?, ?);
        """
        self.execute(sql, parameters=(telegram_id, full_name, count), commit=True)  # Выполняем SQL-запрос для добавления ответов пользователя

    # Метод для подсчета количества записей (пользователей) в таблице ANSWERS
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM ANSWERS;", fetchone=True)
