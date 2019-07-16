#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re
import dictionaries
import asserts

### Functions
def check_iban_regexp(iban: str) -> bool:
    if not re.fullmatch(r"[A-Z]{1,2}[0-9A-Z]{20,32}", iban) is None:
        return True
    else:
        return False
    
def get_country(iban: str) -> bool:
    global country_code
    global country
    country_code = iban[0:2]
    try:
        country = iban_dictionaries.COUNTRIES_ALPHA2[country_code]
        return True
    except:
        return False

def check_lenght(iban: str) -> bool:
    if len(iban) == iban_dictionaries.IBAN_LENGHT[country_code]:
        return True
    return False

def get_bic(iban: str) -> bool:
    global bank_bic
    bank_bic = ""
    try:
        bic_range = iban_dictionaries.BIC_RANGE_VARIABLES[country_code]
        bank_bic = iban[bic_range[0]:bic_range[1]]
        return True
    except:
        return False

def get_branch(iban: str) -> bool:
    global bank_branch
    bank_branch = ""
    try:
        branch_range = iban_dictionaries.BRANCH_RANGE_VARIABLES[country_code]
        bank_branch = iban[branch_range[0]:branch_range[1]]
    except:
        bank_branch = "N/A"
    return True


def get_iban_info(iban: str) -> dict:
    iban = iban.replace(" ","")
    if not check_iban_regexp(iban):
        return {
            "Status":"Error",
            "Description":"Wrong IBAN format",
        }
    if not get_country(iban):
        return {
            "Status":"Error", 
            "Description":"Country nor found",
        }
    if not check_lenght(iban):
        return {
            "Status":"Error", 
            "Description":"Whong lenght",
        }        
    if not get_bic(iban):
        return {
            "Status":"Error", 
            "Description":"BIC definition error",
        }   
    get_branch(iban)
    return {
        "Status": "OK", 
        "Country code": country_code, 
        "Country": country,
        "Bank BIC": bank_bic,
        "Bank branch code": bank_branch,
    }

