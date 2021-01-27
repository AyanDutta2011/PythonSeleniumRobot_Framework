#Data Driven testing
#username/password :: admin/mercury
*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}      http://newtours.demoaut.com/
${browser}      chrome

*** Keywords ***
open my browser
    open browser    ${url}  ${browser}
    maximize browser window

close browser
    close all browsers

UserName
    [Arguments]  ${un}
    input text  xpath:/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input     ${un}

Password
    [Arguments]     ${pwd}
    input text  xpath:/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/input     ${pwd}

Login
    click element   xpath:/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input

SignInError
    title should be     Sign-on: Mercury Tours

SignInSuccess
    title should be     Find a Flight: Mercury Tours:
