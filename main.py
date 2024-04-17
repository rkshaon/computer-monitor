from os_details import main as os_details
from network_speed_monitor import main as network_speed_monitor



def main():
    while True:
        print("\nMenu:")
        print("Input 1 to get OS details")
        print("Input 2 to Monitor Internet Speed")
        print("x. Exit")

        choice = input("\nEnter your choice: ")
        print(f"\n")

        if choice == "1":
            os_details.main()
        elif choice == "2":
            network_speed_monitor.main()
        elif choice == "x":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
