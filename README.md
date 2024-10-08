## Описание проекта

Проект "Gazprom Organizational Chart Backend" представляет собой серверную часть системы управления организационной структурой компании. Система позволяет управлять информацией о сотрудниках, их должностях, командах и проектах. Основная цель проекта — обеспечить удобный и эффективный способ отслеживания и управления ресурсами компании, а также предоставить API для интеграции с другими системами.

## Стэк технологий

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose
- **API Documentation**: drf-yasg (Swagger)
- **Authentication**: djangorestframework-simplejwt

## Ссылки на сторонние фреймворки и библиотеки

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [drf-yasg](https://github.com/axnsan12/drf-yasg)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [djangorestframework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt)

## Запуск проекта

0. При необходимости устанавливаем Docker: [Docker Desktop](https://www.docker.com/products/docker-desktop)
1. Клонируем и переходим в дирректорию проекта:

    ```
    git clone git@github.com:Gazprom-Operator-ID-Hackathon/gazprom_operator_id_hackathon_backend.git
    cd gazprom_operator_id_hackathon_backend/
    ```

2. Создаем в корневой директории `.env` и копируем в него содержимое `.env_example`.
3. Из корневой папки запускаем:

    ```
    docker-compose up --build
    ```

4. Команда сборки и запуска контейнера включает в себя создание superuser для входа в административную панель:

    ```
    login: admin
    password: admin
    ```

API проекта будет доступен по адресу: [http://127.0.0.1:8000/api/v1/](http://127.0.0.1:8000/api/v1/).

Swagger проекта будет доступен по адресу: [http://127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger).

Вход в административную панель: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

## Развертывание проекта

Готовый проект доступен по адресу: [https://timurisrafilov.github.io/gaz-hack-front/#/company](https://timurisrafilov.github.io/gaz-hack-front/#/company).

API доступен по адресу: [https://hackathonproject.sytes.net/api/v1/users/](https://hackathonproject.sytes.net/api/v1/users/).

Основные эндпоинты API:

- получение списка пользователей с определенным набором полей: [https://hackathonproject.sytes.net/api/v1/users/](https://hackathonproject.sytes.net/api/v1/users/);

- получение конкретного пользователя по id (на примере id=402): [https://hackathonproject.sytes.net/api/v1/users/402](https://hackathonproject.sytes.net/api/v1/users/402);

- получение основной информации о проектах с определенным набором полей: [https://hackathonproject.sytes.net/api/v1/projects/](https://hackathonproject.sytes.net/api/v1/projects/);

- получение списка IT-компонентов с определенной структурой полей: [https://hackathonproject.sytes.net/api/v1/itcomponents/](https://hackathonproject.sytes.net/api/v1/itcomponents/);

- Swagger проекта: [https://hackathonproject.sytes.net/swagger](https://hackathonproject.sytes.net/swagger).

## Основные реализованные бизнес-логики в проекте

Учитывая сокращенные сроки разработки, основное внимание было сфокусировано на создании структуры взаимосвязей моделей для реализации функционала по управлению работниками и их текущими проектами.

В проекте каждый сотрудник имеет следующие связи:

- связь с проектами, в которых данный сотрудник задействован;
- связь с командой, в которой он состоит. Команды разделены по направлениям (дизайн, маркетинг, анализ, менеджмент, HR, девопсы, девелопмент);
- связь с непосредственным руководителем в иерархии подчиненности компании.

Для презентации проекта в базу данных были добавлены 47 карточек работников с уникальными данными (имя, фамилия, аватар, грейд, навыки и т.д.), для каждого из них настроены вышеуказанные связи.

## Система аутентификации и авторизации

По нашему мнению, учитывая назначение разрабатываемого решения для использования заказчиком для собственных нужд, мы не добавляли механизмы регистрации и авторизации "из вне".

Согласно общепринятой практике в крупных компаниях, от которой мы отталкивались, при найме нового сотрудника и добавлении его в команду, администратор создает учетную запись с данными пользователя, вручную указывает необходимые данные (имя, фамилия, стек, регион проживания, набор навыков, указание на команду и руководителя и пр.).

После внесения информации в учетную запись сотрудника, данные изменения отражаются в разделе "Организационная диаграмма", где наглядно показывается членом какой группы является данный работник, кто его руководитель, над каким IT-компонентом в настоящее время работает команда, описание команды, контакты и другая информация.

## Наши предложения по дальнейшему развитию проекта

### 1. Функционал Drag-and-Drop в разделе "Организационная диаграмма"

В настоящее время в проекте уже реализован функционал Drag-and-Drop на уровне управления работниками конкретной группы.
В дальнейшем целесообразно расширить этот функционал для удобного управления работой над всемии IT-компонентами в целом.

Например, создается новый IT-компонент с новым заданием. В начале в данном проекте, допустим, нужны только команды дизайна, анализа и маркетинга.
"Перетаскиваем" в нужный IT-компонент свободные команды, руководителям команд на корпоративную почту поступает письмо с содержанием задачи и ответственным лицом для связи.
После разработки артефактов "переносим" из IT-компонента ненужные команды и добавляем команды разработчиков для реализации задания. Если нужно, чтобы в проекте осталось по одному дизайнеру/аналитику/маркетологу, то конкретного работника оставляем на данном IT-компоненте. Все происходит через Drag-and-Drop.

### 2. Функционал для рассылки писем по корпоративной почте

При добавлении команды в новый IT-компонент, переводе на другой IT-компонент и т.д. руководителям групп приходит рассылка на адрес корпоративной почты с описанием задачи и ответственным лицом. С данным отвественным лицом руководители могут связаться через контакты, указанные в профиле сотрудника. Также есть возможность найти любого коллегу через поиск или организационную диаграмму и связаться с ним.
Это сэкономит время на постановку новых задач и облегчит процесс коммуникации между участниками проектов.

### 3. Система прав для руководителей различных уровней

У каждой группы руководителей свои обязанности и полномочия. Например, правом на создание новых IT-компонентов может обладать высший руководящий состав. Руководители команд и сотрудники имеют права, связанные с доступом к определенным IT-компонентам. 
Для сотрудников отдела HR мы предлагаем добавить структуру прав, связанных с управлением составом команд, формированием новых команд при найме сотрудников и т.д.

## Разработчик

- Павел Охрим. [Telegram](https://t.me/d1g_it)
