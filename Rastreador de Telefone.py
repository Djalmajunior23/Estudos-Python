import phonenumbers


from phonenumbers import geocoder

phone = input('Digite o telefone no formato +5531999784473:  ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
print(geocoder.country_name_for_number(phone_number, 'pt'))
print(geocoder.description_for_valid_number(phone_number, 'pt'))
