## Проект API автотестов 

<!-- Технологии -->
<p  align="center">
  <code><img width="5%" title="Pycharm" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/pycharm.png"></code>
  <code><img width="5%" title="Python" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/python.png"></code>
  <code><img width="5%" title="Pytest" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/pytest.png"></code>
  <code><img width="5%" title="GitHub" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/github.png"></code>
  <code><img width="5%" title="Jenkins" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/allure.png"></code>
  <code><img width="5%" title="Allure TestOps" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/allure_testops.png"></code>
  <code><img width="5%" title="Telegram" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/telegram.png"></code>
  <code><img width="5%" title="Telegram" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/json.png"></code>
</p>

<!-- Тест кейсы -->

### Что проверяем

* Запрос списка пользователей
* Создание нового пользователя с валидными данными 
* Обновление данных пользователя
* Удаление пользователя
* Регистрация с валидными данными 
* Регистрация с невалидными данными
* Вход в систему с валидными данными
* Вход в систему с невалидными данными


### <img width="5%" title="Jenkins" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/jenkins.png"> Запуск проекта в Jenkins  
### [Job](https://jenkins.autotests.cloud/job/qa_guru_6_diploma_API/)

При нажатии кнопки "Собрать сейчас" происходит сборка авторестов и формируются 2 отчета: Allure Report и Allire TestOps

<img width="100%" title="parametrs" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/screenshots/joba.png"></code>

<!-- Allure report -->

 ### <img width="5%" title="Allure Report" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/allure.png"> Allure

 ### [Report](https://jenkins.autotests.cloud/job/qa_guru_6_diploma_API/2/allure/)
 
 После прохождения теста результаты можно посмотреть в Allure отчете.

<img width="100%" title="parametrs" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/screenshots/allure.png"></code>

 Во вкладке Suites можно посмотреть собранныет тесты, у которых описаны шаги, приложены логи, скриншот и видео прохождения теста 

 <img width="100%" title="parametrs" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/screenshots/allure_suites.png"></code>

  <!-- Allure TestOps -->

  ### <img width="5%" title="Allure TestOps" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/allure_testops.png"> Интеграция с Allure TestOps
 
 ### [Allure Testops](https://allure.autotests.cloud/launch/30802)

 Также отчетность генерируется в Allure TestOps.

 <img width="100%" title="parametrs" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/screenshots/allure_testops.png"></code>

 <img width="100%" title="parametrs" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/screenshots/testops.png"></code>

 <!-- Telegram -->

### <img width="5%" title="Telegram" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/images/telegram.png"> Интеграция с Telegram

После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

<img width="50%" title="allure_tests" src="https://github.com/Alexaborland/qa_guru_python_6_diploma_API/blob/main/screenshots/telegram.png"></code>
 
 
