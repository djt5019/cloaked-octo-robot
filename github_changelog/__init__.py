# -*- coding: utf-8 -*-
version_info = (1, 0, 0)
__version__ = '.'.join(str(v) for v in version_info[:3])


import requests

username = 'dant'
token = ''
root = ''

tags_uri = '/tags'
commits_uri = '/commit/'
pulls_uri = '/pulls?state=closed'
compare_uri = '/compare/{}...{}'
events_uri = '/issues/events'

events_response = requests.get(root + events_uri, auth=(username, token))
events_response.raise_for_status()
events = [e for e in events_response.json() if e['event'] == 'merged']

tag_response = requests.get(root + tags_uri, auth=(username, token))
tag_response.raise_for_status()
tags = [tag['name'] for tag in tag_response.json()]
tags.reverse()

current_tag = 'HEAD'

for next_tag in tags:
    compare_response = requests.get(root + compare_uri.format(cu))

merged_pulls = []
merge_response = requests.get(root + pulls_uri, auth=(username, token))
merge_response.raise_for_status()



# Grab all tags
# for each tag grab the commits between last tag and current
# for each commit record each merge commit
