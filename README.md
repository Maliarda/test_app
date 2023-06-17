### Установка Poetry

Если у вас уже установлен Poetry, вы можете перейти к следующему разделу. 
В противном случае, следуйте инструкциям ниже, чтобы установить Poetry.

```
curl -sSL https://install.python-poetry.org | python3 -
```

Дополнительные способы установки можно найти в [Официальной документации Poetry](https://python-poetry.org/docs/)

### Установка зависимостей проекта
После установки Poetry, перейдите в каталог проекта и выполните 
следующую команду для установки зависимостей:

```
poetry install
```

Эта команда прочитает файл pyproject.toml, который содержит список зависимостей проекта, 
и создаст виртуальное окружение для проекта, в котором будут установлены все зависимости.

### Активация виртуального окружения
После успешной установки зависимостей, активируйте виртуальное окружение проекта 
с помощью команды:

```
poetry shell
```

### Управление зависимостями
Для управления зависимостями, используйте команды Poetry, такие как add, remove, update и др. 
Например:

Добавление зависимости:

```
poetry add <package-name>
```

### Применение миграций
Перед запуском проекта, необходимо применить миграции базы данных. 
Выполните следующую команду:

```
python manage.py migrate
```

### Создание базы
Возможно с помощью [PGAdmin](https://info-comp.ru/install-pgadmin-4-on-windows-10#nastroyka-podklyucheniya-k-postgresql) или DBeaver

### Настройка переменных окружения
1. Создать файл `.env` в корне проекта

2. Записать в этот файл следующее: 

```
POSTGRES_DB=тут_ваше_название_БД_какую_создали_на_предыдущем_шаге
POSTGRES_USER=тут_ваш_пользователь_БД
POSTGRES_PASSWORD=тут_ваш_пароль_от_БД
POSTGRES_HOST=localhost  
POSTGRES_PORT=5432
SECRET_KEY=тут_ваш_секретный_ключ
```

### Применение миграций

```
python manage.py makemigrations
python manage.py migrate 
```

### Запуск сервера

```
poetry run python manage.py runserver
```

### Документация доступна по адресам:
[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

[http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)