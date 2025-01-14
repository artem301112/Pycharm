def display_even_numbers_reverse(n):

    even_numbers = []

    for i in range(n, 0, -1):

        if i % 2 == 0:
            even_numbers.append(i)

    result = ' '.join(map(str, even_numbers))

    print(result)


n = int(input("Enter a number: "))
display_even_numbers_reverse(n)