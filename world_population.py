import json
import pygal
from pygal.style import LightColorizedStyle, RotateStyle
#load data in list
from countries_code import get_country_code

file_name='population_data.json'
with open(file_name) as f:
	pop_data = json.load(f)

#print the 2010 population data for each country
cc_populations = {}
prompt=input("Enter Year: ")
for pop_dict in pop_data:
	if pop_dict['Year']==prompt:
		country_name=pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		#print(country_name + ' : ' + str(population))
		code=get_country_code(country_name)
		if code:
			cc_populations[code]=population

cc_pop1, cc_pop2, cc_pop3 = {},{},{}
#group the countries by their population
for cc, pop in cc_populations.items():
	if pop<10000000:
		cc_pop1[cc]=pop
	elif pop<1000000000:
		cc_pop2[cc]=pop
	else:
		cc_pop3[cc]=pop
		
#see how many countries are in each level
print(len(cc_pop1), len(cc_pop2), len(cc_pop3))


wm_style = RotateStyle('#336688', base_style=LightColorizedStyle)
wm=pygal.maps.world.World(style=wm_style)
wm.title="World population in " + prompt + ", by country"
wm.add('0-10m', cc_pop1)
wm.add('10m-1bn',cc_pop2)
wm.add('>1bn', cc_pop3)
wm.render_to_file('World_population_' + prompt + '.svg')
