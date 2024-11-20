import base64
import re
import platform
import os

try:
    # Check and install the required modules
    import requests
except ImportError:
    os.system("python3 -m pip install requests -q -q -q")
    import requests

try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()  # Initialize colorama
except ImportError:
    os.system("python3 -m pip install colorama -q -q -q")
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()  # Initialize colorama after importing

try:
    from pystyle import Colors, Colorate, Center
except ImportError:
    os.system("python3 -m pip install pystyle -q -q -q")
    from pystyle import Colors, Colorate, Center

# Banner display
banner = Center.XCenter(r"""********************************************************************
*        ___   _              __     __   _____ _  __     __        *
*       / / \ | |_   _ _ __ __\ \   / /__|___ /(_)/ _|_   \ \       *
*      | ||  \| | | | | '_ ` _ \ \ / / _ \ |_ \| | |_| | | | |      *
*     < < | |\  | |_| | | | | | \ V /  __/___) | |  _| |_| |> >     *
*      | ||_| \_|\__,_|_| |_| |_|\_/ \___|____/|_|_|  \__, | |      *
*       \_\                                           |___/_/       *
*                                                                   *
*           OSINT TOOL TO FIND MOBILE INFO, LOCATION AND VALIDITY   *
*                                                                   *
*                    Coded By: Machine1337                          *
*********************************************************************
          Note: Enter Number with country code but without +
                          (9123456789098)
""")

# Validate mobile number format


def is_valid_mobile_number(mobile_number):
    pattern = re.compile(r"^\d{10,15}$")  # Allow 10 to 15 digits
    return pattern.match(mobile_number) is not None

# Main function to check the mobile number


def check_number():
    try:
        # Clear the console
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))

        mobile_number = input(Fore.GREEN + '\n[+] Enter Mobile Number: ')
        if is_valid_mobile_number(mobile_number):
            # Decode the API URL and key
            message = base64.b64decode(
                'aHR0cHM6Ly9hcGkuYXBpbGF5ZXIuY29tL251bWJlcl92ZXJpZmljYXRpb24vdmFsaWRhdGU/bnVtYmVyPQ=='.encode(
                    'ascii')).decode('ascii')
            url = f"{message}{mobile_number}"
            api_key = base64.b64decode(
                'dGdDckRFOVF0QVF4Q1lvNnk4dHprMUdtQTJKbzBYZmI='.encode('ascii')).decode('ascii')

            # Send the request
            headers = {"apikey": f"{api_key}"}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                # Parse and display the response JSON
                response_json = response.json()
                print(f"""
Country code: {response_json.get("country_code", "N/A")}
Number: {response_json.get("number", "N/A")}
Country name: {response_json.get("country_name", "N/A")}
Country prefix: {response_json.get("country_prefix", "N/A")}
International format: {response_json.get("international_format", "N/A")}
Line type: {response_json.get("line_type", "N/A")}
Local format: {response_json.get("local_format", "N/A")}
Location: {response_json.get("location", "N/A")}
Valid: {response_json.get("valid", "N/A")}
""")
            else:
                # Display error if response is not successful
                print(Fore.RED + f"Error: {response.status_code}")
        else:
            # Invalid mobile number input
            print(Fore.RED + '[*] Invalid Mobile Number....')
    except KeyboardInterrupt:
        # Handle user interrupt
        print(Fore.RED + '\n[*] You Pressed The Wrong Button....')
    except Exception as e:
        # Handle unexpected errors
        print(Fore.RED + f'\n[*] Unexpected error: {str(e)}')


# Call the main function
if __name__ == "__main__":
    check_number()
