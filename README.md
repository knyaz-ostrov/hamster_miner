Hamster Mine
Скрипт для автоматического фарма монет в Hamster Kombat.

Инструкция по запуску:

ШАГ 1: Скачайте и установите Python
Скачайте и установите Python последней версии с 'https://www.python.org/'.
Обязательно отметьте опцию "Add Python to PATH" перед установкой.

ШАГ 2: Скачайте программу Hamster Mine
Скачайте код с Github: 'https://github.com/knyaz-ostrov/hamster_miner/archive/refs/heads/master.zip'.
Распакуйте код в удобном для вас месте.

ШАГ 3: Узнайте свой токен авторизации Hamster Kombat
Установите расширение Resource Override в интернет-магазине chrome: 'https://chromewebstore.google.com/detail/resource-override/pkoacgokdfckfpndoffpifphamojphii'
Открой меню установленного расширения; нажмите кнопку 'Add Rule' -> 'Inject File'. В списке ниже
появится безымянный файл; в его строке нажмите Edit File.
Откройте любым текстовым редактором файл 'override.js' и скопируйте всё содержимое; вставьте в поле
редактирования расширения Resource Override и нажмите 'Save & Close'. Перейдите в веб-версию телеграма: 'https://web.telegram.org/';
залогиньтесь и откройте Hamster Kombat. Нажмите клавишу F12. В открывшемся окне перейдите во вкладку Network.
Тапните по хомяку и через несколько секунд в панели Network появится объект 'tap' с полем Status - 200.
Нажмите на этот объект и в открывшемся окне во вкладке Headers найдите параметр 'Authorization'.
Справа напротив него скопируйте набор латинских букв и цифр после слова 'Bearer'.
Перейдите в папку с программой и откройте файл 'config.py' в любом текстовом редакторе.
Найдите параметр 'TOKEN' и вставьте скопированное значение между одинарными кавычками.
ПРИМЕР:
```python
TOKEN = 'qweRTY1234ytrEWQ4321'
```

ШАГ 4: Создайте виртуальное окружение
Перейдите в папку с распакованной программой и создайте виртуальное окружение
```PowerShell
cd путь/к/папке/
py -m venv venv
```

ШАГ 5: Активируйте виртуальное окружение и установите модуль requests
```PowerShell
venv/Scripts/activate
pip install requests
```

ШАГ 5: Запустите скрипт
```PowerShell
py main.py
```
