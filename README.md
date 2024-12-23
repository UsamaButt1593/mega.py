This library is no longer maintained, you should instead use the official CLI client MEGAcmd:

Download it: https://mega.io/cmd#downloadapps

Learn how to use it: https://github.com/meganz/MEGAcmd/blob/master/UserGuide.md


----


Have a Look
===========

There is now an official programmable solution from Mega.nz itself but it has some limitations.

### Not able to directly upload a file by its url
Can be fixed by a vps with disk space

### Encrypts/Decrypts before uploading/downloading files
This can pose a lot of problems e.g. 
- On web, we can only provide mega links (no direct download link) for downloads which copyright holders can exploit to get our data removed from Mega.nz
- On android, it is very challenging to play Mega.nz links in any video player because they need live decryption which in theory can be done by copying how megatools does it but in practical very difficult and time consuming to achieve

## Alternatives
### [Megatools](https://megatools.megous.com/)
We can change this library to disable encryption/decryption. Just remove/comment blocks at [line#3357](https://megous.com/git/megatools/tree/lib/mega.c#n3357) and [line#4274](https://megous.com/git/megatools/tree/lib/mega.c#n4274) in file [lib/mega.c](https://megous.com/git/megatools/tree/lib/mega.c).

We can also implement upload by url using downloading mechanism used by this library.

### [mega_scripts](https://github.com/Amourspirit/mega_scripts)
Provides code to keep mega accounts alive which are by default disabled after 3 months of inactivity.

Also provides code to create unlimited mega accounts without even using legit email accounts using guerrillamail api.

### [mega_scripts](https://github.com/Amourspirit/mega_scripts)
Does some iseful things using bash and megatools

### [mega_scripts](https://greasyfork.org/en/scripts/by-site/mega.nz)
Have not looked at it but it claims to bypass 20GB account storage limit.

### Indishare
Not exactly an alternative but can be used in conjuction with mega as a **_caching layer_**
  


Mega.py
=======

[![Build
Status](https://travis-ci.org/odwyersoftware/mega.py.png?branch=master)](https://travis-ci.org/odwyersoftware/mega.py)
[![Downloads](https://pypip.in/d/mega.py/badge.png)](https://crate.io/packages/mega.py/)  [![PyPI version](https://badge.fury.io/py/mega.py.svg)](https://pypi.org/project/mega.py/)

Python library for the [Mega.co.nz](https://mega.nz/aff=Zo6IxNaHw14)
API, currently supporting:

-   login
-   uploading
-   downloading
-   deleting
-   searching
-   sharing
-   renaming
-   moving files

This is a work in progress, further functionality coming shortly.

For more detailed information see API\_INFO.md

How To Use
----------

### Create a Mega account

First, [create an account with Mega](https://mega.nz/aff=Zo6IxNaHw14) .

### Install mega.py package

Run the following command, or run setup from the latest github source.

```python
pip install mega.py
```

### Import mega.py

```python
from mega import Mega
```

### Create an instance of Mega.py

```python
mega = Mega()
```

### Login to Mega

```python
m = mega.login(email, password)
# login using a temporary anonymous account
m = mega.login()
```

### Get user details

```python
details = m.get_user()
```

### Get account balance (Pro accounts only)

```python
balance = m.get_balance()
```

### Get account disk quota

```python
quota = m.get_quota()
```

### Get account storage space

```python
# specify unit output kilo, mega, gig, else bytes will output
space = m.get_storage_space(kilo=True)
```

### Get account files

```python
files = m.get_files()
```

### Upload a file, and get its public link

```python
file = m.upload('myfile.doc')
m.get_upload_link(file)
# see mega.py for destination and filename options
```
### Upload a file directly via Url, and get its public link

```python
file = m.upload_url('https://examplesite.com/example.zip', 'destination file name.zip')
m.get_upload_link(file)
# you can add custom headers to the request using headers param
# see mega.py for headers, chunk_size, and destination options
```
upload_url(self, url, dest_filename, dest=None, headers=None,chunk_size=10485760 )

### Export a file or folder

```python
public_exported_web_link = m.export('myfile.doc')
public_exported_web_link = m.export('my_mega_folder/my_sub_folder_to_share')
# e.g. https://mega.nz/#F!WlVl1CbZ!M3wmhwZDENMNUJoBsdzFng
```

### Find a file or folder

```python
folder = m.find('my_mega_folder')
# Excludes results which are in the Trash folder (i.e. deleted)
folder = m.find('my_mega_folder', exclude_deleted=True)
```

### Upload a file to a destination folder

```python
folder = m.find('my_mega_folder')
m.upload('myfile.doc', folder[0])
```

### Download a file from URL or file obj, optionally specify destination folder

```python
file = m.find('myfile.doc')
m.download(file)
m.download_url('https://mega.co.nz/#!utYjgSTQ!OM4U3V5v_W4N5edSo0wolg1D5H0fwSrLD3oLnLuS9pc')
m.download(file, '/home/john-smith/Desktop')
# specify optional download filename (download_url() supports this also)
m.download(file, '/home/john-smith/Desktop', 'myfile.zip')
```

### Import a file from URL, optionally specify destination folder

```python
m.import_public_url('https://mega.co.nz/#!utYjgSTQ!OM4U3V5v_W4N5edSo0wolg1D5H0fwSrLD3oLnLuS9pc')
folder_node = m.find('Documents')[1]
m.import_public_url('https://mega.co.nz/#!utYjgSTQ!OM4U3V5v_W4N5edSo0wolg1D5H0fwSrLD3oLnLuS9pc', dest_node=folder_node)
```

### Create a folder

```python
m.create_folder('new_folder')
m.create_folder('new_folder/sub_folder/subsub_folder')
```

Returns a dict of folder node name and node\_id, e.g.

```python
{
  'new_folder': 'qpFhAYwA',
  'sub_folder': '2pdlmY4Z',
  'subsub_folder': 'GgMFCKLZ'
}
```

### Rename a file or a folder

```python
file = m.find('myfile.doc')
m.rename(file, 'my_file.doc')
```

## Contact Support

For paid priority support contact [mega@odwyer.software](mailto:mega@odwyer.software).

**[UK Python Development Agency](https://odwyer.software/)**
