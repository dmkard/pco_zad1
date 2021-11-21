# Zadanie 1 i 2
Serwer jest napisany na Pythonie. Program serweru pobiera zewnętrzny IP adres klienta wysyłając żądanie na *https://ident.me*. Z danego IP program następnie wysyła żądznie na *http://ip-api.com/json/* żeby dostać info o strefie czasowej, i przy pomocy bibliotek Pythona dostaje aktualny czas klienta. Dla spęłnienia tych celów Dockerfile posiada polecenie do instalacji bibliotek **requests** oraz **pytz**.

# Zadanie 3

- budowanie obrazu kontenera
`docker build -t httpserver:v1 .`

- uruchomienie kontenera na podstawie zbudowanego obrazu
`docker run --name server -p 80:7000 httpserver:v1`

- dostęp do informacji wygenerowanych w trakcie uruchamiania kontenera
`docker logs server`

- sprawdzenie ile warstw posiada obraz
`docker image inspect  httpserver:v1 | jq '.[].RootFS.Layers'`
*Obraz posiada 7 warstw.*

![]https://github.com/dmkard/pco_zad1/blob/main/Resources/screenshot.png)

# Zadanie 4
W płatnych subskrypcja DockerHub daje możliwość na podpinanie konta GitHub do konta DockerHub. Takie podpięcie daje możliwośc do wskazania brahchu, przy commicie do którego musi być odpalony auto build. Jest też możliwosć wskazania tagu obrazu po auto buildzie. Źródło: https://davelms.medium.com/build-your-docker-images-automatically-when-pushing-new-code-to-github-394f4c1679cc
