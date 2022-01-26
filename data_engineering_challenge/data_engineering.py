# Import required packages
import requests


def get_report(data_url_path):
    """
    Reads the data from the url and converts to text.
    Additionally, it gives a report about data results.

    Args:
        data_url_path (str):
            Path to the data
    """

    print("Getting data results...")

    # Values used to determine the data included in the report instance – such as attribute values,
    # metric values and view filters. JSON format. Leave empty to import everything
    data_details = ""
    r = requests.get(data_url_path, data=data_details)
    if r.ok:
        print("Data results received...")
        print("HTTP %i - %s" % (r.status_code, r.reason))
        return r.text
    else:
        print("HTTP %i - %s" % (r.status_code, r.reason))


def export_to_json(data_url_path):
    """
    Reads the data and exports it to a json file.

    Args:
        data_url_path (str):
            Path to the data
    """

    print("Exporting data results to JSON file...")
    r = get_report(data_url_path)
    text_file = open("results.json", "w", encoding="utf8")
    text_file.write(r)
    print("Exported data results to JSON file...")
    text_file.close()


def main():
    # Path to data url
    data_url_path = "https://randomuser.me/api/?results=300&nat=de,dk,fr,gb&inc=id,gender,name,location,email,dob,picture,nat&seed=flightright"

    option = None
    while option != "0":
        print(
            """
        ---MENU---

        0 - Exit
        1 - Export data results to JSON file
        """
        )

        option = input("Your option: ")  # What To Do ???
        print()

        if option == "0":
            print("Good bye!")
        elif option == "1":
            export_to_json(data_url_path)
        else:
            print(" ### Wrong option ### ")


# Main program
main()
