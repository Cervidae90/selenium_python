# AutomatedWebSelenium
Contents:
1. Installing and setting up python, environment and libraries
2. Running tests
3. Other

## 1. Installing and setting up python, environment and libraries

### a) Install latest Python 3.x.x (e.g. 3.8.0)
https://www.python.org/downloads/

Then to make sure it's installed properly please type in console:
```
python --version
```
The output should be ```Python {installed_version}```, e.g:
```
Python 3.8.0
```

### b) Install virtualenv (virtual environment)
In your console type:
```
pip install virtualenv
```
####Note: if you are somehow using Python 2.x.x and you want to use 3.x.x instead but you don't know how to override newer version, please do the following:  ```virtualenv -p python3 venv```. This will install python 3.x.x in your virtual environment.

Then to make sure it's installed properly type in console:
```
virtualenv --version
```
The output should be ```{installed_version}```:
 e.g:
```
16.0.0
```
### c) Create virtual environment (with python 3)
In ```/python-selenium-framework``` directory (where README.md file is) run:
```
virtualenv venv
```
####Note: If you face some errors please do:
```
python -m venv <venv_path>
```

### d) Run virtual environment
It is essentially that you are using virtual environment while proceeding next steps. Please always pay attention to that.

To activate virtual env, type:

On Mac:
```
source venv/bin/activate
```
On Windows:
```
venv/Scripts/activate
```
Now you're using virtual environment. ```(venv)``` should be visible in the console, e.g:
```
(venv) ➜  bin git:() 
```

### e) Install requirements (dependencies/libraries)
If you are already using virtual environment, type:
```
pip install -r requirements.txt
```
Then to make sure it's installed properly type:
```
pip freeze
```
The output should look similar to this (some libraries may be different):
```
atomicwrites==1.3.0
attrs==19.1.0
certifi==2019.6.16
chardet==3.0.4
colorama==0.4.1
configparser==3.8.1
crayons==0.2.0
idna==2.8
importlib-metadata==0.19
more-itertools==7.2.0
packaging==19.1
pluggy==0.12.0
py==1.8.0
pyparsing==2.4.2
pytest==5.0.1
pytest-html==1.22.0
pytest-metadata==1.8.0
requests==2.22.0
selenium==3.141.0
six==1.12.0
urllib3==1.25.3
wcwidth==0.1.7
webdriver-manager==1.8.2
zipp==0.5.2
```
####NOTE: If you face some errors please do:
```
python -m pip install -r requirements.txt
```


## 2. Running tests
####Make sure you:
- are in `/python_selenium_framework/python_selenium_framework` directory 
- have virtual environment (venv) activated -> if not, go to 1. d)

**Example run (chrome browser is set by default)**

```
python -m pytest
```


## 3. Other

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

