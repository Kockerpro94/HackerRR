while True:
    user_input = input("type to see this is ip IPv4 or IPv6: ")
    user_input_number = len(user_input)
    if '.' in user_input and user_input_number > 10:
        print("This is an IPv4 address.")
        break
    if '192.168.' in user_input:
        print("This is a private IPv4 address.")
        break   
    if user_input_number < 11 and ':' in user_input:
        print("This is an IPv6 address.")
        break
    if user_input == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Error: Invalid input. Please try again.")