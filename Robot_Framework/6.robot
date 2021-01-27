*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  http://testautomationpractice.blogspot.com/
${browser}  chrome

*** Test Cases ***
MouseActions_right click
    open browser    ${url}  ${browser}
    maximize browser window

    open context menu       xpath://demo

Mouse_doubleClick
    sleep  2
    double click element    xpath://*[@id="HTML10"]/div[1]/button
    sleep  2

Mouse_Drag_Drop
    drag and drop       xpath://*[@id="gallery"]/li[1]/img      xpath://*[@id="trash"]
    close browser

Scroll
    open browser    ${url}  ${browser}
    maximize browser window
    #execute javascript  window.scrollTo(0,2500)
    execute javascript  window.scrollTo(0,document.body.scrollHeight)
    sleep  2
    execute javascript  window.scrollTo(0,-document.body.scrollHeight)
    sleep  2
    scroll element into view    xpath://*[@id="gallery"]/li[2]/img
    sleep  2
    close browser

*** Keywords ***
