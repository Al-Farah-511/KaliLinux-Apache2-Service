#!/usr/bin/env python3

import os
import subprocess
import sys

def print_banner():
    print("""
    Hello M@TE !
    Welcome to Apache2 Script :)

    Coded By Al Farah
    The 511
    Digital Security Research Group
    """)

def print_menu():
    print("""
    Select a Method:
    [1] Start Apache2
    [2] Stop Apache2
    [3] Restart Apache2
    [4] Open Localhost
    [0] Exit
    """)

def manage_apache(action):
    service_name = "apache2"
    systemctl_cmd = f"systemctl {action} {service_name}"
    
    try:
        subprocess.run(
            systemctl_cmd.split(),
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Apache2 service {action}ed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to {action} Apache2 service.")
        print(f"Error: {e.stderr.strip()}")

def open_localhost():
    try:
        subprocess.run(["xdg-open", "http://localhost"], check=True)
        print("Localhost opened in your default browser!")
    except subprocess.CalledProcessError as e:
        print("Failed to open localhost.")
        print(f"Error: {e.stderr.strip()}")

def main():
    if os.geteuid() != 0:
        print("This script must be run as root. Use sudo.")
        sys.exit(1)

    while True:
        print_banner()
        print_menu()
        choice = input("Number-# ")

        if choice == "1":
            manage_apache("start")
        elif choice == "2":
            manage_apache("stop")
        elif choice == "3":
            manage_apache("restart")
        elif choice == "4":
            open_localhost()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
