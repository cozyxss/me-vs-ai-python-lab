# Function that prints a rectangle made of 0s

def rectangle_printer():
    print("Creating Rectangle Printer")
    print("Please enter a width of your choice:")
    rect_width = input(">")

    for _ in range(5):
        for _ in range(int(rect_width)):
            print("0", end="")
        print()


# Function that calculates rectangle area and perimeter

def rectangle_calculator():
    print("Enter the width for the rectangle")
    rect_width = int(input(">"))

    print("Enter the length for the rectangle")
    rect_len = int(input(">"))

    rect_area = rect_width * rect_len
    rect_perimeter = 2 * (rect_width + rect_len)

    print("Area of the rectangle:" + str(rect_area))
    print("Perimeter of the rectangle:" + str(rect_perimeter))


def main():
    while True:
        print("\nSelect an option:")
        print("1 - Rectangle Printer")
        print("2 - Perimeter and Area Calculator")
        print("0 - Exit")

        choice = input("> ")

        if choice == "1":
            rectangle_printer()
        elif choice == "2":
            rectangle_calculator()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
