import random

def main():
    numbers = [1.5, 16.2, 17.6, 19.4 , 4.3]

    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers,3)
    print(numbers)


def append_random_numbers(numbered_list, quantity=1):
    """this function will generate a random number and append it to a list,
    args, numbered_list the list that we want to append on to
    quantity: int, how many times the function will run"""
    if quantity  <1 :
        quantity = 1
    for i in range(quantity):
        rand_num1 = random.uniform(0,100)
        rand_num2 = round(rand_num1,1)
        append_rand = numbered_list.append(rand_num2)
    return append_rand
        
    
if __name__ == "__main__":
    main()

