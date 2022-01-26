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
    Reads the data from the url and exports it to a json file.

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


def export_to_csv(data_url_path):
    """
    Reads the data from the url and exports it to a json file.

    Args:
        data_url_path (str):
            Path to the data
    """

    print("Exporting data results to CSV file...")

    csv_file = open('report_results.csv', "w", encoding="utf8")
    csv_file.write("gender; title; first; last; street_number; street_name; city; state; country; postcode; "
                   "latitude;longitude; timezone_offset; timezone_description;email; dob; age; id_name; "
                   "id_value; picture_large; picture_medium; picture_thumbnail; nationality "+"\n")
    csv_file.close()

    # Load the data as json
    r = get_report(data_url_path)
    contents = json.loads(r)

    # Write data results into a CSV
    print("Writing data results to CSV file...")
    for a1 in contents:
        if a1 == 'results':
            for a2 in contents[a1]:
                print(a2)
                val1 = a2['gender']
                print(val1)
                val2 = a2['name']['title']
                print(val2)
                val3 = a2['name']['first']
                print(val3)
                val4 = a2['name']['last']
                print(val4)
                val5 = str(a2['location']['street']['number'])
                print(val5)
                val6 = a2['location']['street']['name']
                print(val6)
                val7 = a2['location']['city']
                print(val7)
                val8 = a2['location']['state']
                print(val8)
                val9 = a2['location']['country']
                print(val9)
                val10 = str(a2['location']['postcode'])
                print(val10)
                val11 = str(a2['location']['coordinates']['latitude'])
                print(val11)
                val12 = str(a2['location']['coordinates']['longitude'])
                print(val12)
                val13 = str(a2['location']['timezone']['offset'])
                print(val13)
                val14 = a2['location']['timezone']['description']
                print(val14)
                val15 = a2['email']
                print(val15)
                val16 = str(a2['dob']['date'])
                print(val16)
                val17 = str(a2['dob']['age'])
                print(val17)
                val18 = a2['id']['name']
                print(val18)
                val19 = str(a2['id']['value'])
                print(val19)
                val20 = a2['picture']['large']
                print(val20)
                val21 = a2['picture']['medium']
                print(val21)
                val22 = a2['picture']['thumbnail']
                print(val22)
                val23 = a2['nat']
                print(val23)
                csv_file = open('report_results.csv', "a", encoding="utf8")
                print("csv file opened")
                csv_file.write(val1 + ";" + val2 + ";" + val3 + ";" + val4 + ";" + val5 + ";" + val6 + ";" + val7 + ";"
                               + val8 + ";" + val9 + ";" + val10 + ";" + val11 + ";" + val12 + ";" + val13 + ";" + val14
                               + ";" + val15 + ";" + val16 + ";" + val17 + ";" + val18 + ";" + val19 + ";" + val20 + ";"
                               + val21 + ";" + val22 + ";" + val23 + "\n")
                csv_file.close()
        else:
            continue

    print("Export finished")


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
        2 - Export data results to CSV file
        """
        )

        option = input("Your option: ")  # What To Do ???
        print()

        if option == "0":
            print("Good bye!")
        elif option == "1":
            export_to_json(data_url_path)
        elif option == "2":
            export_to_csv(data_url_path)
        else:
            print(" ### Wrong option ### ")


# Main program
main()
