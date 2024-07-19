# API Weather App

## Описание

API Weather app - это веб-приложение, которое предоставляет информацию о погоде в разных городах.

---

Оно предоставляет возможность:

- Сохранения истории запросов у каждого пользователя
- Обращения к внешнему API сайта для получения информации о количестве запросов для разных городов

Примечание:
- написаны тесты
- всё это помещено в докер контейнер
- при повторном посещении сайта будет предложено посмотреть погоду в городе, в котором пользователь уже смотрел ранее
- будет сохраняться история поиска для каждого пользователя, и будет API, показывающее сколько раз вводили какой город


## Стек технологий

- **Backend**: FastAPI (Python)
- **База данных**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Тестирование**: httpx, pytest
- **Контейнеризация**: Docker

## Установка и запуск

### Установка приложения

1. Клонируйте репозиторий:
    
    ```sh
    git clone https://github.com/kenniele/api-weather-app.git
   ```

2. Перейдите в директорию проекта:

   ```sh
   cd api-weather-app
   ```

### Запуск приложения с Docker

1. Создайте Docker-образ и запустите контейнер:

   ```sh
   docker-compose up --build
   ```

2. Откройте браузер и перейдите по адресу:

   ```sh
   http://localhost:8000
   ```
   
### Запуск приложения без Docker

1. Создайте и активируйте виртуальное окружение:

   ```sh
   python -m venv venv
   source venv/bin/activate # Для Windows используйте venv\Scripts\activate
   ```

2. Установите зависимости:

   ```sh
   pip install -r requirements.txt
   ```

3. Запустите файл main.py:

   ```sh
   python.exe src/main.py
   ```

4. Откройте браузер и перейдите по адресу:

   ```sh
   http://localhost:8000
   ```

## Использование

- Введите название города в поле ввода
- Нажмите на кнопку "Получить погоду"
- Информация о запросе отобразиться на главной странице

## API

### Получение информации о городе

- **URL**: `/info/{city}`
- **Метод**: `GET`
- **Параметры**:
  - `city` - название города
- **Ответ (пример)**:
  ```json
  {
    "city": "Moscow",
    "count": 5
  }
  ```
