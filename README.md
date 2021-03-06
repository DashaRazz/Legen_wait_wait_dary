# Legen wait wait dary



## Целевая аудитория 

Группа друзей

## Потребности

Общение с друзьями. Личный блог

## Функционал

- Размещение постов
- Комментирование постов
- Размещение коротких статусов 

## Архитектрура

- Python
- SQLAlchemy
- Flask

## Обзор аналогов

**Аналог 1**

Сайт: https://medium.com

Дает возможность авторам и целым изданиям размещать заметки. Доступны короткие комментарии, открывающиеся во всплывающем окне справа, для более развернутых ответов предлагается написать отдельный пост. Сервис написания поста обладает минималистичным дизайном и  набором основных функций: выбор начертания текста и выключки абзацев, три уровня заголовков, цитирование и создание гиперссылок. Поддерживается работа нескольких авторов над одной заметкой. Материалы публикуются не в общей ленте, а в тематических категориях.


**Аналог 2**

Сайт: tumbler.com

На сайте пользователи ведут собственные блоги, а также подписываются на блоги других пользователей, чьи записи начинают отображаться в ленте подписавшихся. Помимо текстов, размещается и контент иных типов: фото, цитата, ссылка, чат, аудио и видео. Понравившиеся материалы могут быть отмечены «лайком», прокомментированы и перенесены к себе на страницу («реблог»). Функция отложенного постинга позволяет заранее создать запись и запланировать ее публикацию на определенное время. 


**Аналог 3**

Сайт: blogger.com

Веб-сервис для создания блогов без программирования и специального ПО, одна из старейших подобных платформ. Каждый блог представляет собой отдельный субдомен или собственный домен пользователя, блоги не существуют в единой экосистеме. Авторы создают внутри своих блогов сообщения, которые для удобства фильтрации могут быть помечены «ярлыками». Поддерживается добавления фото и видео, а также комментариев к записям. Также доступны простейшие настройки дизайна страницы и «фиды» для публикации контента на сторонних сайтах. 

| Критерий | Мой сайт | Аналог 1 | Аналог 2 | Аналог 3|
| ------ | ------ | ------ | ------ | ------ |
| публикация постов | 1 | 1 | 1 | 1 |
| комментирование | 1 | 1 | 1 | 1 |
|лента постов| 1 | 0 | 0 | 0 |
|отметка понравившихся постов| 0 | 1 | 1 | 0 |
|«репост» к себе на страницу| 0 | 0 | 1 | 0 |
|форматирование тектса| 0 | 1 | 1 | 1 | 
|совместная работа над постом| 0 | 1 | 0 | 0 |
|отложенная публикация| 0 | 0 | 1 | 1 |

**Вывод**

Продукт предоставляет пользователю самый основной набор функций для творчества по созданию собственных постов. Это позволяет сфокусироваться на процессе их написания или чтения, не отвлекаясь на дополнительные параметры. Кроме того функция создания статусов и просмотра статусов других пользователей дает другие возможности для общения и взаимодействия на платформе. 

## Прецеденты использования


