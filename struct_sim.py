#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

url="http://www.rcsb.org/search"
url="http://search.rcsb.org/rcsbsearch/v1/query"
#url = 'http://httpbin.org/post'

json = {
    "query" : {
        "type" : "group",
        "logical_operator" : "and",
        "nodes" : [ {
            "type" : "terminal",
            "service" : "structure",
            "parameters" : {
                "value" : {
                    "entry_id" : "6B8A",
                    "assembly_id" : "1"
                },
                "operator" : "strict_shape_match"
            },
            "label" : "structure",
            "node_id" : 0
        } ],
        "label" : "query-builder"
    },
    "return_type" : "entry",
    "request_options" : {
        "pager" : {
            "start" : 0,
            "rows" : 100
        },
        "scoring_strategy" : "combined",
        "sort" : [ {
            "sort_by" : "score",
            "direction" : "desc"
        } ]
    },
    "request_info" : {
        "src" : "ui",
        "query_id" : "1546b7b8568a1505f259b4d3f3a01034"
    }
}

result = requests.post(url, json=json)

if result:
    print(result.text)
    print("Found number of PDB entries:", result.text.count('\n'))
else:
    print("Failed to retrieve results")
