file = open("detail.txt", "a")

# Loop to input details for 5 destinations
destinations = []  # create an empty list to store destination details
for i in range(1, 3):
    from_location = input("From: ")
    to_location = input("To: ")
    depart_time = input("Depart Time: ")
    adult_price = input("Adult Price: ")
    child_price = input("Child Price: ")
    destinations.append([from_location, to_location, depart_time, adult_price, child_price])  # add the destination details to the list

    # Write the details to the "detail.txt" file
    file.write(str(i))
    print("")
#file.close()
# Loop to input customer details
for i in range(1,6):
    ticket_id = int(input("Enter the Ticket id: "))
    destination_num = int(input("Enter the destination number (1-5): "))
    from_location, to_location, depart_time, adult_price, child_price = destinations[destination_num-1]  # get the destination details from the list using the destination number

    num_adults = int(input("Number of Adults: "))
    num_children = int(input("Number of Children: "))

    total_payment = (float(num_adults) * float(adult_price)) + (float(num_children) * float(child_price))

    # Print the details entered by the user
    print("\nDetails Entered:")
    print("Ticket ID:", ticket_id)
    print("From:", from_location)
    print("To:", to_location)
    print("Depart Time:", depart_time)
    print("Number of Adults:", num_adults)
    print("Number of Children:", num_children)
    print("Total Payment: RM", "{:.0f}".format(float(total_payment)))

    # Write the details to the "detail.txt" file
    print("\n")
    file.write(str(ticket_id) + "  " + from_location + "  " + to_location + "  " + str(num_adults) + "  " + str(num_children) + "  " + "{:.0f}".format(total_payment) + "\n")

    # Display message for the next customer
    print("\nDetails saved for Ticket ID", ticket_id)
    print("--------------------------------------------------")

# Close the "detail.txt" file
file.close()