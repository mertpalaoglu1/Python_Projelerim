import requests
import json
## Gelecek commitlerde uygulama arayüzü eklenecek. 

sehir = input("Şehir adi giriniz: ")
origin_url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid=e5d4d1ef34e7df15187c034c597ee14d"
response = requests.get(origin_url) ## Sitedeki verileri çektik ve response değişkenine atadık.

if response.status_code==404:
    print("Sehir ismi hatali.") ## Dönen status kodu kullanarak, girilen isim hatali mi diye kontrol ettik.
else:    
    jsonResponse = json.loads(response.text) ## İsimde hata yoksa devam edip verileri json olarak parçalara böldük.

sicaklik=str(jsonResponse["main"]["temp"] - 272.15)
hissedilen=str(jsonResponse["main"]["feels_like"] -272.15 ) ## Kelvinden Celcius'a çevirdik.
basinc=str(jsonResponse["main"]["pressure"])
nem=str(jsonResponse["main"]["humidity"])

print("İsim: " + sehir ) 
print("Sicaklik: " + sicaklik + " °C" )
print("Hissedilen Sicaklik: "+ hissedilen + " °C" ) 
print("Basinc: "+ basinc + " Paskal") 
print("Nem Orani: "+ "%" + nem ) 