![Иллюстрация к проекту](https://github.com/DashaRazz/Legen_wait_wait_dary/blob/master/Прецеденты%20использования.jpg)


| Критерий | Описание |
| ------ | ------ |
| Прецедент использования | Регистрация пользователя|
| Действующие лица | Гость |
|Краткое описание |Этот прецедент использования позволяет действующему лицу Гость зарегистрировать в системе новую учетную запись|
|Предусловия|Желание действующего лица зарегистрировать новую учетную запись|
|Основной поток|Прецедент использования начинается с того, что Гость решает зарегистрировать новую учетную запись и заполняет соответствующую регистрационную форму, обязательно указав имя, фамилию, пароль и имя учетной записи, после чего отправляет на регистрацию. Прецедент использования завершается|
|Альтернативные потоки|Действующее лицо Гость неверно заполнило регистрационную форму или учетная запись с таким именем уже существует. Заявка на регистрацию проекта, действующее лицо Гость получает сообщение об ошибке и должно либо повторно заполнить форму продолжая прецедент использования, либо отменить регистрацию завершая прецедент использования|
|Постусловия|Если прецедент использования завершился успешно, в системе регистрируется новая учетная запись, в противном случае состояние системы остается неизменным|


| Критерий | Описание |
| ------ | ------ |
| Прецедент использования |Авторизация|
| Действующие лица | Гость |
|Краткое описание|Прецедент использования позволяет Гостю войти в существующую учётную запись|
|Предусловия|Желание делиться с друзьями новостями|
|Основной поток|Прецедент использования начинается с того, что Гость решает зайти в существующую учётную запись и заполняет обязательные поля Логина и Пароля после чего отправляет данные на проверку|
|Альтернативные потоки|Действующее лицо Гость неверно заполнило поля Логина или Пароля. Действующее лицо Гость получает сообщение об ошибке и должно либо повторно заполнить форму продолжая прецедент использования, либо отменить регистрацию завершая прецедент использования|


| Критерий | Описание |
| ------ | ------ |
| Прецедент использования |Просмотр страницы с постами|
|Действующие лица|Гость, Авторизованный пользователь, Админ|
|Краткое описание|Этот прецедент использования позволяет совершить просмотр списка постов|
|Предусловия|Пользователь хочет узнать информацию|
|Основной поток|Пользователь заходит на главную страницу|
|Альтернативные потоки||
|Постусловия||


| Критерий | Описание |
| ------ | ------ |
| Прецедент использования |Добавление поста|
|Действующие лица|Авторизованный пользователь|
|Краткое описание|Прецедент позволяет Авторизированному пользователю добавить пост на главную страницу|
|Предусловия||
|Основной поток|Открытие формы добавления поста. Обязательное заполнение граф названия, лид и текста. Отправка поста на сервер|
|Альтернативные потоки|Пользователь не заполнил одну или несколько граф и сайт выдал ошибку|
|Постусловия|Пост размещается на главной странице сайта|


| Критерий | Описание |
| ------ | ------ |
| Прецедент использования |Редактирование поста пользователем|
|Действующие лица|Авторизованный пользователь, Админ|
|Краткое описание|Прецедент позволяет Авторизованному пользователю отредактировать свой пост, админ может отредактировать любой пост|
|Предусловия|Для редактирования поста авторизованному пользователю необходимо быть автором этого поста|
|Основной поток|Открытие поста, переход в форму редактирования поста, исправление поста и отправка его на сервер|
|Альтернативные потоки|Пользователь не заполнил одну или несколько граф и сайт выдал ошибку|
|Постусловия|Существующий пост меняет свое содержание|

| Критерий | Описание |
| ------ | ------ |
| Прецедент использования |Удаление поста|
|Действующие лица|Авторизованный пользователь, Админ|
|Краткое описание|Прецедент позволяет Авторизованному пользователю удалить свой пост, админ может удалить любой пост|
|Предусловия|Для удаления поста авторизованному пользователю необходимо быть автором этого поста|
|Основной поток|Открытие поста и нажатие кнопки удаления|
|Альтернативные потоки||
|Постусловия|Пост удален из базы данных и больше не отображается на главной странице сайта|

| Критерий | Описание |
| ------ | ------ |
| Прецедент использования |Добавление статуса|
|Действующие лица|Авторизованный пользователь|
|Краткое описание|Прецедент позволяет авторизованному пользователю добавить короткий статус, который будет отображаться на его личной странице|
|Предусловия|Для добавления статуса должна быть открыта личная страница пользователя|
|Основной поток|Открытие формы добавления статуса, написание текста, отправка текста на сервер|
|Альтернативные потоки|При добавлении статуса произошла ошибка. Следует отправить статус повторно|
|Постусловия|Добавление статуса на страницу пользователя|

| Критерий | Описание |
| ------ | ------ |
| Прецедент использования |Комментирование поста|
|Действующие лица|Авторизованный пользователь|
|Краткое описание|Прецедент позволяет добавлять комментарии к опубликованным постам|
|Предусловия|Для добавления комментария необходимо открыть страницу поста|
|Основной поток|Написание комментария в форме на странице и отправка его на сервер|
|Альтернативные потоки||
|Постусловия|Добавление комментария на страницу поста|


## Проектирование БД

**Список сущностей**
База данных в проекте – реляционная, значит ее сущностями являются таблицы, а объектами – строки. Список сущностей:

- Пользователь
- Пост
- Комментарий
- Статус

Далее в таблицах представлены поля сущностей системы и их значения.

**Пользователь**
| Свойство | Комментарий |
| ------ | ------ |
| id | Primary key. Идентификационный номер пользователя |
| nickname | Имя учётной записи |
| password | Пароль пользователя |
| email | Электронная почта пользователя |
| created_on | Дата регистрации пользователя |


**Пост**
| Свойство | Комментарий |
| ------ | ------ |
| id | Primary key. Идентификационный номер поста |
| title | Название поста |
| intro | Лид поста |
| text | Текст поста |
| date | Дата создания поста |
| user_id | ForeignKey('user.id'). Идентификационный номер пользователя создавшего пост|


**Комментарий**
| Свойство | Комментарий |
| ------ | ------ |
| id | Primary key. Идентификационный номер комментария |
| text | Текст комментария |
| date | Дата создания комментария |
| user_id | ForeignKey('user.id'). Идентификационный номер пользователя создавшего комментарий |
| article_id | ForeignKey('article.id'). Идентификационный номер поста, под которым разместили комментарий |


**Статус**
| Свойство | Комментарий |
| ------ | ------ |
| id | Primary key. Идентификационный номер статуса |
| text | Текст статуса |
| date | Дата создания статуса |
| user_id | ForeignKey('user.id'). Идентификационный номер пользователя создавшего статус |


**Отношения между сущностями**
| Сущность 1 | Сущность 2 | Тип связи | Пояснение|
| ------ | ------ | ------ | ------ |
| User | Article | Один ко многим | Один пользователь может добавлять много статей |
| User | Comment | Один ко многим | Один пользователь может добавлять много комментариев |
| Article | Comment | Один ко многим | Под одной статьей может быть много комментариев |
| User | Status | Один ко многим | Один пользователь может добавлять много статусов |

![Иллюстрация к проекту](https://github.com/DashaRazz/Legen_wait_wait_dary/blob/master/ER.png)
![Иллюстрация к проекту](https://github.com/DashaRazz/Legen_wait_wait_dary/blob/master/даталогическая%20модель.png)

## Список интерфейсов

Доступные гостю:
- Интерфейс авторизации
- Интерфейс регистрации
- Интерфейс главной страницы с постами
- Интерфейс страницы поста
- Интерфейс списка пользователей
- Интерфейс личных страниц

Доступные пользователю:
- Интерфейс главной страницы с постами
- Интерфейс страницы поста
- Интерфейс списка пользователей
- Интерфейс личных страниц
- Интерфейс создания поста
- Интерфейс создания статуса
- Интерфейс редактирования поста



### Добавление поста:
![Иллюстрация к проекту](https://github.com/DashaRazz/Legen_wait_wait_dary/blob/master/выкладывание%20поста.jpg)


### Главная страница:
![Иллюстрация к проекту](https://github.com/DashaRazz/Legen_wait_wait_dary/blob/master/посты.jpg)


### Страница с пользователями: 
![Иллюстрация к проекту](https://github.com/DashaRazz/Legen_wait_wait_dary/blob/master/люди.jpg)


### Страница поста:
![Иллюстрация к проекту](https://github.com/DashaRazz/Legen_wait_wait_dary/blob/master/пост.jpg)


### Добавление статуса: 
![Иллюстрация к проекту](https://github.com/DashaRazz/Legen_wait_wait_dary/blob/master/статус.jpg)


### Диаграмма интерфейсов:
![Иллюстрация к проекту](https://github.com/DashaRazz/Legen_wait_wait_dary/blob/master/Интерфейсы.png)
