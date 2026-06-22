items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if items in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)


