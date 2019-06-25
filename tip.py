billtotal = float(input('What was the total bill? '))
service = input('How was the service (good, fair, or bad)? ').lower()
if service == 'good':
    goodservice = billtotal * 0.20
    print('You should tip: ' + str(goodservice))
elif service == 'fair':
    fairservice = billtotal * 0.15
    print('You should tip: ' + str(fairservice))
elif service == 'bad':
    badservice = billtotal * 0.10
    print('You should tip: ' + str(badservice))
else:
    print('Invalid answer!')