# cert_msg.py
# Copyright (С) 2023 Ефимов Даниил УГИ-216004

# Это программное обеспечение лицензировано под GNU GPL версии 3 или выше.
# Вы можете найти текст лицензии по адресу https://www.gnu.org/licenses/gpl.html

#Данная программа отправляет сертификаты участника
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# SMTP сервер и порт для mail.ru
smtp_server = "smtp.mail.ru"
smtp_port = 587

# Логин и пароль почты mail.ru
smtp_username = "uanalitic_test@mail.ru"
smtp_password = "aMuFHpGn0cDurV7gJpvn"

# Электронная почта, от которой отправляются письма
from_email = "uanalitic_test@mail.ru"

# Чтение списка адресов и имен файлов с приглашениями из CSV файла
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        to_email = row[0]
        first_name = row[2]
        last_name = row[1]
        invitation_file = f"{last_name}_{first_name}.pdf"
        subject = 'СЕРТИФИКАТ'

        # Создание сообщения
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject

        # Добавление текста сообщения
        message.attach(MIMEText('TEST', 'plain'))  # Здесь нужно обновить текст сообщения

        # Добавление файла с приглашением в PDF формате
        with open(invitation_file, 'rb') as pdf_file:
            pdf_attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
            pdf_attachment.add_header('Content-Disposition', 'attachment', filename=invitation_file)
            message.attach(pdf_attachment)

        # Отправка сообщения
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, message.as_string())
            print('Email sent to', to_email)
        except Exception as e:
            print('Error sending email to', to_email, ':', str(e))
        finally:
            server.quit()

