from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
	#Return 2 digit country code
	for code, name in COUNTRIES.items():
		if name==country_name:
			#print(COUNTRIES.values())
			return code
		#if the name is not same then return none
	return None
#print(get_country_code('India'))
