# При использовании ORM Session объект отвечает за построение Insert конструкций и их выпуск в виде операторов INSERT
# в рамках текущей транзакции. Мы указываем Session сделать это, добавляя в него записи объектов; Session
# затем обеспечивает, чтобы эти новые записи были выпущены в базу данных, когда они понадобятся, используя процесс,
# известный как flush . Общий процесс, используемый для Sessionсохранения объектов, известен как шаблон единицы работы.

