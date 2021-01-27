*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  http://testautomationpractice.blogspot.com/
${browser}  chrome

*** Test Cases ***
AlertWindow
    open browser    ${url}  ${browser}
    maximize browser window
    click element   xpath://*[@id="HTML9"]/div[1]/button
    sleep  2
    #handle alert    accept     #it will accept the alert
    #handle alert    dismiss     #it will dismiss the alert
    handle alert    leave       #it will not perform any action on alert pop-up
    alert should be present     Press a button!
    alert should not be present     zzzzzzzzzz

Screenshot
    open browser    ${url}  ${browser}
    maximize browser window

    capture element screenshot  xpath://*[@id="gallery"]/li[1]/img    C:/Users/Ayan Dutta/PycharmProjects/Automation/Robot_Framework/files/ele.png
    capture page screenshot     C:/Users/Ayan Dutta/PycharmProjects/Automation/Robot_Framework/files/page.png

    close all browsers

*** Keywords ***



