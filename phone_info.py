import phonenumbers

from phonenumbers import geocoder
ch_number = phonenumbers.parse("+905396128980", "CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier

serice_number = phonenumbers.parse("+905396128980", "Ro")
print(carrier.name_for_number(serice_number,"en"))