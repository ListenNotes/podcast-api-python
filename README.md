# Podcast API Python Library

[![Build Status](https://travis-ci.com/ListenNotes/python-api-python.svg?branch=master)](https://travis-ci.com/ListenNotes/python-api-python)

The Podcast API Python library provides convenient access to the [Listen Notes Podcast API](https://www.listennotes.com/api/) from
applications written in the Python language.

Simple and no-nonsense podcast search & directory API. Search the meta data of all podcasts and episodes by people, places, or topics.

<a href="https://www.listennotes.com/api/"><img src="https://raw.githubusercontent.com/ListenNotes/ListenApiDemo/master/web/src/powered_by_listennotes.png" width="300" /></a>

## Documentation

See the [Listen Notes Podcast API docs](https://www.listennotes.com/api/docs/).


## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, please run:

```sh
pip install --upgrade podcast-api
```

Install from source with:

```sh
make && source venv/bin/activate
```

### Requirements

- Python 3.5+

## Usage

The library needs to be configured with your account's API key which is
available in your [Listen API Dashboard](https://www.listennotes.com/api/dashboard/#apps). Set `api_key` to its
value:

```python
from listennotes import podcast_api

api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)

response = client.search(q='star wars')

print(response.json())
```

If `api_key` is None, then we'll connect to a [mock server](https://www.listennotes.com/api/tutorials/#faq0) that returns fake data for testing purposes.

You can see all available API endpoints and parameters on the API Docs page at [listennotes.com/api/docs/](https://www.listennotes.com/api/docs/). 

### Handling exceptions

Unsuccessful requests raise exceptions. The class of the exception will reflect
the sort of error that occurred.

All exception classes can be found in [this file](https://github.com/ListenNotes/podcast-api-python/blob/main/listennotes/errors.py).

And you can see some sample code [here](https://github.com/ListenNotes/podcast-api-python/blob/main/examples/sample.py#L17).