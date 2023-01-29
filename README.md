:performing_arts: [Playwright] [APIRequest] builder
===

[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


Documented
---
Read it here [:link: documentation](./doc)  
Read more about the _builder pattern_ on [:link: refactoring.guru](https://refactoring.guru/design-patterns/builder/python/example#lang-features)


Example
---

```python
# sync example
from playwright.sync_api import sync_playwright
from playwright_request.sync_builder import RequestBuilder

with sync_playwright() as p:
    builder = RequestBuilder(p, base_url='https://playwright.dev/')
    request = builder.get("python/docs/intro").create_request()
    response = request()
    print(response.text())
```

```python
# async example
import asyncio
from playwright.async_api import async_playwright
from playwright_request.async_builder import RequestBuilder

async def main():
    async with async_playwright() as p:
        builder = RequestBuilder(p, base_url='https://playwright.dev/')
        request = builder.get("python/docs/intro").create_request()
        response = await request()
        print(await response.text())

asyncio.run(main())
```


Requirements
---
Python3  
Playwright >= 1.26.0


[Playwright]: https://playwright.dev/python/
[APIRequest]: https://playwright.dev/python/docs/api/class-apirequest
[`max_redirects`]: https://playwright.dev/python/docs/api/class-apirequestcontext#api-request-context-delete-option-max-redirects