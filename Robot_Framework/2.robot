*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  http://www.practiceselenium.com/practice-form.html
${browser}  chrome

*** Test Cases ***
RadioButton_CheckBox
    open browser    ${url}  ${browser}
    maximize browser window

    set selenium timeout    10 seconds      #it will wait max 10 sec for the variable to be appear on webpage
    wait until page contains    Practice Form   #it will wait for max 5 sec

# verify element is visible or not
    ${radio}  set variable  xpath://*[@id="sex-1"]
    element should be visible  ${radio}

#selecting radio button
    select radio button     sex     Female
    select radio button     exp     exp-3

#selecting/unselecting check box
    set selenium speed      2 seconds    #works like implicitly wait, it will wait for 2 sec for every steps
    select checkbox     BlackTea
    select checkbox     RedTea

    unselect checkbox       RedTea
Dropdown
#select from dropdown
    select from list by label   continents  Australia
    select from list by index   continents  5
List
#select/unselect values from lists
    select from list by label   selenium_commands   Navigation Commands
    set selenium implicit wait  10 seconds      #it will wait for max 10 sec
    #if we dont give implicit wait and the variable is not present in webpage,
    #so it will give error immidiatly like : Such element is not found
    #by default it will wait for 0 sec
    #this statement will applicable for every statement in script
    select from list by label   selenium_commands   WebElement Commands
    sleep  1
    unselect from list by label   selenium_commands   Navigation Commands

    CloseApp        #calling the keywords

*** Keywords ***
#user defined keyword without [arguments]
CloseApp            #Creating own keywords in python
    close browser           #it will close the current browser
    #close all browsers     #it will close all the open browser