# Via SDK


## Overview

Sample API: Optional multiline or single-line description in [CommonMark](http://commonmark.org/help/) or HTML.

### Available Operations

* [get_users](#get_users) - Returns a list of users.

## get_users

Optional extended description in CommonMark or HTML.

### Example Usage

```python
import via

s = via.Via()


res = s.get_users()

if res.strings is not None:
    # handle response
    pass
```


### Response

**[operations.GetUsersResponse](../../models/operations/getusersresponse.md)**

