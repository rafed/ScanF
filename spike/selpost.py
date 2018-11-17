#!usr/bin/python3

import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from seleniumrequests import Chrome

chrome_options = Options()
chrome_options.add_argument("window-size=1366,768")
# chrome_options.add_argument("--start-maximized") # doesnt work for headless, go with window-size
# chrome_options.add_argument("--headless")  


driver = Chrome(executable_path='../chromedriver', chrome_options=chrome_options)

action_link = 'https://www.w3schools.com/action_page.php'
data = {'firstname':'Rafed', 'lastname':'Yasir'}

driver.get('http://www.google.com/')

script = '''
function post(path, params) {
    method = "post"; 

    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
        }
    }

    document.body.appendChild(form);
    form.submit();
}
'''

script_post = 'post("{}", data={});'.format(action_link, json.dumps(data))

script = script + script_post

driver.execute_script(script)
driver.save_screenshot('shot.png')
driver.quit()