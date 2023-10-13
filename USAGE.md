<!-- Start SDK Example Usage -->


```python
import via


s = via.Via()


res = s.via.get_users()

if res.get_users_200_application_json_strings is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->