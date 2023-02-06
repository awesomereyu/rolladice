import random
response = str(input("Do you want to roll a dice?(y/n)"))
while response == "y":
    response = str(input("Do you want to roll a dice?(y/n)"))
no = random.randint(1,6)
if no == 1:
    print("[-----]")
    print("[     ]")
    print("[  1  ]")
    print("[     ]")
    print("[-----]")
elif no ==2:
    print("[-----]")
    print("[     ]")
    print("[  2  ]")
    print("[     ]")
    print("[-----]")
elif no ==3:
    print("[-----]")
    print("[     ]")
    print("[  3  ]")
    print("[     ]")
    print("[-----]")
elif no ==4:
    print("[-----]")
    print("[     ]")
    print("[  4  ]")
    print("[     ]")
    print("[-----]")
elif no==5:
    print("[-----]")
    print("[     ]")
    print("[  5  ]")
    print("[     ]")
    print("[-----]")
elif no ==6:
    print("[-----]")
    print("[     ]")
    print("[  6  ]")
    print("[     ]")
    print("[-----]")