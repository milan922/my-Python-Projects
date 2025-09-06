# Movie Ticket Booking System

# Constants
ROWS = 5
COLUMNS = 5
ticket_price = 150

# Initialize seat layout (2D list)
seats = [["O" for _ in range(COLUMNS)] for _ in range(ROWS)]  # O = Open, X = Booked
booked = {}

# Function to display seats
def display_seats():
    print("\nSeat Layout (O = Open, X = Booked):")
    print("   " + " ".join(str(i+1) for i in range(COLUMNS)))
    for i in range(ROWS):
        print(f"{i+1}  " + " ".join(seats[i]))
    print()

# Book a ticket
def book_seat():
    display_seats()
    row = int(input("Enter row number (1-5): ")) - 1
    col = int(input("Enter column number (1-5): ")) - 1

    if row < 0 or row >= ROWS or col < 0 or col >= COLUMNS:
         print("❌ Invalid seat number.")
         return

    if seats[row][col] == "X":
        print("❌ Seat already booked!")
    else:
        name = input("Enter your name: ")
        seats[row][col] = "X"
        seat_number = f"R{row+1}C{col+1}"
        booked[seat_number] = name
        print(f"✅ Seat {seat_number} successfully booked for {name}.")

# View bookings
def view_bookings():
    if not booked:
        print("No bookings yet.")
    else:
        print("\n📒 Booked Seats:")
        for seat, name in booked.items():
            print(f"{seat} - {name}")
        print()

# View total income
def view_income():
    total = len(booked) * ticket_price
    print(f"\n💰 Total Income: ₹{total}\n")

# Main program loop
while True:
    print("\n--- Movie Ticket Booking System ---")
    print("1. Show Seats")
    print("2. Book a Seat")
    print("3. View Booked Seats")
    print("4. View Total Income")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_seats()
    elif choice == '2':
        book_seat()
    elif choice == '3':
        view_bookings()
    elif choice == '4':
        view_income()
    elif choice == '5':4

    print("Thank you for using the system!" )
    break
else:
    print("❌ Invalid choice. Tryagain.")
