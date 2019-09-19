# AutomatedWebSelenium

## 1. Installing and setting up python, environment and libraries

### a) Install newest python 3
https://www.python.org/downloads/

### b) Install virtualenv
```pip install virtualenv```

### c) Create virtual environment (with python 3)
at /python-selenium-framework folder (where README.md file is) run:
```
virtualenv venv
```
NOTE: If you face some errors please do:
```
python -m venv <venv_path>
```

### d) Run virtual environment
Mac:
```
source venv/bin/activate
```
Windows:
```
venv/Scripts/activate
```
Now you're using virtual environment -> (venv) should be visible in the console, e.g:
```
(venv) ➜  bin git:() 
```

### e) Install requirements (on your virtual environment) 
```
pip install -r requirements.txt
```
NOTE: If you face some errors please do:
```
python -m pip install -r requirements.txt
```


## 2. Running tests
**IMPORTANT! Make sure you:**
- are in `/python_selenium_framework/python_selenium_framework` directory 
- have virtual environment (venv) activated -> if not, go to 1. d)

**Example run (chrome browser is set by default)**

```
python -m pytest
```
## 3. Others**

### to run tests with other browser:
```
python -m pytest --browser="firefox"
```

### To run tests with short traceback:
```
python -m pytest --tb=native
```

### To run tests multiple times:
```
python -m pytest --count <number>
``` 

### To generate report of tests results:
```
python -m pytest --html=report.html
```


### TIPS:
My favourite selenium selector:
find_element_by_css_selector("div[class='xxx']")


## Suggested naming conventions for Selenium identifiers in python:

| Category | UI/Control type | Prefix | Example |
| ------ | ------ | ------ | ------ |
| Common | {no_type}                  | ---    | _created_goal         |
| Common | Banner                     | bnr    | _notification_bnr     |
| Common | Button                     | btn    | _exit_btn             |
| Common | Check box                  | chb    | _i_agree_chk          |
| Common | Icon                       | icn    | _delete_icn           |
| Common | Image                      | img    | _icon_img             |
| Common | Field                      | fld    | _date_fld             |
| Common | Frame                      | fra    | _language_fra         |
| Common | Message                    | msg    | _error_msg         |
| Common | Navigation button          | nav    | _home_nav             |
| Common | Radio button               | rbn    | _gender_rbn           |
| Common | String                     | str    | _successful_login_str |
| Common | Tab                        | tab    | _user_tab             |
| Common | Text Area                  | txa    | _description_txa      |
| Common | Text box                   | txt    | _last_name_txt        |
| Common | Date picker                | dtp    | _published_dtp        |
| Common | Dropdown List              | ddl    | _country_ddl          |
| Common | Dropdown trigger           | ddt    | _customer_ddt         |
| Common | Dropdown item              | ddi    | _users_ddi            |
| Common | Links/Anchor Tags          | lnk    | _forgot_pwd_lnk       |
| -----------| -----------| -----------| -----------| 
| Complex | Table                      | tbl    | _customer_tbl      |
| Complex | List box                   | lst    | _policy_codes_lst  |
| Complex | ProgressBar                | prg    | _load_file_prg     | 
| Complex | StatusBar                  | sta    | _date_time_sta     |
| Complex | Spinner                    | spn    | _spinner_spn       |
| Complex | Toolbar                    | tlb    | _actions_tlb       |

For more you can inspire from: 
https://stackoverflow.com/questions/45028747/suggested-naming-conventions-for-selenium-identifiers

