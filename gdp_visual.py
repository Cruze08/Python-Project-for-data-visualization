import json
import pygal
from pygal.style import LightColorizedStyle, RotateStyle
#load data in list
from countries_code import get_country_code


file_name='gdp_json.json'
with open(file_name) as f:
	gdp_data = json.load(f)

#print the 2014 GDP data for each country
cc_gdp = {}
prompt= int(input("Enter Year: "))
for gdp_dict in gdp_data:
	if gdp_dict['Year']==prompt:
		country_name=gdp_dict['Country Name']
		gdp = int(float(gdp_dict['Value']))
		#print(country_name + ' : ' + str(gdp))
		code=get_country_code(country_name)
		if code:
			cc_gdp[code]=gdp

cc_gdp1, cc_gdp2, cc_gdp3 = {},{},{}
#group the countries by their GDP VALUES
for cc, gdps in cc_gdp.items():
	if gdps<5000000000:
		cc_gdp1[cc]=round(gdps /1000000000)
	elif gdps< 50000000000:
		cc_gdp2[cc]=round(gdps/1000000000)
	else:
		cc_gdp3[cc]=round(gdps/1000000000)
		
#see how many countries are in each level
print(len(cc_gdp1), len(cc_gdp2), len(cc_gdp3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm=pygal.maps.world.World(style=wm_style)
wm.title='Global GDP in '+ str(prompt)  + ', by Country (in billions USD)'
wm.add('0-5bn', cc_gdp1)
wm.add('5bn-50bn',cc_gdp2)
wm.add('>50bn', cc_gdp3)
wm.render_to_file('World_gdp_'+ str(prompt) +'.svg')
