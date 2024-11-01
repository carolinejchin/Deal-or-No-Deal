import random
import time
import math
import sys

d = {}
case_amounts = [0, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
rand_index = random.sample(range(0, 26), 26)

for x in range(0, 26):
    d[x + 1] = case_amounts[rand_index[x]]
# print(d)
available_cases = list(d.keys())
print(f"Available cases: {available_cases}")
str(case_amounts)
print()

while True:
    try:
        personal_case = int(input("Select your personal case: "))
        if 1 <= personal_case <= 26:
            print(f"Your personal case: {personal_case}")
            print()
            break
        else:
            print("Please enter a number between 1 and 26.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

available_cases.remove(personal_case)

def select_cases(count):
    while count > 0:
        while True:
            try:
                print(f"Status of cases: {case_amounts}")
                print()
                print(f"Available cases: {available_cases}")
                case1 = int(input(f"Select {count} cases: "))
                if case1 in available_cases:
                    print()
                    print()
                    print(f"Amount that was in case {case1}: {d[case1]}")
                    print()
                    available_cases.remove(case1)
                    case_amounts[case_amounts.index(d[case1])] = f"--{d[case1]}--"
                    break
                else:
                    print()
                    print("Please enter an available case number")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        count -= 1

previous_offers = []

def offer():
    sum = d[personal_case]
    for x in available_cases:
        sum += d[x]
    expected = sum / (len(available_cases) + 1)
    cases_remaining = len(available_cases)
    maximum = max(available_cases)
    return int(round((12275.30 + (0.748 * expected) - (2714.74 * cases_remaining) - (0.40 * maximum) + (.0000006986 * expected**2) + (32.623 * cases_remaining**2)), -3))

def banker():
    print(f"Status of cases: {case_amounts}")
    print()
    print("The banker is calling... ")
    time.sleep(3)
    print(f"Here's their offer: {offer()}")
    time.sleep(3)
    print()
    print(f"Previous offers: {previous_offers}")
    print()
    
    while True:
        try:
            print("DEAL OR NO DEAL?")
            deal = input("y for DEAL, n for NO DEAL ")

            if deal == "y":
                print()
                print(f"Congrats! You won ${offer()}")
                time.sleep(3)
                print(f"Your case had: ${d[personal_case]}")
                return True
            elif deal == "n":
                print()
                print("NO DEAL")
                previous_offers.insert(0, offer())
                return False
            else:
                print()
                print("Please enter y or n")
        except ValueError:
            print()
            print("Invalid input. Please enter y or n.")

#Actual simulation
select_cases(6)
done = banker()

if done:
    print("Game Over")
    sys.exit()

select_cases(5)
done = banker()

if done:
    print("Game Over")
    sys.exit()

select_cases(4)
done = banker()

if done:
    print("Game Over")
    sys.exit()

select_cases(3)
done = banker()

if done:
    print("Game Over")
    sys.exit()

select_cases(2)
done = banker()

if done:
    print("Game Over")
    sys.exit()

select_cases(1)
done = banker()

if done:
    print("Game Over")
    sys.exit()

select_cases(1)
done = banker()

if done:
    print("Game Over")
    sys.exit()

select_cases(1)
done = banker()

if done:
    print("Game Over")
    sys.exit()

select_cases(1)
done = banker()

if done:
    print("Game Over")
    sys.exit()

print("Your deal: Your case")
time.sleep(3)
print(f"Congrats! You won ${d[personal_case]}")
print("Game Over")
