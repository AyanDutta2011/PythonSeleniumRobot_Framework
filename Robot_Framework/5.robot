*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  http://demo.automationtesting.in/Windows.html
${browser}  chrome

*** Test Cases ***
TabbedWindow
    open browser    ${url}  ${browser}
    maximize browser window

    click element       xpath://*[@id="Tabbed"]/a/button
    select window       Sakinalium | Home       #it will select window based on the title of next window
    click link      xpath://*[@id="container"]/header/div/div/div[2]/ul/li[4]/a
    close all browsers

Multi_browser
    open browser    https://www.google.co.in/  ${browser}

    sleep  3

    open browser    https://www.bing.com/  ${browser}
    ${title}=   get title
    log to console  ${title}
    switch browser  1           #for switching between multiple open broswer
    sleep  3
    switch browser  2
    ${title}=   get title       #for getting the title
    log to console  ${title}

    close browser
    close all browsers

GoTo_GoBack_GetLoc
    open browser    https://www.google.co.in/  ${browser}
    ${loc}=     get location
    log to console  ${loc}
    sleep  2

    go to   https://www.bing.com/           #for go to the next url in same window
    ${loc}=     get location               #for getting the locations
    log to console  ${loc}
    sleep  2

    go back                                 #for navigate back to the previous url
    ${loc}=     get location
    log to console  ${loc}
    sleep  2

    close browser

*** Keywords ***
