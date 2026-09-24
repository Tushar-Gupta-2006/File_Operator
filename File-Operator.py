import os
from datetime import datetime
print("Welcome to personal Journal Manager !")

print("")

class JournalManager:
    def __init__(self):
        self.file = "journal.txt"

    def add_entry(self):
        entry = input("Enter your journal entry: ")
        try:
            with open(self.file, "a") as f:
                f.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}]\n{entry}\n\n")
            print("Entry added successfully!")
            print("---------------------------------------------")
            print("")
        except PermissionError:
            print("Permission denied.")
            print("---------------------------------------------")
            print("")

    def view_entry(self):
        try:
            with open(self.file, "r") as f: 
                print("Your Journal Entries : ")
                print("")
                data = f.read()
                print(data if data else "No journal entries found.")
                print("---------------------------------------------")
                print("")
        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry.")
            print("---------------------------------------------")
            print("")

    def search_entry(self):
        key = input("Enter a keyword or date to search: ")
        try:
            with open(self.file, "r") as f:
                data = f.read()

            found = [x for x in data.split("\n\n") if key.lower() in x.lower()]

            if found:
                print("\nMatching Entries:")
                print("")
                print("\n\n".join(found))
                print("---------------------------------------------")
                print("")
            else:
                print(f"No entries were found for the keyword: {key}.")
                print("---------------------------------------------")
                print("")
        except FileNotFoundError:
            print("Error: The journal file does not exist.")
            print("---------------------------------------------")
            print("")

    def delete_entry(self):
        if not os.path.exists(self.file):
            print("No journal entries to delete.")
            print("---------------------------------------------")
            print("")
            return

        if input("Are you sure? (yes/no): ").lower() == "yes":
            os.remove(self.file)
            print("All journal entries have been deleted.")
            print("---------------------------------------------")
            print("")

    def run(self):
        while True:
            print("Please select an option:")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            print("")
            print("--------------------------------")
            choice = input("User Input : ")
            print("--------------------------------")
            print("")

            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.view_entry()
            elif choice == "3":
                self.search_entry()
            elif choice == "4":
                self.delete_entry()
            elif choice == "5":
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please select a valid option from the menu.")

JournalManager().run()