*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  http://testautomationpractice.blogspot.com/
${browser}  chrome

*** Test Cases ***
HTML_Table
    open browser    ${url}  ${browser}
    maximize browser window
    ${rows}=    get element count   xpath://table[@name='BookTable']/tbody/tr
    ${cols}=    get element count   xpath://table[@name='BookTable']/tbody/tr[1]/th

    log to console  ${rows}
    log to console  ${cols}

    ${data}=    get text    xpath://table[@name='BookTable']/tbody/tr[4]/td[1]
    log to console  ${data}
    sleep  10

    table column should contain     xpath://table[@name='BookTable']    2   Author
    table row should contain    xpath://table[@name='BookTable']    4   Learn JS
    table cell should contain   xpath://table[@name='BookTable']    5   2   Mukesh
    table header should contain     xpath://table[@name='BookTable']    BookName

    close browser
