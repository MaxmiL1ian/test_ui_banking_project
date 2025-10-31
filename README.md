# test_ui_banking_project
Этот проект содержит автоматизированный UI тесты для формы BankingProject. Тест выполняет следующие проверки:
*   Добавление пользователя; 
*   Сортировка пользователей по именам; 
*   Удаление пользователя.

## 📌 Содержание

*   [Требования](#-требования)
*   [Установка](#-установка)
*   [Запуск теста](#-запуск-теста) 
*   [Просмотр результатов](#-Просмотр-результатов)

## 🔧 Требования

*   Python 3.12 
*   Google Chrome (последняя версия)
*   Git (для клонирования репозитория)

## 🚀 Установка

1.  Клонируйте репозиторий:

    ```bash
    git clone https://github.com/MaxmiL1ian/test_ui_banking_project.git
    ```

2.  Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv .venv
    # Для Windows:
    .venv\Scripts\activate
    # Для Linux/macOS:
    source .venv/bin/activate
    ```

3.  Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## ⚡ Запуск теста

Выполните команду:

```bash
pytest tests/test_banking_project.py --alluredir=./allure-results
```

Также проект поддерживает параллельный запуск тестов:

```bash
pytest -n auto --alluredir=./allure-results tests/test_banking_project.py
```
## 🔎 Просмотр результатов

Выполните команду:

```bash
allure serve  (Путь до директории)/allure-results
```