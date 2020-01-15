totalAmount = int(input("How much is your bill? "))
serviceLevel = input("How was your service (Good or Bad): ")
numOfPayers = int(input("spilt checks? If so how many: "))
badService = .15
goodService = .25


if serviceLevel == "Bad":
    print(float(badService * totalAmount / numOfPayers))
else: 
    print(float(badService * totalAmount / numOfPayers))