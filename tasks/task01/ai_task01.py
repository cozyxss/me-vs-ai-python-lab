def get_positive_int(prompt):
    """Kullanıcıdan pozitif tam sayı alır."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Value must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def print_rectangle(width, height, char="0"):
    """Belirtilen karakterle dikdörtgen basar."""
    for _ in range(height):
        print(char * width)


def rectangle_printer():
    print("\nRectangle Printer")
    width = get_positive_int("Width: ")
    height = get_positive_int("Height: ")
    char = input("Character to use (default 0): ") or "0"

    print("\nResult:")
    print_rectangle(width, height, char)


def rectangle_calculator():
    print("\nRectangle Calculator")
    width = get_positive_int("Width: ")
    height = get_positive_int("Height: ")

    area = width * height
    perimeter = 2 * (width + height)

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


def show_menu():
    print("\nSelect an option:")
    print("1 - Rectangle Printer")
    print("2 - Rectangle Area and Perimeter Calculator")
    print("0 - Exit")


def main():
    actions = {"1": rectangle_printer, "2": rectangle_calculator}

    while True:
        show_menu()
        choice = input("> ")

        if choice == "0":
            print("Exiting program.")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
