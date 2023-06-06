# CERT.py
# Copyright (С) 2023 Ефимов Даниил УГИ-216004

# Это программное обеспечение лицензировано под GNU GPL версии 3 или выше.
# Вы можете найти текст лицензии по адресу https://www.gnu.org/licenses/gpl.html

#Данная программа разделяет на отдельные сертификаты созданный шаблон
import csv
import os
from PyPDF2 import PdfReader, PdfWriter
import pandas as pd

# Путь к PDF-файлу
pdf_file_path = 'CERT.pdf'

# Путь к CSV-файлу
csv_file_path = 'data.csv'

# Загрузка данных из CSV-файла
data = pd.read_csv(csv_file_path, header=None)

# Открытие PDF-файла
with open(pdf_file_path, 'rb') as pdf_file:
    pdf = PdfReader(pdf_file)

    # Перебор страниц PDF-файла и данных из CSV-файла
    for i, row in data.iterrows():
        page = pdf.pages[i]
        
        # Получение имени файла на основе данных из CSV-файла
        filename = f"{row[1]}_{row[2]}.pdf"

        # Создание нового PDF-файла для текущей страницы
        output_pdf = PdfWriter()
        output_pdf.add_page(page)

        # Сохранение нового PDF-файла
        output_path = os.path.join('CERT_OUT', filename)
        with open(output_path, 'wb') as output_file:
            output_pdf.write(output_file)
