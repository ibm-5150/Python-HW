velocity  = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53,'july':54, 'Aug':44, 'Sept':54} 
time  = {'jan':300, 'feb':700 , 'march':900, 'April':1200, 'May':600, 'June':700,'july':80, 'Aug':500, 'Sept':600}

#distance: s = v*t

"""
for key in velocity:
	print(key)

for value in velocity.values():
	print(value)
"""

#loop 1
time['jan'] = 300/60
time['feb'] = 700/60
time['march'] = 900/60
time['April'] = 1200/60
time['May'] = 600/60
time['June'] = 700/60
time['july'] = 80/60
time['Aug'] = 500/60
time['Sept'] = 600/60

#print(time)

#loop 2
jan = round(velocity['jan'] * time['jan'])
feb =  round(velocity['feb'] * time['feb'])
march = round(velocity['march'] * time['march'])
april = round(velocity['April'] * time['April'])
may = round(velocity['May'] * time['May'])
june = round(velocity['June'] * time['June'])
july = round(velocity['july'] * time['july'])
aug = round(velocity['Aug'] * time['Aug'])
sept = round(velocity['Sept'] * time['Sept'])

print(f'Distance: \nJanuary: {jan}km \nFebruary: {feb}km \nMarch: {march}km \nApril: {april}km \nMay: {may}km \nJune: {june}km \nJuly: {july}km \nAugust: {aug}km \nSeptember: {sept}km')