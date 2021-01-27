#Data Driven testing using XLSX file
*** Settings ***
Library  SeleniumLibrary
Resource  C:/Users/Ayan Dutta/PycharmProjects/Automation/Robot_Framework/11.robot
Library  DataDriver     C:/Users/Ayan Dutta/PycharmProjects/Automation/Robot_Framework/files/test.xlsx     sheet_name=Sheet1

Test Setup  open my browser
Test Teardown  close browser
Test Template  InvalidLogin      #import user define keyword

*** Variables ***
${url}      http://newtours.demoaut.com/
${browser}      chrome

*** Test Cases ***
LoginWithExcel  using   ${un}   and   ${pwd}

*** Keywords ***
InvalidLogin
    [Arguments]  ${un}  ${pwd}
    UserName    ${un}
    Password    ${pwd}
    Login
    SignInError
