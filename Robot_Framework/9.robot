*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.microsoft.com/en-in/
${browser}  chrome


*** Test Cases ***
AllLinksCountElement
    open browser    ${url}  ${browser}
    maximize browser window
    ${AllLinksCount}=   get element count   xpath://a
    log to console      ${AllLinksCount}

    @{linktext}     create list
    :FOR    ${i}    IN RANGE    1   ${AllLinksCount}+1
    \   ${linktext}=    get text    xpath:(//a)[${i}]
    \   log to console  ${linktext}
    close browser
