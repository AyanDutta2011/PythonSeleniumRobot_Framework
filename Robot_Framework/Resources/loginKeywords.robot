*** Settings ***
Library  SeleniumLibrary
Variables   C:/Users/Ayan Dutta/PycharmProjects/Automation/Robot_Framework/PageObject/locators.py
Library  SeleniumLibrary
Variables  C:/Users/Ayan Dutta/PycharmProjects/Automation/Robot_Framework/PageObject/locators.py

*** Keywords ***
Open my browser
    [Arguments]     ${url}  ${browser}
    open browser    ${url}   ${browser}
    maximize browser window
Close browser
    close all browsers

#for testcase1
Enter username
    [Arguments]  ${un}
    input text  ${user}     ${un}
Enter password
    [Arguments]  ${pwd}
    input text  ${passw}        ${pwd}
Signin
    click button    ${signin}
SuccessLogIN
    title should be     Find a Flight: Mercury Tours:


#for testcase 2
Register
    click link  ${reg}
Fname
    [Arguments]  ${fn}
    input text  ${fname}    ${fn}
Lname
    [Arguments]  ${ln}
    input text  ${lname}    ${ln}
Phone
    [Arguments]  ${pn}
    input text  ${phone}    ${pn}
Email
    [Arguments]  ${em}
    input text  ${email}    ${em}
Address1
    [Arguments]  ${ad1}
    input text  ${addr1}    ${ad1}
Address2
    [Arguments]  ${ad2}
    input text  ${addr2}    ${ad2}
City
    [Arguments]  ${cc}
    input text  ${city_N}    ${cc}
State
    [Arguments]  ${sc}
    input text  ${state}    ${sc}
Pincode
    [Arguments]  ${pc}
    input text  ${pcode}    ${pc}
Contry
    [Arguments]  ${con}
    select from list by label  ${cont}    ${con}
Uname
    [Arguments]  ${unn}
    input text  ${uname}    ${unn}
Password
    [Arguments]  ${upp}
    input text  ${upassw}    ${upp}
Confirm Password
    [Arguments]  ${cp}
    input text  ${cpassw}    ${cp}
Submit button
    click button    ${submit}
