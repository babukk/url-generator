
curl -i -H "Content-Type: application/json" \
    -X POST -d '{"title": "Harry Potter", "author": "J. K. Rowling", "description": "Harry Potter is a series of fantasy novels written by British author J. K. Rowling."}' \
    'http://localhost:5000/books/api/v1.0/book'


curl -i -H "Content-Type: application/json" \
    -X POST -d '{"title": "рассказы Васи Пупкина", "author": "Вася Пупкин", "description": "Рассказы Васи Пупкина о себе."}' \
    'http://localhost:5000/books/api/v1.0/book'
