Проект на фреймворке Django

Выгрузите репозиторий командой git clone https://github.com/GalakhovOA/TopShop.git

В этом репозитории уже есть виртуальное окружение на версии python 3.11, убедитесь, что у вас установлен python 3.11, если нет - установите.

активируйте venv, если он не активировался автоматически

.venv\Scripts\activate или venv\Scripts\activate

Перейдите в основную папку cd myshop

Может потребоваться установка Pillow, при требовании установки, введитие команду python -m pip install Pillow

Выполнить миграцию БД: python manage.py makemigrations python manage.py migrate при необходимости

Запустите проект командой python manage.py runserver

Перейдите по адресу http://127.0.0.1:8000 - стартовая страница
