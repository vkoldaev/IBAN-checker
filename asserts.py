#!/usr/bin/env python
# coding: utf-8

# In[7]:


import iban_checker

### Examples
#iban_list = (
#    "GB29NWBK60161331926819", 
#    "ALKK BBBS SSSX CCCC CCCC CCCC CCCC", 
#    "GB123", 
#    "ZZ29NWBK60161331926819", 
#    "GB29NWBK601613319268191"
#)
#for i in iban_list:
#    print(get_iban_info(i))
    
### asserts
assert iban_checker.get_iban_info("GB29NWBK60161331926819") == {
    'Status': 'OK', 
    'Country code': 'GB', 
    'Country': 'United Kingdom', 
    'Bank BIC': 'NWBK', 
    'Bank branch code': '601613'
}, "OK"

assert iban_checker.get_iban_info("ALKK BBBS SSSX CCCC CCCC CCCC CCCC") == {
    'Status': 'OK', 
    'Country code': 'AL', 
    'Country': 'Albania', 
    'Bank BIC': 'BBB', 
    'Bank branch code': 'N/A'
}, "OK w/o branch"

assert iban_checker.get_iban_info("GB123") == {
    'Status': 'Error', 
    'Description': 'Wrong IBAN format'
}, "Wrong format"

assert iban_checker.get_iban_info("ZZ29NWBK60161331926819") == {
    'Status': 'Error', 
    'Description': 'Country nor found'
}, "Wrong country"

assert iban_checker.get_iban_info("GB29NWBK601613319268191") == {
    'Status': 'Error', 
    'Description': 'Whong lenght'
}, "Wrong lenght"

#print ("All tests are OK")

