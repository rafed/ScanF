import random
import os
from datetime import datetime
from fuzzywuzzy import fuzz
import string

from model.field import Field
from model.constraint import Constraint

string_types = ['text', 'password', 'color', 'date', 'datetime-local', 'email', 'month', 'search', 'tel', 'url', 'week']
number_types = ['number', 'range']
click_types = ['radio', 'checkbox']
# time, date

class AutoFormFill:
    @staticmethod
    def fillForm(form_id):
        fields = Field.query.filter(Field.form_id == form_id).all()
        fields = [x.as_dict() for x in fields]

        new_form = {}

        for field in fields:
            if field['name'] is None:
                continue

            constraints = Constraint.query.filter(Constraint.field_id==field['id']).all()
            constraints = [x.as_dict() for x in constraints]

            min = 0
            max = 100
            maxlength = 10

            for c in constraints:
                if c['type'] == 'maxlength': maxlength=c['value']
                if c['type'] == 'min': min=c['value']
                if c['type'] == 'max': max=c['value']

            if field['type'] in number_types:
                new_form[field['name']] = randomNumber(min, max)
                
            elif field['type'] == 'date':
                new_form[field['name']] = datetime.now().strftime("%Y-%m-%d")
            elif field['type'] == 'time':
                new_form[field['name']] = datetime.now().strftime("%H:%M:%S")

            elif field['type'] in string_types:
                data = os.listdir("data/forms")
                fuzz_val = 0
                fuzz_name = ''

                for d in data:
                    if fuzz.ratio(field['name'], d) > fuzz_val:
                        fuzz_val = fuzz.ratio(field['name'], d)
                        fuzz_name = d

                if fuzz_val < 20:
                    new_form[field['name']] = randomString(int(maxlength))
                else:
                    lines = open('data/forms/' + fuzz_name).read().splitlines()
                    line = random.choice(lines)
                    new_form[field['name']] = line

            elif field['type'] in click_types:
                new_form[field['name']] = field['default_value']

            else:
                new_form[field['name']] = randomString(int(maxlength))

        return new_form


def randomNumber(min, max):
    return random.randint(min, max)

def randomString(length):
    print(length)
    return ''.join(random.choice(string.ascii_letters) for x in range(length))