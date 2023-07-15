#!/usr/bin/env python3
import subprocess
import os
import sys


def display():
    """Display the welcome message and provide details about the script."""
    print("Welcome to Debian Cleaner")
    print("This script performs the following actions:")
    print("1: Update System and Packages")
    print("2: Clean package cache")
    print("3: Remove unnecessary packages")
    print("4: Remove unused dependencies")


def update():
    print("Running Update System")
    subprocess.run(["sudo", "apt-get", "update"])

    print("Cleaning package cache")
    subprocess.run(["sudo", "apt", "clean"])

    print("Removing unnecessary packages")
    subprocess.run(["sudo", "apt", "autoremove"])

    print("Removing unused dependencies")
    subprocess.run(["sudo", "apt", "autoremove", "--purge"])

    print("Update Complete")


if __name__ == "__main__":
    # Checking if the script is running with root permissions
    if os.geteuid() != 0:
        print("This script needs to be run with root privileges.")
        sys.exit(1)

    display()
    update()
