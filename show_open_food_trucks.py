from FoodTruck import FoodTruckController

FIELD_WIDTH = 80
nextPage = True
pageNum = 0
controller = FoodTruckController()

while nextPage:
    foodtrucks = controller.getCurrentOpenFoodTrucks(pageNum)
    if not foodtrucks:
        if pageNum:
            print("No More Food Trucks")
        else:
            print("No Open Food Trucks")
        print("<---Bye--->")
        break
    print(f'{"NAME".ljust(FIELD_WIDTH, " ")} ADDRESS')
    print("".ljust(100, '-'))
    for truck in foodtrucks:
        print(f'{truck.name.ljust(FIELD_WIDTH, " ")} {truck.address}')
    userInput = input("\nDo you want to see more (Y/N): ").lower()
    print()
    if userInput in ['y', 'yes']:
        pageNum += 1
    else:
        print("<---Bye--->")
        nextPage = False
