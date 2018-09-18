# python-appfollow
A Python wrapper for the [AppFollow API](https://appfollow.docs.apiary.io/#)

Installation
------------
```
pip install -e https://github.com/michal-michalak/python-appfollow
```

Requires
--------
    * requests
 
 
Usage
-----

```python
from pyappfollow.client import AppFollowAPI

client = AppFollowAPI(cid='YOUR_CLIENT_ID', api_secret='YOUR_API_SECRET')
 
# app external id (differs for platforms (ios, android etc.))
# for App Store — this is 9-10 digits identification number
# for Google Play — this is bundle name
ext_id = 'SAMPLE_EXT_ID'
 
ratings = client.get_ratings(ext_id=ext_id)
ratings = client.get_ratings(ext_id=ext_id)
versions = client.get_versions(ext_id=ext_id)
```