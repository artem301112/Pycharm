def display_numbers():
    from_num = int(input("Enter the starting number: "))
    to_num = int(input("Enter the ending number: "))

    print(f"The numbers from {from_num} to {to_num} are:")
    for number in range(from_num, to_num + 1):
        print(number)


display_numbers()
