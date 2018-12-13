from urllib.parse import urlparse, urljoin

allTextInputTypes = ['text', 'password', 'color', 'date', 'datetime-local', 'email', 'month', 'number', 'range', 'search', 'tel', 'time', 'url', 'week']

class FormParser:
    def __init__(self, baseurl, soup):
        self.form = soup
        self.baseurl = baseurl

    def parse(self, baseurl, soup):
        pass

    def get_action(self):
        action = self.form.get('action')
        if action is None:
            action = ''
        return urljoin(self.baseurl, action)

    def get_method(self):
        m = self.form.get('method')
        if m is None:
            return 'get'
        return m

    def get_fields(self):
        field_list = []
        
        for x in self._get_text():
            field_list.append(x)

        for x in self._get_textArea():
            field_list.append(x)

        for x in self._get_radio():
            field_list.append(x)

        for x in self._get_checkbox():
            field_list.append(x)

        for x in self._get_select():
            field_list.append(x)
        
        return field_list
        

    def _get_text(self):
        field_list = []

        for a in allTextInputTypes:
            fields = self.form.findAll('input', attrs={'type':a})

            for field in fields:
                attr = {}
                constraint = {}
                
                if field.has_attr('disabled'):
                    continue

                attr['type'] = field.get('type')
                attr['name'] = field.get('name')
                attr['value'] = field.get('value')

                constraint['size'] = field.get('size')
                constraint['maxlength'] = field.get('maxlength')
                constraint['min'] = field.get('min')
                constraint['max'] = field.get('max')
                # constraint['multipart/form-data'] = field.get('multipart/form-data')
                # constraint['pattern'] = field.get('pattern')

                j = {'attributes':attr, 'constraints':constraint}
                field_list.append(j)

        return field_list

    def _get_textArea(self):
        field_list = []

        textareas = self.form.findAll('textarea')

        for textarea in textareas:
            attr = {}
            constraint = {}

            if textarea.has_attr('disabled'):
                continue

            attr['type'] = 'textarea'
            attr['name'] = textarea.get('name')
            attr['value'] = textarea.getText()

            constraint['maxlength'] = textarea.get('maxlength')

            j = {'attributes':attr, 'constraints':constraint}
            field_list.append(j)
        
        return field_list

    def _get_radio(self):
        radio_list = []

        radio_names_taken = []

        radios = self.form.findAll('input', attrs={'type':'radio'})

        for radio in radios:
            attr = {}
            
            if radio.get('name') in radio_names_taken:
                continue

            radio_names_taken.append(radio.get('name'))

            attr['type'] = 'radio'
            attr['name'] = radio.get('name')
            attr['value'] = radio.get('value')

            j = {'attributes':attr, 'constraints':{}}
            radio_list.append(j)

        return radio_list

    def _get_checkbox(self):
        checkbox_list = []

        checkboxes = self.form.findAll('input', attrs={'type':'checkbox'})

        for checkbox in checkboxes:
            attr = {}
            
            attr['type'] = 'checkbox'
            attr['name'] = checkbox.get('name')
            attr['value'] = checkbox.get('value')

            j = {'attributes':attr, 'constraints':{}}
            checkbox_list.append(j)

        return checkbox_list

    def _get_select(self):
        select_list = []

        selects = self.form.findAll('select')

        for select in selects:
            attr = {}
            
            options = select.findAll('option')

            if options is None:
                continue

            op = options[0]

            attr['type'] = 'select'
            attr['name'] = select.get('name')
            attr['value'] = op.get('value')

            j = {'attributes':attr, 'constraints':{}}
            select_list.append(j)

        return select_list