*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  http://demoForFramesConcept.com/
${browser}  chrome

*** Test Cases ***
Switch_frame
    open browser    ${url}  ${browser}
    maximize browser window

    select frame    frame1      #we are selecting the 1st frame
    click link      link_of_1   #we are clicking on the link present in 1st frame
    unselect frame      #we are unselecting the frame or navigate back to default one

    sleep  2
    select frame     frame2      #again we are selecting the 2nd frame
    click link       link_of_2       #we are clicking on the link present in 2nd frame

*** Keywords ***
