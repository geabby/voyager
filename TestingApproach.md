Public Repository - https://github.com/geabby/voyager

Define what we need to test and decide where we test them
Testing would be a combination of unit/integration/e2e exploratory and automation testing


##Testing Approach
API being tested
Since this API does not require any tokens or access code, we can directly call this api to test
```
- https://docs.github.com/en/rest/activity/events#list-public-events
HTTP response status codes
Status code	Description
200	OK
304	Not modified
403	Forbidden
503	Service unavailable
```

Test for different ways we can return the above response codes and json response
Check for any case where the above reponse code is not returned

Query Params
Ensure we test for all the query params and we get a result based on the param


Other cases - Test for cases where we get an error
- No params
- Invalid value for the params
- Negative value in params
- Invalid params
- Max size of the response
- No data present in back end
- Perform Post/Put/Delete on a Get call

System Down
- Check Api response when service or any dependant service is down


Performance
- Performance of the api and SLA



Concerns from testing perspective
- Understand better how and when the api is used
- Is there a Staging env we can test
- DO we need to run tests in parallel since in general api testing is fast. Behave might not be the best solution for parallel tests


What tests to automate
- Tests that can serve as regression and that are reliable can be automated
- Checks that are data dependant are not good candidates. Incase we can stub the data then they can considered as candidates for automation






