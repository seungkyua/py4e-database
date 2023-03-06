# Enter: 7, 2, bob, 10, 4, done
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = n
        smallest = n
    else:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)