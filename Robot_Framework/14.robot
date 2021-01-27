*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
TC1
    [Tags]  sanity
    log to console  Ayan
TC2
    [Tags]  ff
    log to console  Aparna
TC3
    [Tags]  ff
    log to console  Chandra
TC4
    [Tags]  sanity
    log to console  Dutta
TC5
    [Tags]  sanity
    log to console  Howrah


#How to run?

#robot --include=sanity 14.robot    ---to execute particular type of test cases
#robot -i sanity -i ff 14.robot     ---to execute multiple test cases
#robot -e sanity 14.robot           ---to exclude a type of test cases /will execute without sanity type
#robot -i sanity -e ff 14.robot     ---incule and exlude a type of test cases