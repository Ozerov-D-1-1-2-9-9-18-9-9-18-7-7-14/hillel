data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

result = {}

for item in data:
    item_name = item['item']
    item_amount = item['amount']

    if item_name in result:
        result[item_name] += item_amount
    else:
        result[item_name] = item_amount

print(result)

