import socket


def get_ip_address() -> str:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    return ip_address


def main():
    ip_address = get_ip_address()
    print(f"Your Computer IP Address is: {get_ip_address()}")


if __name__ == "__main__":
    main()
