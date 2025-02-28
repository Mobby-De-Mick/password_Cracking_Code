import subprocess

# Get all WLAN profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Extract the profile names
profiles = [i.split(":")[1].strip() for i in data if "All User Profile" in i]

# Print header
print("\n{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("--------------------")

# Iterate through profiles
for i in profiles:
    # Ensure 'i' is properly inserted in the argument list as a string
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8').split(
            '\n')

        # Extract the key content if found
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        # Print profile and its password
        if results:
            print("{:<30} | {:<}".format(i, results[0]))
        else:
            # If no password is found, print empty
            print("{:<30} | {:<}".format(i, ""))
    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails (e.g., profile not found)
        print("{:<30} | {:<}".format(i, "Error retrieving details"))
