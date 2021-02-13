*** Settings ***
Library     SeleniumLibrary

Test Setup      LaunchBrowser
Test Teardown   CloseBrowser

*** Variables ***
${url}      https://www.amazon.in/
${browser}      chrome

*** Test Cases ***
LinksCount
    ${ALLLinks}=    get element count   xpath://a
    @{linksList}    create list
        :FOR    ${i}    IN RANGE    1    ${ALLLinks} + 1
        \   ${linksList}=   get text    xpath:(//a)[${i}]
        \   log to console  ${linkslist}

*** Keywords ***

LaunchBrowser
    open browser    ${url}  ${browser}
    maximize browser window
    sleep   5

CloseBrowser
    close all browsers