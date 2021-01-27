*** Settings ***
Library     SeleniumLibrary

#Suite Setup  Mahapatra1
#Suite Teardown  Mahapatra2

#Test Setup     Ishita1
#Test Teardown   Ishita2

*** Variables ***

*** Test Cases ***
TC1
    [Tags]  Sanity
    log to console  Ayan1

TC2
    [tags]  Reg
    log to console  Ayan2

TC3
    [Tags]  Reg
    log to console  Ayan3

TC4
    [Tags]  Sanity
    log to console  Ayan4

TC5
    [Tags]  Reg
    log to console  Ayan5

Ishita1
    log to console  zzz

Ishita2
    log to console  yyy

Mahapatra1
    log to console  aaa

Mahapatra2
    log to console  zzz


*** Keywords ***

