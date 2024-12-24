print("Select your ride:")
ride = int(input("Choose 1 for bike and 2 for car: "))

if ride == 1:
    print("You have chosen bike!")
    print("Choose the type of bike you want:")
    bike = int(input("Choose 1 for trike bike and choose 2 for unibike: "))
    if bike == 1:
        print("It's a trike bike!")
    else:
        print("It's a unibike!")
else:
    print("You have chosen car!")
    print("Choose the type of car you want:")
    car = int(input("Choose 1 for Lamborgini and choose 2 for Ferrari: "))
    if car == 1:
        print("It's a Lambo!")
    else:
        print("It's a Ferrari!")





