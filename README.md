# Социальное веб-приложение bookmarks.
## Краткий функционал
0. Пользователи могут делиться изображениями, которые они находят в интернете и добавляют на свой профиль со своим описанием.
1. Сервис имеет систему аутентификации (регистрация, вход в систему, редактирование своего профиля, менять или сбрасывать пароль).
2. Система подписки, позволяющая пользователям подписываться друг на друга на сайте.
3. Функциональность отображения выложенных изображений и система, позволяющая пользователям делиться изображениями с любого веб-сайта.
4. Поток активности, который позволяет пользователям видеть контент людей, на которых оформлена подписка.
   

## Подробное описание функционала

В приложении есть 3 основные страницы с контентом.

0. My dashboard
1. Images
2. People

На странице ```Dashboard``` представлена информация о количестве изображений добавленных на сайт пользователем. Представлен функционал кнопки для добавления изображений на сайт через панель закладок. Так же есть возможность изменить свой профиль и сменить пароль. В блоке ```What's happening``` отображается лента активности пользователей на которых оформлена подписка.

----

![home_page](https://sun9-45.userapi.com/impg/zUvX37Tw3PCNCCrowPQxvw04DOWAzl39AYEdkg/yY6lyGyL59E.jpg?size=771x682&quality=96&sign=01d615978b9e44d985364d496db38951&type=album "Домашнаяя страница")

----

Во вкладке ```Images``` представлены миниатюрные версии всех изображений загруженных на сайт пользователями. По клику мыши можно перейти к описанию изображения, лайкнуть изображение и посмотреть количество просмотров данного изображения (просмотры реализованны с помощью ```Redis```). Так же на данной странице реализована бесконечная прокрутка ленты изображений.

----

![images page](https://sun9-71.userapi.com/impg/qCM18t2-6E1AePWKu3O_18hmIwJPBtSXjKyJEg/MrO-qApjNSg.jpg?size=1280x696&quality=96&sign=4cfd8b1128969836f986d5a0eb1d273e&type=album "images page")

![Post page](https://sun9-47.userapi.com/impg/gMjnrng1qQ5YC_ie361GPnnAyVBHnW6x9s9sdg/-fO5J09lxTA.jpg?size=1280x463&quality=96&sign=f1c756876973dd9623351676047cc1dc&type=album "Post page")

----

Во вкладке ```People``` отображаются все пользователи зарегистрированные на сайте. Если кликнуть по аватару пользователя можно перейти к нему в профиль и ознакомиться с изображениями, которые он добавил на сайт, количеством подписчиков, и произвести подписку.

----

![people](https://sun9-77.userapi.com/impg/nqUnzKqiSiewjoUWufxQDa3xVtdsw1sZMg1j5g/SpiaZUzUNyo.jpg?size=1273x372&quality=96&sign=a43d8e3a8e47537b514e341cc67fdb41&type=album "peoples page")

![profile](https://sun9-7.userapi.com/impg/LEZNWRUVWAsXBUJsKybKLPjW3Vygb559meM9RA/SQFAyBPS-tg.jpg?size=1280x684&quality=96&sign=bea8d25d1d06f22d52b1b8480f7d3fcc&type=album "Профиль пользователя")

## Аутентификация пользователей

Перед использованием функционала сайта пользователю необходимо авторизоваться, либо зарегистрировать свой профиль. Предусмотрен функционал сброса пароля через email и социальную авторизацию через google аккаунт. Для реализации работы по https используется криптографическая библиотека ```werkzeug``` для генерации SLL-сертификата. Так как сгенерированный SSL-сертификат не проходил верификацию система безопасности браузера будет предупреждать о небезоспасном соединении.

----

![log-in](https://sun9-62.userapi.com/impg/eml_Uw-woLxebs3bXCa1rFBqHmUjIPRBtkTsLA/4IEfbK_Yj2o.jpg?size=1280x490&quality=96&sign=209763c9564f3a72d66aac189259924c&type=album "Login")

----
При сбросе пароля генерируется ссылка с формой для регистрации нового пароля для профиля. Предусмотрена проверка валидности пароля на тривиальность.

----

![email](https://sun9-43.userapi.com/impg/GUSCeGp-9Fri2Z0ssaKfPjzsCm2MOcXMQ8WPCw/fTyReKwarLY.jpg?size=715x290&quality=96&sign=25c7af21098cc0843440c2f93b59a6ea&type=album "Email reset")

![Reset](https://sun9-33.userapi.com/impg/g0-T492dQy85gHFbXTM9lC6U0XwMs4_RSeQ5-w/BvOAyM75RVI.jpg?size=743x673&quality=96&sign=1e9557697a787c2160024ea9282c5458&type=album "Reset done")

## Визуальная демонстрация функционала

HTML-контейнер для выбора изображения на выбранном сайте. Запускается с помощью панели закладок. Закладка позволяет пользователям сохранять изображения в своей учетной записи.
Реализован с помощью JavaScript.

----
![select](https://sun9-49.userapi.com/impg/jioxBi8LQt3oO9jFsmFbAWXIqNd5ryAmj4Kouw/T5Q43Ma1cNk.jpg?size=1249x878&quality=96&sign=b095bad9fb9248fe1d085f40e6f6601d&type=album "Select image")

----

Страница редактирования информации об изображении перед загрузкой на сайт. Опционально можно добавить описание для изображения. 

----
![Add](https://sun9-5.userapi.com/impg/-V_KdZUzczAo5vpnLXx_zMc6fG0IN0v804vEBw/uukaqH6nJas.jpg?size=940x613&quality=96&sign=f94b161843421eb56774db34276f3574&type=album "Add image")

-----

Страница добавленного изображения с уведомлением об успешной загрузке на сайт. Количество просмотров обновляются с каждым переходом на страницу. Подсчет реализован с помощью Redis, для оптимизации SQL запросов к БД.

----
![Image_added](https://sun9-59.userapi.com/impg/Gw98D9VEt74z50-kZ-iRfmWPHAdKLrJmbfykVg/OlQggztW30U.jpg?size=1280x683&quality=96&sign=3afd56e1157c68b20ad8efab6d6d0ef7&type=album "Image_added")

----
Так же с помощью Redis был реализован рейтинг изображений по количеству просмотров.

----
![rank](https://sun9-72.userapi.com/impg/Rq7DHnuNlCU-ay3ACVglXXOOaCQNKYo56pU2yg/8xOMq7GbEKM.jpg?size=1091x589&quality=96&sign=a243ca3058efb9e75fdf5da610dff944&type=album "Rank")

----
Страница редактирования информации профиля пользователя.

----
![Edit](https://sun9-57.userapi.com/impg/MNGSHg6HBMg0qjTRXk5NwrclePEIrUk_XacO4A/AseXSWCYjgk.jpg?size=840x854&quality=96&sign=9f81f7e7c71a3b0a38be726e92d28236&type=album "Edit profile")

----
Страница регистрации пользователя. При регистрации предусмотрена проверка на валидность поля электронной почты.

----
![Registation](https://sun9-70.userapi.com/impg/O2rhNcqCzKNH-IgPKcBKttdlSIt1u-kjBNJIQA/XSdeMswnQro.jpg?size=860x813&quality=96&sign=09451a8018ce4c8a420f37d8c6b89de1&type=album "Rigister page")

