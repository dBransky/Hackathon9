import requests
import json

def get_doctor_fax(name):
    url = 'https://serguide.maccabi4u.co.il/webapi/api/SearchPage/GetSearchPageSearch/'
    data = {
        "DocName": name,
        "ChapterId": "001",
        "InitiatorCode": "001",
        "isKosher": 0,
        "IsMobileApplication": 0,
        "PageNumber": 1,
    }

    response = requests.post(url, data=data)
    phone_numbers = json.loads(response.content)['Items'][0]['PHONENUMBERS']
    curr_phone = 0
    fax = None
    for phone_entry in phone_numbers:
        if phone_entry['Title'] == "פקס":
            fax = phone_entry['Value']
    
    return fax if fax else 0

print(get_doctor_fax('אופיר יוסף '))