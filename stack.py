stack = []

# Push operation
def push_book():
    book = input("Enter book name to add: ")
    stack.append(book)
    print(f'"{book}" added to stack.')

# Pop operation
def pop_book():
    if len(stack) == 0:
        print("Stack is empty. Nothing to remove.")
    else:
        removed = stack.pop()
        print(f'"{removed}" removed from stack.')

# Display operation
def display_stack():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("\nBooks in stack (Top to Bottom):")
        for book in reversed(stack):
            print(book)

# Menu-driven program
while True:
    print("\n--- STACK MENU ---")
    print("1. Push Book")
    print("2. Pop Book")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push_book()
    elif choice == 2:
        pop_book()
    elif choice == 3:
        display_stack()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")