#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

url = 'http://www.rcsb.org/pdb/rest/search'

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

    print("Found number of PDB entries:", result.text.count('\n'))
    print(result.text)

else:

    print("Failed to retrieve results")
