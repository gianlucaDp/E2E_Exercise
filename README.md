# E2E_Exercise
This repo contains an example of E2E tests in Python with the following frameworks and libraries:
- Pytest
- Selenium
- Allure
<br>
The tests are done on the https://www.douglas.de/de page. Currently there are a simple navigation test, a parametrized test for filters
and a test that always fails to show how fails are handled in the report.

## Installation
All the needed libraries are inside the requirements.txt file, it is advised to use a virtual environment to run the tests.
<br>
If needed please visit the [Allure homepage](https://github.com/allure-framework/allure2) to install the framework on your system.
<br>
Tests can run on multiple browser,
make sure to have those browsers installed on your system if you want to run the tests on them.
## Execution
To run the test launch the command:
```
pytest
```
in the main folder of the repo. By default the tests will be launched in Chrome.
<br>
To launch the tests in a different browser use the command:
```
pytest --browser=<browserName>
```
Currently the supported browser are: 
 `chrome`
 `firefox`
 `safari`

 ## Report
To visualize the report locally execute the command:
```
allure serve allure_results/
```
The report will open in the default current browser.

## Remarks
- To save execution time the browser driver is only created once at the beginning of the tests execution. Thanks to this it's also only necessay to accept cookies once.
- Firefox cookie handling in headless mode is a little trickier, a profile has been added to the repo that will allow cookies to be stored.
- Tests elements are written following the OOP principle, in particular the Page Object model. Thanks to this the tests are easy to read and elements are highly reusable.
- A parametrized test is present that gets the data from the excel file present in the data folder. Since this is a live website some expected values could change in time. Usually it's advised to run tests in a controlled test environment, where the input conditions are stable.
- There is a test that always fails in the repo. In allure report it will show the failure message and a screenshot of the browser will be added in the test_failed_check step.

