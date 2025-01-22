from colorama import Fore, Style, init
import qrcode
import os

# Initialize colorama
init(autoreset=True)

# Options menu
options = {
    0: "Exit",
    1: "Add New QR Code",
    2: "Show QR Codes",
    3: "Delete QR Code"
}

# Directory to save QR codes
output_dir = "qr_codes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to display menu
def display_menu():
    print(Fore.GREEN + "नवयुवक छात्र सरस्वती पूजा समिति के सभी माननीय सदस्यों को यह सूचित किया जाता है कि समिति के सभी सदस्यों के लिए पहचान पत्र जारी किया जाना है।")
    print(Style.BRIGHT + "Options:")
    for key, value in options.items():
        print(f"{key}: {value}")

# Function to add a new QR code
def add_qr_code():
    print(Fore.YELLOW + "\nEnter the following details:")
    name = input("1. नाम: ")
    position = input("2. पद का नाम: ")
    address = input("3. पता: ")
    blood_group = input("4. ब्लड ग्रुप: ")
    aadhaar = input("5. आधार संख्या: ")
    email = input("6. ईमेल आईडी: ")
    phone = input("7. दूरभाष संख्या: ")

    # Create data string
    data = f"""
    नाम: {name}
    पद का नाम: {position}
    पता: {address}
    ब्लड ग्रुप: {blood_group}
    आधार संख्या: {aadhaar}
    ईमेल आईडी: {email}
    दूरभाष संख्या: {phone}
    """

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image
    filename = f"{output_dir}/{name.replace(' ', '_')}.png"
    img.save(filename)
    print(Fore.GREEN + f"QR code for {name} saved as {filename}.\n")

# Function to list existing QR codes
def show_qr_codes():
    files = os.listdir(output_dir)
    if not files:
        print(Fore.RED + "No QR codes found.\n")
        return
    print(Fore.CYAN + "Existing QR codes:")
    for file in files:
        print(f"- {file}")
    print()

# Function to delete a QR code
def delete_qr_code():
    show_qr_codes()
    filename = input("Enter the name of the QR code file to delete (without extension): ")
    filepath = f"{output_dir}/{filename}.png"
    if os.path.exists(filepath):
        os.remove(filepath)
        print(Fore.GREEN + f"Deleted {filename}.png.\n")
    else:
        print(Fore.RED + "File not found.\n")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input(Fore.BLUE + "Choose an option: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                print(Fore.GREEN + "Exiting program. Thank you!")
                break
            elif choice == 1:
                add_qr_code()
            elif choice == 2:
                show_qr_codes()
            elif choice == 3:
                delete_qr_code()
            else:
                print(Fore.RED + "Invalid choice. Try again.\n")
        else:
            print(Fore.RED + "Please enter a valid number.\n")

# Run the program
if __name__ == "__main__":
    main()
