from collections import deque


def display_queues(preparing_queue, serving_queue):
    print("\n--- Now Preparing ---")
    print(list(preparing_queue) if preparing_queue else "Empty")
    print("\n--- Now Serving ---")
    print(list(serving_queue) if serving_queue else "Empty")


def main():
    preparing_queue = deque()
    serving_queue = deque()

    while True:
        display_queues(preparing_queue, serving_queue)
        print("\nOptions:")
        print("1. Add order")
        print("2. Move prepared order Now Serving")
        print("3. Remove order from Now Preparing")
        print("4. Remove order from Now Serving")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            order_number = input("Enter order number: ")
            if order_number in preparing_queue or order_number in serving_queue:
                print("Error: Duplicate order number detected.")
            else:
                preparing_queue.append(order_number)
                print(f"Order {order_number} added to Now Preparing queue.")

        elif choice == "2":
            if preparing_queue:
                order_number = input("Enter order number to move: ")
                if order_number in preparing_queue:
                    preparing_queue.remove(order_number)
                    serving_queue.append(order_number)
                    print(f"Order {order_number} moved to Now Serving queue.")
                else:
                    print("Error: Order number not found in Now Preparing queue.")
            else:
                print("No orders in Now Preparing queue.")

        elif choice == "3":
            if preparing_queue:
                order_number = input("Enter order number to remove: ")
                if order_number in preparing_queue:
                    preparing_queue.remove(order_number)
                    print(f"Order {order_number} removed from Now Preparing queue.")
                else:
                    print("Error: Order number not found in Now Preparing queue.")
            else:
                print("No orders in Now Preparing queue.")

        elif choice == "4":
            if serving_queue:
                order_number = input("Enter order number to remove: ")
                if order_number in serving_queue:
                    serving_queue.remove(order_number)
                    print(f"Order {order_number} removed from Now Serving queue.")
                else:
                    print("Error: Order number not found in Now Serving queue.")
            else:
                print("No orders in Now Serving queue.")

        elif choice == "5":
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
