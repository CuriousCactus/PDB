#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Gets IDs of structures in the PDB according to an XML query using Python 3
# Uses the requests module instead of urllib2, as requests is more modern

# Note the artificial splitting of the xml query into a key:value pair
# This is needed because if xml is passed to requests.post as one string it is interpreted as data, whereas if it is passed as a key:value pair it is interpreted as the input to a form
# If the query is passed as data the request doesn't work and the html of the whole search page is returned

# If urllib2 is given an xml query which is not in key:value format it forces it into that format and treats it as the input to a form, which works fine
# Requests does not do this forcing, hence it must be done manually

import requests

url = 'http://www.rcsb.org/pdb/rest/search'
#url = 'http://httpbin.org/post'

queryText = """
'1.0' encoding='utf-8'?>
<orgPdbQuery>
    <version>B0907</version>
    <queryType>org.pdb.query.simple.ExpTypeQuery</queryType>
    <description>Experimental Method Search: Experimental Method=SOLID-STATE NMR</description>
    <mvStructure.expMethod.value>SOLID-STATE NMR</mvStructure.expMethod.value>
</orgPdbQuery>
"""

xml = {"<?xml version": queryText}

result = requests.post(url, data = xml)

if result:
    print(result.text)
    print("Found number of PDB entries:", result.text.count('\n'))
else:
    print("Failed to retrieve results")
