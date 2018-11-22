from services.form_parser import FormParser
import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

url = "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_date_max_min"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

forms = soup.findAll('form')
# print(forms)

for form in forms:
    # print(form)
    # print('\n\n\n')
    f = FormParser(url, form)

    # print(f.get_action())
    # print(f.get_method())
    # j = json.loads(str(f.get_fields()))
    # print(j.dumps(ident=2))

    pprint(f.get_fields())
