# Blogicum

Социальная сеть, небольшой сервис микроблогов, где пользователи могут создавать посты, взаимодействовать с ними и читать посты других пользователей

## Функционал сайта

- Незарегистрированный пользователь имеет возможность создать аккаунт или войти в уже существующий. Так же ему доступна лента новостей и просмотр аккаунтов зарегистрированных пользователей.

- Каждый зарегистрированный пользователь имеет свою страницу профиля, где отображаются указанная им информация, дата регистрации и посты. Автор может задать и изменить пароль, имя и уникальный адрес для своей страницы. На странице автор видит все свои посты, другим пользователям видны только активные посты с датой публикации не позднее настоящей.

- Для каждого поста существует категория, дата публикации, а так же опционально можно указать локацию, с которой связан пост. Если поставить дату публикации в будущем, запить не будет видна другим пользователям до наступления указанной даты.

- Автор может изменить и удалить свой пост. Изменить можно всю информацию о посте, включая дату публикации.

- Каждая категория имеет свою страницу с описанием контента и постами, опубликованными по данной категории.

- Пользователи могут читать посты других авторов в общей ленте постов на главной странице, на страницах категорий и на личных страницах других пользователей. Для отображение полного текста поста, нужно зайти на его страницу.

- Пользователи могут оставлять комментарии к постам. Комментарии можно оставлять как к своим, так и к чужим постам. Автор может редактировать и удалять свои комментарии.

- Так же на сайте есть статические страницы с описанием проекта и правилами пользования блогом.

В проекте реализована админ-зона с полным набором функций для модерации контента.
Проект покрыт тестами по всем эндпоинтам.


## Технологии

- Python
- Django
- Djangorestframework
- HTML
- Bootstrap5
- SQLite3



## Установка и запуск

Клонировать репозиторий:
```
git clone <https or SSH URL>
```

Перейти в папку проекта:
```
cd blogicum
```

Создать и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```

Обновить pip:
```
python -m pip install --upgrade pip
```

Установить библиотеки:
```
pip install -r requirements.txt
```

Создать и выполнить миграции:
```
python blogicum/manage.py makemigrations
python blogicum/manage.py migrate
```

Загрузить фикстуры DB:
```
python blogicum/manage.py loaddata db.json
```

Создать суперпользователя:
```
python blogicum/manage.py createsuperuser
```

Запустить сервер django:
```
python blogicum/manage.py runserver
```

Проект будет доступен по адресу: http://127.0.0.1:8000/

Админ-зона по адресу: http://127.0.0.1:8000/admin/

  
## Автор проекта
[Ксения Тетерчева](https://github.com/GreenVibesOnly/) 🌿
