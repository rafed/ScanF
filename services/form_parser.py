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

        # for x in self._get_textArea():
        #     field_list.append(x)

        # for x in self._get_checkbox():
        #     field_list.append(x)
        
        # for x in self._get_radio():
        #     field_list.append(x)
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
        fields = self.form.findAll('input', attrs={'type':'textarea'})

        field_list = []

    def _get_checkbox(self):
        fields = self.form.findAll('input', attrs={'type':'checkbox'})

        field_list = []

    def _get_radio(self):
        fields = self.form.findAll('input', attrs={'type':'radio'})

        field_list = []