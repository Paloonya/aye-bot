FROM python

COPY . .

EXPOSE 443

RUN pip install --upgrade pip
RUN pip install discord.py
RUN pip install telebot

CMD ["python", "./main.py"]