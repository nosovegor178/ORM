### Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т. к. у вас нет доступа к БД, но можете свободно использовать код верстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визами допуска и карточками пропуска сотрудников нашего банка.

### Как установить


Python 3.11 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

### Переменные окружения
Необходимо создать файл .env в котором нужно прописать такие строки:
```
DB_ENGINE='engine' - движок сайта
DB_HOST='host' - хост сайта
DB_PORT='port' - порт сайта
DB_NAME='name' - имя 
DB_USER='username' - имя пользователя
DB_PASSWORD='password' - пароль
DEBUG=false
SECRET_KEY='secret_key' - секретный ключ
ALLOWED_HOSTS='alowed_hosts' - разрешенные хосты
```
Здесь вместо значений в кавычках нужно подставить свои. Без этого программа работать не будет.

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org]("https://dvmn.org/modules/").