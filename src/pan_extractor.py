import re

def extract_pan_details(text):

    pan_pattern = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"
    dob_pattern = r"\d{2}/\d{2}/\d{4}"

    pan = re.findall(pan_pattern, text)
    dob = re.findall(dob_pattern, text)

    lines = text.split("\n")

    name = ""
    father_name = ""

    for i,line in enumerate(lines):

        if "Name" in line or "NAME" in line:
            name = lines[i+1]

        if "Father" in line or "FATHER" in line:
            father_name = lines[i+1]

    data = {
        "PAN_Number": pan[0] if pan else "",
        "Name": name,
        "Father_Name": father_name,
        "Date_of_Birth": dob[0] if dob else ""
    }

    return data
