import phonenumbers

from phonenumbers import geocoder

print('')
print('			Digite o Número como no exemplo:')
print('')
print('		##################################################')
print('		#		Exemplo: +5555999999999          #')
print('		##################################################')
print('')

##Number= str(input('Digite o número do Celular:'))

Number= str('55999999999')
ch_number = phonenumbers.parse(Number, "BR")
print('')
print('Local:', geocoder.description_for_number(ch_number, "BR"))

##print('Regiam:', geocoder._region_display_name(ch_number, "en"))

print('')
from phonenumbers import carrier
service_number = phonenumbers.parse(Number, "BR")
print('Operadora:', carrier.name_for_number(service_number, "pt-br"))

print('')

from phonenumbers import timezone
gb_number = phonenumbers.parse(Number, "BR")
print('Fuso Horário: ', timezone.time_zones_for_number(gb_number))