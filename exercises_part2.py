# ---------- EXERCISE NINE ---------
grocery_list = ["carrots", "toilet paper", "apples", "salmon"]
grocery_list.append("rice")

for item in grocery_list:
  print(f"*  {item}")

print("There are", len(grocery_list), "items on your list")

if grocery_list.count('bananas') < 1:
  print("You need to pick up bananas")
else:
  print("You don't need to pick up bananas today")

print(grocery_list[1])

sorted_grocery_list = sorted(grocery_list)

def print_alpha_list():
  print("Alphabetical list:")
  print("---------------------")

  for item in sorted_grocery_list:
    print(f"*  {item}")

print_alpha_list()

sorted_grocery_list.pop(sorted_grocery_list.index('salmon'))

print_alpha_list()