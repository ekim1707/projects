billtotal = float(input('What was the total bill? '))
service = input('How was the service (good, fair, or bad)? ').lower()
partysize = int(input('Split how many ways? '))
if service == 'good':
    goodservice = billtotal * 0.20
    print('Tip amount: ' + str(goodservice))
    print('Total amount: ' + str(billtotal))
    print('Amount per person: ' + str(goodservice/partysize))
elif service == 'fair':
    fairservice = billtotal * 0.15
    print('Tip amount: ' + str(fairservice))
    print('Total amount: ' + str(billtotal))
    print('Amount per person: ' + str(fairservice/partysize))
elif service == 'bad':
    badservice = billtotal * 0.10
    print('Tip amount: ' + str(badservice))
    print('Total amount: ' + str(billtotal))
    print('Amount per person: ' + str(badservice/partysize))
else:
    print('Invalid answer!')