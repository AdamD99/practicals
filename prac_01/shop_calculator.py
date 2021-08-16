
item_count = int(input("Number of items: "))
total_price = 0

while item_count <= 0:
    print("Invalid number of items!")
    item_count = int(input("Number of items: "))

for i in range(item_count):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9

print("Total price for {:} item(s) is ${:.2f}".format(item_count, total_price))