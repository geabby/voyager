#Assumption - Backend is python based

###About
- The tests are written using behave framework. Behave using behaviour-driven development and Python to define the tests. [behave](https://behave.readthedocs.io/en/stable/)
- The tests broken into
  features
  - steps
    - *.py
  *.feature

`.feature` contains the test we want to run
With each feature tests are broken into scenarios and scenario outline
Each scenario is made up of multiple steps
The implementation of a step in present in `.py` files

###How to run the tests
- We are using tags to decide which tests to run. Currently all the tests are tagged with @prod. Passing this into the test will allow us to target only those tests with the tag. This will allow us to create tests based on env and flows and run them separately
- The current framework can be expanded to test multiple different use cases reusing most of the steps
- Scenario outline and table allow us to cover many checks using the same test


```
https://docs.github.com/en/rest/activity/events#list-public-events
HTTP response status codes
Status code	Description
200	OK
304	Not modified
403	Forbidden
503	Service unavailable
```


Note: I have not added all the tests we need to automated but focussed on building a framework which can be expanded to add many different use cases

####Steps
Pre Req
- Python and pip are installed
- Token is present
Install behave- `pip install behave`

RUN `API_URL=https://api.github.com python -m behave --tags=prod`

Result
1 feature passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
11 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m1.218s


###Framework
- We have used python based BDD framework to run the tests. Behave is the tool which is used to create the tests
- The feature file is defined in a human readable form and steps can be resused
- Step definitions contain the implementation of the feature steps which is in python



###Reporting
- We can use allure to display reports
- Although i have not implemented it yet, report will display each step and if failure happen what failed



###CI
- These test can be run in Jenkins
- Jenkins has a plugin for allure which will enable us to create good reports


###Debugging
- I have added a settings.json file
- Install Cucumber gherkin plugin in VSCODE
- You should be able to command click into the step from the feature file
- I have also added a launch.json file
- Add the API Token in the file
- Clicking on RUN, you should be able to run tests directly from VSCode
- We should also be able to put breakpoints in the code and test behavior