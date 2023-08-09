import smtplib
import os
my_secret_log = os.environ['LOGIN']
my_secret_pas = os.environ['PASSWORD']

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')

text = """From: nick1tapinyagin@yandex.ru
To: nick1tapinyagin@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

website='https://dvmn.org/referrals/I8wtSY8wzbS3X0nCcFcYSeGVpJq6OAO8rZQhxfoU/'
friend_name = 'Леонид'
my_name = 'Никита'

text=text.replace('%website%',website)
text = text.replace('%friend_name%',friend_name)
text = text.replace('%my_name%',my_name)

text = text.encode("UTF-8")

server.login(my_secret_log, my_secret_pas)
server.sendmail('nick1tapinyagin@yandex.ru', 'nick1tapinyagin@yandex.ru', text)
server.quit()
