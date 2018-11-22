import requests
from bs4 import BeautifulSoup
import json

# website = "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_attributes_readonly"
website = "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elem_select_multiple"
skip = ["submit", "reset", "button", "file"]

r = requests.get(website)
soup = BeautifulSoup(r.text, "html.parser")

form = soup.find('form')

form_action = form.get('action')
method = form.get('method')

fields = form.findAll('input')

field_list = []

for field in fields:
    attr = {}
    constraint = {}
    
    attr_type = field.get('type')
    if attr_type in skip:
        continue

    if field.has_attr('disabled'):
        continue

    attr['type'] = attr_type
    attr['name'] = field.get('name')
    attr['value'] = field.get('value')

    # if field.has_attr('readonly'):
    #     constraint['readonly'] = True
    constraint['size'] = field.get('size')
    constraint['maxlength'] = field.get('maxlength')
    constraint['multipart/form-data'] = field.get('multipart/form-data')
    constraint['min'] = field.get('min')
    constraint['max'] = field.get('max')
    constraint['pattern'] = field.get('pattern')


    j = {'attributes':attr, 'constraints':constraint}
    field_list.append(j)


for f in field_list:
    print(json.dumps(f, indent=2))

# color, date, datetime-local, email, number(min, max), range, tel, time, url, week