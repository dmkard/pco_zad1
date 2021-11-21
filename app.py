import http.server
import socketserver
import urllib.request
import os
import requests
from datetime import datetime
import pytz
import json


class HttpGetHandler(http.server.SimpleHTTPRequestHandler):

    #nadpisanie funkcji co odpowiada za nadchodzace GET zapytania
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Server</title></head>'.encode())
        #pobranie zewnetrznego ip klienta
        ipAdd = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        #pobranie info o kliencie
        data = (requests.get(url="http://ip-api.com/json/"+ipAdd)).json()
        #pobranie czasu i daty z pobranych danych
        currentTime = datetime.now(pytz.timezone(data["timezone"]))
        #wypisanie na stronie danych
        self.wfile.write('<body>Twoj IP address: {} </br>'.format(ipAdd).encode())
        self.wfile.write('Czas: {} </body></html>'.format(currentTime).encode())

Handler = HttpGetHandler

#pobranie numeru portu ze zmienych srodowiskowych       
Port= os.environ['PORT']

#wypisanie logow
print("Start serweru o ", datetime.now())
print("Nasluchanie na ", Port)
print("Dmytro Kardash")

#twirzenie serwera
httpd = socketserver.TCPServer(("", int(Port)), Handler)

try:
    #uruchamianie serwera
    httpd.serve_forever()

except KeyboardInterrupt:
      httpd.server_close()

