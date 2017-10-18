```
Используется микрофреймворк Flask.
Реализован простой RESTful web-сервис:

- POST /books/api/v1.0/book  - создает объект 'книга';
- GET /books/api/v1.0/book - возвращает массив объектов 'книга';
- PUT /books/api/v1.0/make_slug/<id> -  создает SLUG-ссылку для 'книги' по ID;
- GET /books/api/v1.0/get_book/<slug> - возвращает 'книгу' по заданному slug


Примеры:
curl -i -H "Content-Type: application/json" \
    -X POST -d '{"title": "рассказы Васи Пупкина", "author": "Вася Пупкин", "description": "Рассказы Васи Пупкина о себе."}' \
    'http://localhost:5000/books/api/v1.0/book'

curl -i -H "Content-Type: application/json" \
    -X GET \
    'http://localhost:5000/books/api/v1.0/book'

curl -i -H "Content-Type: application/json" \
    -X PUT \
    'http://localhost:5000/books/api/v1.0/make_slug/2'

curl -i -H "Content-Type: application/json" \
    -X GET \
    'http://localhost:5000/books/api/v1.0/get_book/2-rasskazy-vasi-pupkina'

```
