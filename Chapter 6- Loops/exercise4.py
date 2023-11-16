sandwich_orders = ["pastrami","tuna", "ham", "club", "turkey"]
finished_sandwiches = []

print("\n\tWelcome to Sandwitch!\n")
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print("we are making your " + made_sandwich + " sandwich")
    finished_sandwiches.append(made_sandwich)

print("\n")
for items in finished_sandwiches:
    print("we have made your " + items + " sandwich")
