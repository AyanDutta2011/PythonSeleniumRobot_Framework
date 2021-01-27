*** Settings ***
Library  SeleniumLibrary
Resource    C:/Users/Ayan Dutta/PycharmProjects/Automation/Robot_Framework/Resources/loginKeywords.robot
Library  SeleniumLibrary
Resource  C:/Users/Ayan Dutta/PycharmProjects/Automation/Robot_Framework/Resources/loginKeywords.robot
*** Variables ***
${url}      http://newtours.demoaut.com/
${browser}      headLesschrome  #--- for run testcases without opening browser/ headless browser
${un}   admin
${pwd}  mercury

*** Test Cases ***
LogInTest
    Open my browser      ${url}  ${browser}
    Enter username  ${un}
    Enter password  ${pwd}
    Signin
    sleep  3 seconds
    SuccessLogIN
    Close browser

RegisterTest
    Open my browser      ${url}  ${browser}
    Register
    Fname   Ayan
    Lname   Dutta
    Phone   8777345702
    Email  ayand777@gmail.com
    Address1    NSD Road
    Address2    Kadamtala
    City    Howrah
    State   West Bengal
    Pincode  711101
    Contry  BELGIUM
    Uname  AyanDutta
    Password  2011
    Confirm Password  2011
    Submit button
    Close browser
