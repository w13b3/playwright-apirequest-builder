Documentation: playwright_request.async_builder
---

# Usage

```python
import asyncio
from playwright.async_api import APIResponse
from playwright_request.async_builder import RequestBuilder


async def main() -> None:
    builder = RequestBuilder()
    request = builder.get("https://www.python.org/").create_request()
    response: APIResponse = await request()
    print(response.text())

    
asyncio.run(main())
```

or

```python
import asyncio
from playwright_request.async_builder import RequestBuilder


async def main() -> None:
    builder = RequestBuilder()
    response = await builder.get("https://www.python.org/").do()
    print(response.text())

    
asyncio.run(main())
```


## `RequestBuilder`  
Initializes the builder  
Parameters:  
- `playwright` -  default: `None`  

Keyword only parameters:  
- `base_url` -  default: `None`  
- `extra_http_headers` -  default: `None`  
- `http_credentials` -  default: `None`  
- `ignore_https_errors` -  default: `None`  
- `proxy` -  default: `None`  
- `user_agent` -  default: `None`  
- `timeout` -  default: `None`  
- `storage_state` -  default: `None`  

Returns:
- `RequestBuilder`

---


### `url`  
Method of [`RequestBuilder`]
Parameters: 
- `_str: str` 

Returns:
- [`RequestBuilder`]

---


### `params`  
Method of [`RequestBuilder`]
Parameters: 
- `_dict: typing.Dict[str, typing.Union[str, float, bool]]` 

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---


### `method`  
Method of [`RequestBuilder`]
Parameters: 
- `_str: str` 

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---

### `headers`  
Method of [`RequestBuilder`]
Parameters:   
- `_dict: typing.Dict[str, str]`  

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---


### `data`  
Method of [`RequestBuilder`]
Parameters:   
- `_any: typing.Union[typing.Any, str, bytes]`  

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---


### `form`  
Method of [`RequestBuilder`]
Parameters:   
- `_dict: typing.Dict[str, typing.Union[str, float, bool]]`  

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---


### `multipart`  
Method of [`RequestBuilder`]
Parameters:   
- `_dict: typing.Dict[str, typing.Union[bytes, bool, float, str, FilePayload]]`  

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---


### `timeout`  
Method of [`RequestBuilder`]
Parameters:   
- `_milliseconds: float`  

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---


### `fail_on_status_code`  
Method of [`RequestBuilder`]
Parameters:   
- `_bool: bool` - default: `True`  

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---


### `ignore_https_errors`  
Method of [`RequestBuilder`]
Parameters:   
- `_bool: bool` - default: `True`  

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---


### `max_redirects`  
Method of [`RequestBuilder`]
Parameters:   
- `_int: int`  

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---


### `request_context`  
Method of [`RequestBuilder`]
Parameters:   
- `` 

Returns:
- [`RequestBuilder`]

_Parameter of playwright [APIrequest new_context]_  

---


## Methods  

### `delete`  
Method of [`RequestBuilder`]
Set [`method`] to DELETE and [`url`] to given string.  
Parameters:   
- `_url: str`  

Returns:
- [`RequestBuilder`]

---


### `get`  
Method of [`RequestBuilder`]
Set [`method`] to GET and [`url`] to given string.  
Parameters:   
- `_url: str`  

Returns:
- [`RequestBuilder`]

---


### `head`  
Method of [`RequestBuilder`]
Set [`method`] to HEAD and [`url`] to given string.  
Parameters:   
- `_url: str`  

Returns:
- [`RequestBuilder`]

---


### `patch`  
Method of [`RequestBuilder`]
Set [`method`] to PATCH and [`url`] to given string.  
Parameters:   
- `_url: str`  

Returns:
- [`RequestBuilder`]

---


### `put`  
Method of [`RequestBuilder`]
Set [`method`] to PUT and [`url`] to given string.  
Parameters:   
- `_url: str`  

Returns:
- [`RequestBuilder`]

---


### `post`  
Method of [`RequestBuilder`]
Set [`method`] to POST and [`url`] to given string.  
Parameters:   
- `_url: str`  

Returns:
- [`RequestBuilder`]

---


### `reset`  
Method of [`RequestBuilder`]
Sets all the values to the default value.

Returns:
- [`RequestBuilder`]

---


### `create_request`  
Returns a callable
Method of [`RequestBuilder`]

Returns:
- `typing.Callable[[typing.Optional[APIRequestContext]], typing.Coroutine[typing.Any, typing.Any, APIResponse]`

---


#### Callable from `create_request`  
Makes the request as it is built  
Parameters: 
- `context: typing.Optional[APIRequestContext]` - default: `None`  

Returns:
- [`playwright.sync_api.APIResponse`] 

---


### `do`  
Method of [`RequestBuilder`]
Makes the request as it is built  
Parameters:   
- `context: typing.Optional[APIRequestContext]` - default: `None`  

Returns:
- [`playwright.sync_api.APIResponse`] 

---

<!-- archive.today/dSsue -->
[APIrequest new_context]: http://playwright.dev/python/docs/api/class-apirequest#APIrequest  
<!-- archive.today/osYj2 -->
[`playwright.sync_api.APIResponse`]: http://playwright.dev/python/docs/api/class-apiresponse  

[`RequestBuilder`]: #RequestBuilder
[`method`]: #method
[`url`]: #url
