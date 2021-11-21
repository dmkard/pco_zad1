FROM python:3.10.0-alpine3.14
#tworzenie zmiennej srodowiskowej z numerem portu
ENV PORT="7000"
#kopiowanie pliku ze skryptem do kontenera
COPY app.py /
#otwieranie portu 7000
EXPOSE ${PORT}
#instalacja niezbednych bibliotek
RUN pip install requests && pip install pytz
#uruchomienie skryptu serwera
CMD python -u app.py