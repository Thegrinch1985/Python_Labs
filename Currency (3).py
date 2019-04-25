# conversion from euro to usd, gbp, aud, cad

from functools import reduce

euro_rates = {'usd': 1.063, 'gbp': 0.837, 'aud': 1.417, 'cad': 1.393}

def convert_from_euro(value, to_currency):
        return value * euro_rates[to_currency]

def convert_to_euro(from_currency, value):
    return value * (1 / euro_rates[from_currency])

print (convert_from_euro(100, 'usd'))
print (convert_to_euro('usd', 100))

# a list of transactions
euro_account = []

def balance(trans):
	return sum(trans)

# +
def debit(amount, account):
	if amount > 0:
		account.append(amount)
	else:
		raise ValueError('invalid amount')

# -
def credit(amount, account):
	if amount > 0:
		if (amount <= balance(account)):
			account.append(-amount)
		else:
			raise ValueError('insufficent funds')
	else:
		raise ValueError('invalid amount')
	
debit(100, euro_account)
debit(200, euro_account)
credit(50, euro_account)
print (balance(euro_account))

# format transactions for display
def format(a, b):
    output = ''
    if b < 0:
        output += 'credit: '
    else:
        output += 'debit: '
    return str(a) + output + str(b) + ' '
output = reduce(format, euro_account, '')
print (output)

# convert to dollars
dollars = map(lambda euro: convert_from_euro(euro, 'usd'), euro_account)
print (list(dollars))