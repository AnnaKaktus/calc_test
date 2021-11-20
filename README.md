# autotests with appium for drom
## Автотесты для тестового задания Калькулятор
С помощью данных тестов осуществляется smoke-тестирование приложения (проверка основного функционала)

Для запуска тестов:

- создаем виртуальное окружение python
- необходимо установить библиотеку pythest командой `pip install -U pytest`
- установить пакет appium `pip install Appium-Python-Client`
- в файле calc_test.py задаем полный путь до apk калькулятора **PATH_TO_APK** при необходимости меняем настройки драйвера
- в Android studio запускаем эмулятор или реальное устройство
- запускаем сервер Appium

- запустить все тесты `pytest -v`
- запустить конкретный тест `pytest -k имя_теста`
