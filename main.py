import os

from os_details import main as os_details
from network_speed_monitor import main as network_speed_monitor
from loader import main as loader



def main():
    while True:
        print("\nMenu:")
        print("Input 1 to get OS details")
        print("Input 2 to Monitor Internet Speed")
        print("3")
        print("Press c to clear the screen")
        print("Press x to exit\n")

        choice = input("\nEnter your choice: ")
        print(f"\n")

        if choice == "1":
            os_details.main()
        elif choice == "2":
            network_speed_monitor.main()
        elif choice == "3":
            loader.main()
        elif choice == "c":
            os.system("clear")
        elif choice == "x":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
