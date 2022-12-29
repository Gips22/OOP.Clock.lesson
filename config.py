"""Все приватные переменные заданы тут. При подключении к проекту - создать файл .env,
внести его в .gitignore и задать там переменные окружения"""
import os

from dotenv import load_dotenv


load_dotenv()

PASSWORD = os.getenv("PASSWORD")
