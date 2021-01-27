*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}     http://demo.automationtesting.in/Register.html
${browser}  chrome

*** Test Cases ***
Register
    Launch_Browser
    sleep  5
    Choose File     //*[@id="imagesrc"]     C:/Users/Ayan Dutta/Pictures/Saved Pictures/screen-3.jpg


    #close browser



*** Keywords ***
Launch_Browser
    open browser    ${url}  ${browser}
    maximize browser window





