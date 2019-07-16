#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# All data has been taken frof Wiki: https://en.wikipedia.org/wiki/International_Bank_Account_Number
# Actual date: 2019.07.15

COUNTRIES_ALPHA2 = {
    "AL": "Albania",
    "AD": "Andorra",
    "AT": "Austria",
    "AZ": "Azerbaijan",
    "BH": "Bahrain",
    "BY": "Belarus",
    "BE": "Belgium",
    "BA": "Bosnia and Herzegovina",
    "BR": "Brazil",
    "BG": "Bulgaria",
    "CR": "Costa Rica",
    "HR": "Croatia",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DK": "Denmark",
    "DO": "Dominican Republic",
    "TL": "East Timor",
    "EE": "Estonia",
    "FO": "Faroe Islands",
    "FI": "Finland",
    "FR": "France",
    "GE": "Georgia",
    "DE": "Germany",
    "GI": "Gibraltar",
    "GR": "Greece",
    "GL": "Greenland",
    "GT": "Guatemala ",
    "HU": "Hungary",
    "IS": "Iceland",
    "IE": "Ireland",
    "IL": "Israel",
    "IT": "Italy",
    "JO": "Jordan",
    "KZ": "Kazakhstan",
    "XK": "Kosovo",
    "KW": "Kuwait",
    "LV": "Latvia",
    "LB": "Lebanon",
    "LI": "Liechtenstein",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "MK": "North Macedonia",
    "MT": "Malta",
    "MR": "Mauritania",
    "MU": "Mauritius",
    "MC": "Monaco",
    "MD": "Moldova",
    "ME": "Montenegro",
    "NL": "Netherlands",
    "NO": "Norway",
    "PK": "Pakistan",
    "PS": "Palestinian territories",
    "PL": "Poland",
    "PT": "Portugal",
    "QA": "Qatar",
    "RO": "Romania",
    "SM": "San Marino",
    "SA": "Saudi Arabia",
    "RS": "Serbia",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "ES": "Spain",
    "SE": "Sweden",
    "CH": "Switzerland",
    "TN": "Tunisia",
    "TR": "Turkey",
    "AE": "United Arab Emirates",
    "GB": "United Kingdom",
    "VA": "Vatican City",
    "VG": "Virgin Islands, British",
}

IBAN_LENGHT = {
    "AL": 28,
    "AD": 24,
    "AT": 20,
    "AZ": 28,
    "BH": 22,
    "BY": 28,
    "BE": 16,
    "BA": 20,
    "BR": 29,
    "BG": 22,
    "CR": 22,
    "HR": 21,
    "CY": 28,
    "CZ": 24,
    "DK": 18,
    "DO": 28,
    "TL": 23,
    "EE": 20,
    "FO": 18,
    "FI": 18,
    "FR": 27,
    "GE": 22,
    "DE": 22,
    "GI": 23,
    "GR": 27,
    "GL": 18,
    "GT": 28,
    "HU": 28,
    "IS": 26,
    "IE": 22,
    "IL": 23,
    "IT": 27,
    "JO": 30,
    "KZ": 20,
    "XK": 20,
    "KW": 30,
    "LV": 21,
    "LB": 28,
    "LI": 21,
    "LT": 20,
    "LU": 20,
    "MK": 19,
    "MT": 31,
    "MR": 27,
    "MU": 30,
    "MC": 27,
    "MD": 24,
    "ME": 22,
    "NL": 18,
    "NO": 15,
    "PK": 24,
    "PS": 29,
    "PL": 28,
    "PT": 25,
    "QA": 29,
    "RO": 24,
    "SM": 27,
    "SA": 24,
    "RS": 22,
    "SK": 24,
    "SI": 19,
    "ES": 24,
    "SE": 24,
    "CH": 21,
    "TN": 24,
    "TR": 26,
    "AE": 23,
    "GB": 22,
    "VA": 22,
    "VG": 24,
}

BIC_RANGE_VARIABLES = {
    "AL": (4,7),
    "AD": (4,8),
    "AT": (4,9),
    "AZ": (4,8),
    "BH": (4,8),
    "BY": (4,8),
    "BE": (4,7),
    "BA": (4,7),
    "BR": (4,12),
    "BG": (4,8),
    "CR": (5,8),
    "HR": (4,11),
    "CY": (4,7),
    "CZ": (4,8),
    "DK": (4,8),
    "DO": (4,8),
    "TL": (4,7),
    "EE": (4,6),
    "FO": (4,8),
    "FI": (4,10),
    "FR": (4,9),
    "GE": (4,6),
    "DE": (4,12),
    "GI": (4,8),
    "GR": (4,7),
    "GL": (4,8),
    "GT": (4,8),
    "HU": (4,7),
    "IS": (4,8),
    "IE": (4,8),
    "IL": (4,7),
    "IT": (5,10),
    "JO": (4,8),
    "KZ": (4,7),
    "XK": (4,8),
    "KW": (4,8),
    "LV": (4,8),
    "LB": (4,8),
    "LI": (4,9),
    "LT": (4,9),
    "LU": (4,7),
    "MK": (4,7),
    "MT": (4,8),
    "MR": (4,9),
    "MU": (4,10),
    "MC": (4,9),
    "MD": (4,6),
    "ME": (4,7),
    "NL": (4,8),
    "NO": (4,8),
    "PK": (4,8),
    "PS": (4,8),
    "PL": (4,7),
    "PT": (4,8),
    "QA": (4,8),
    "RO": (4,8),
    "SM": (4,10),
    "SA": (4,6),
    "RS": (4,7),
    "SK": (4,8),
    "SI": (4,6),
    "ES": (4,8),
    "SE": (4,7),
    "CH": (4,9),
    "TN": (4,6),
    "TR": (4,9),
    "AE": (4,7),
    "GB": (4,8),
    "VA": (4,7),
    "VG": (4,8),
}

BRANCH_RANGE_VARIABLES = {
    "BA": (7,10),
    "BR": (12,17),
    "BG": (8,12),
    "CY": (7,12),
    "EE": (6,8),
    "FR": (9,14),
    "HU": (7,11),
    "IE": (8,14),
    "IL": (7,10),
    "IT": (10,15),
    "JO": (8,12),
    "MT": (8,13),
    "MR": (9,14),
    "MU": (10,12),
    "MC": (9,12),
    "PL": (7,11),
    "PT": (8,12),
    "SM": (10,15),
    "SI": (6,9),
    "ES": (8,12),
    "TN": (6,9),
    "GB": (8,14),
}
