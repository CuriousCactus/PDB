#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

url = "http://search.rcsb.org/rcsbsearch/v1/query"
# url = 'http://httpbin.org/post'

id = "6B8A"

json = {
    "query": {
        "type": "group",
        "logical_operator": "and",
        "nodes": [{
            "type": "terminal",
            "service": "structure",
            "parameters": {
                "value": {
                    "entry_id": id,
                    "assembly_id": "1"
                },
                "operator": "strict_shape_match"
            },
            "label": "structure",
            "node_id": 0
        }],
        "label": "query-builder"
    },
    "return_type": "entry",
    "request_options": {
        "pager": {
            "start": 0,
            "rows": 100
        },
        "scoring_strategy": "combined",
        "sort": [{
            "sort_by": "score",
            "direction": "desc"
        }]
    }
}

result = requests.post(url, json=json)
matches = result.json()['result_set']

if result:
    for match in matches:
        print(
            match['identifier']
            + ", score: "
            + str(round(match['score'], 3))
            + ", original_score: "
            + str(round(match['services'][0]['nodes'][0]['original_score'], 1))
        )
        pass
    print("Found number of PDB entries:", len(matches))
else:
    print("Failed to retrieve results")
