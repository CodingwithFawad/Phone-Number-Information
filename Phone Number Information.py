import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Capture the phone number input
phone_number_str = input("Enter the phone number: ")
print()
phone_number = phonenumbers.parse(phone_number_str, "en")

# Define functions to fetch various details of the phone number

def get_phone_number_info():
    """Fetch and display country, carrier, and time zone information."""
    country = geocoder.description_for_number(phone_number, "en")
    carrier_name = carrier.name_for_number(phone_number, "en")
    time_zone = timezone.time_zones_for_number(phone_number)
    
    print("Country:", country)
    print("Carrier:", carrier_name)
    print("Time Zone:", time_zone)

def get_phone_number_formats():
    """Fetch and display national and international phone number formats."""
    national_format = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    international_format = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    
    print("National Format:", national_format)
    print("International Format:", international_format)

def check_phone_number_validity():
    """Check and display if the phone number is valid."""
    is_valid = phonenumbers.is_valid_number(phone_number)
    
    print("Is Valid:", is_valid)

def get_possible_regions():
    """Fetch and display possible regions associated with the phone number."""
    possible_regions = geocoder.description_for_valid_number(phone_number, "en")
    
    print("Possible Regions:", possible_regions)

def get_region_info():
    """Fetch and display the region code of the phone number."""
    region_info = phonenumbers.region_code_for_number(phone_number)
    
    print("Region Code:", region_info)
    print()

# Execute functions to fetch details and display them
get_phone_number_info()
get_phone_number_formats()
check_phone_number_validity()
get_possible_regions()
get_region_info()

# List to store all results
results = []

# Redefine functions to fetch details and append them to results list

def get_phone_number_info():
    country = geocoder.description_for_number(phone_number, "en")
    carrier_name = carrier.name_for_number(phone_number, "en")
    time_zone = timezone.time_zones_for_number(phone_number)
    
    results.append(f"Country: {country}")
    results.append(f"Carrier: {carrier_name}")
    results.append(f"Time Zone: {time_zone}")

def get_phone_number_formats():
    national_format = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    international_format = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    
    results.append(f"National Format: {national_format}")
    results.append(f"International Format: {international_format}")

def check_phone_number_validity():
    is_valid = phonenumbers.is_valid_number(phone_number)
    
    results.append(f"Is Valid: {is_valid}")

def get_possible_regions():
    possible_regions = geocoder.description_for_valid_number(phone_number, "en")
    
    results.append(f"Possible Regions: {possible_regions}")

def get_region_info():
    region_info = phonenumbers.region_code_for_number(phone_number)
    
    results.append(f"Region Code: {region_info}")

# Execute functions again to fetch details and append them to results list
get_phone_number_info()
get_phone_number_formats()
check_phone_number_validity()
get_possible_regions()
get_region_info()

# Ask the user if they want to save the results to a text file
save_option = input("Do you want to save the results to a text file? (yes/no): ").lower()

if save_option == "yes":
    with open("phone_number_details.txt", "w") as file:
        file.write(f"Phone Number: {phone_number_str}\n")
        for result in results:
            file.write(result + "\n")
    print("Results saved to 'phone_number_details.txt'")
else:
    print("Results not saved.")
