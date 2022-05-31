# Read file
from datetime import datetime


def replaceText(text):
    filters = [["[COMPANY_NAME]", "COMPANY_NAME"],
               ["[EMPLOYEE_NAME]", "EMPLOYEE_NAME"],
               ["[CITY]", "CITY_NAME"],
               ["[COUNTRY]", "COUNTRY_NAME"]

               ]

    for filter in filters:
        print("What is the " + filter[1] + "?")
        textInput = input()
        text = text.replace(filter[0], textInput)
    return text.replace("[CURRENT_DATE]", datetime.today().strftime('%Y-%m-%d'))


contractFile = open("contract.txt", "r")
result = ""
for row in contractFile:
    result += row
result = replaceText(result)


with open("contract_processed.txt", "w") as textFile:
    textFile.write(result)
