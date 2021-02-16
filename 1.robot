*** Settings ***
Library     SeleniumLibrary

Resource  C:/Users/11.robot
Library  DataDriver     C:/Users/test.xlsx     sheet_name=Sheet1

Suite Setup     Start
Suite Teardown  End
Test Setup      LaunchBrowser
Test Teardown   CloseBrowser

*** Variables ***
${url}      https://www.amazon.in/
${browser}      chrome

*** Test Cases ***
Time/Speed
    [Tags]  Sanity
    sleep 5
    set selenium speed  5
    set selenium timeout    5
    set selenium implicit wait  5
    wait untill page contains   ${demo}

Title
    [Tags]  FF
    title should be     AyanDutta
    get text    ${demo}
    get value   ${demo}
    get location
    location should be      ${url}
    log location
    log title

ElementClick
    [Tags]  Sanity
    ${demo}  set variable    xpath://*[@id="directsec"]/img
    click element    ${demo}
    click link      ${demo}
    page should not contain element     ${demo}
    clear element text      ${textbox}
    click image     ${picture}

Alert
    [Tags]  FF
    handle alert    accept
    handle alert    dismiss
    handle alert    leave

    alert should be present     Demo_Alert
    alert should not be present     Demo_Demo

    input text into alert   ayand777@gmail.com
    input text into prompt  ayandutta

RadioButton
    [Tags]  Sanity
    select radio button     sex     Male
    radio button should be set to   sex     Male
    radio button should not be set to   sex     Female
    radio button should not be selected     sex
    page should contain radio button    sex
    page should not contain radio button    sex

CheckBox
    [Tags]  FF
    select checkbox     TOC
    unselect checkbox   TOC
    checkbox should be selected     TOC
    checkbox should not be selected     TOC
    page should contain checkbox    TOC
    page should not contain checkbox    TOC

Frame
    [Tags]  FF
    select frame    frame1
    unselect frame      frame1

Dropdown
    [Tags]  Sanity
    select from list by lebel   country     India
    select from list by index   country     5
    select from list by value   country     India
    unselect from list by index     country     1
    select all from list    country
    unselect all from list    country

Window
    [Tags]  FF
    select window       PageTitle
    switch browser  1
    close window
    mouse over  ${ele}

Navigation
    [Tags]  Sanity
    go to   www.google.com
    go back
    get location
    reload page

FileUpload
    [Tags]  FF
    choose file     ${demo}     C:/Users/HP/Desktop/Imp/ele.png

Scroll
    [Tags]  Sanity
    execute javascript  window.scrollTo(0,document.body.scrollHeight)
    execute javascript  window.scrollTo(0,-document.body.scrollHeight)
    scroll element into view    xpath://*[@id="gallery"]/li[2]/img

Mouse
    [Tags]  FF
    open context menu   ${demo}
    double click element    ${demo}
    drag and drop   ${demo1}    ${demo2}
    mouse hover ${demo}

Verify
    [Tags]  Sanity
    element should be enable   ${demo}
    element should not be enable    ${demo}

    element should be visible   ${demo}
    element should not be visible  ${demo}

Screenshot
    [Tags]  FF
    capture element screenshot      ${demo}     C:/Users/HP/Desktop/Imp/ele.png
    capture page screenshot     C:/Users/HP/Desktop/Imp/ele.png

Table
    [Tags]  Sanity
    ${row} =   get element count       xpath://table[@name='BookTable']/tbody/tr
    ${cols}=    get element count   xpath://table[@name='BookTable']/tbody/tr[1]/th

    ${data}=    get text    xpath://table[@name='BookTable']/tbody/tr[2]/td[5]

    table row should contain    xpath://table[@name='BookTable']/   2   Name
    table column should contain     xpath://table[@name='BookTable']/   2   Ayan
    table cell should contain       xpath://table[@name='BookTable']/   2   5   201196
    table header should contain     xpath://table[@name='BookTable']/   Employee

LinksCount
    [Tags]  FF
    ${ALLLinks}=    get element count   xpath://a
    @{linksList}    create list
        :FOR    ${i}    IN RANGE    1    ${ALLLinks} + 1
        \   ${linksList}=   get text    xpath:(//a)[${i}]
        \   log to console  ${linkslist}

*** Keywords ***

Start
    log to console      Started

End
    log to console      Completed

LaunchBrowser
    open browser    ${url}  ${browser}
    miniimize browser window
    sleep   1
    maximize browser window

CloseBrowser
    log to console  Completed
    close all browsers

#How to run?
#robot --include=sanity 14.robot    ---to execute particular type of test cases
#robot -i sanity -i ff 14.robot     ---to execute multiple test cases
#robot -e sanity 14.robot           ---to exclude a type of test cases /will execute without sanity type
#robot -i sanity -e ff 14.robot     ---incule and exlude a type of test cases

#How to run Test Suits
#robot folder_name\     Multiple test cases will be executed one after another
#robot folder_name\San*.robot    those testcase name starting eith San, will be executed one after another

#How to execute multiple test cases Parallelly
#pip install robotframework-pabot
#pabot --processes 2 folder_name\*.robot
#pabot --processes 2 --outputdir Results folder_name\*.robot    #to store o/p with in a different folder (folder should be created automatically)
