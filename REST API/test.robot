*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://appaccess.mphasis.com/
${browser}  chrome
#How to define variable:
${HCM}  set variable    xpath://*[@id="directsec"]/img

built in keywords:
------------------

*** Test Cases ***
open browser    ${url}  ${browser}
maximize browser window
minimize browser window
input text  xpath://*[@id="textfield"]    2359915
click element   xpath://*[@id="submit"]

title should be     AppAccess
element should be enabled   ${HCM}
element should be visible  ${HCM}
sleep  5
element should not be enabled   ${HCM}
element should not be visible  ${HCM}
click element   xpath:/html/body/section[1]/div/div/div[5]/font/a/strong/img
close browser
close all browser
select radio button     sex     Female			#select radio button
select checkbox     RedTea				#select checkbox
unselect checkbox       RedTea
select from list by label   continents  Australia	#select from dropdown
select from list by index   continents  5		#select from dropdown
select from list by label   selenium_commands   Navigation Commands	#select values from lists
unselect from list by label   selenium_commands   Navigation Commands	#unselect values from lists

set selenium speed	2 seconds		#every steps will be executed after 2 sec
set selenium timeout    10 seconds          	#it will wait max 10 sec for the variable to be appear on webpage
wait until page contains    Practice Form   	#it will wait for max 5 sec
set selenium implicit wait  10 seconds
	#it will wait for max 10 sec
	#if we dont give implicit wait and the variable is not present in webpage,
	#so it will give error immidiatly like : Such element is not found
	#by default it will wait for 0 sec

handle alert    accept     	     #it will accept the alert
handle alert    dismiss     	 #it will dismiss the alert
handle alert    leave      	     #it will not perform any action on alert pop-up

alert should be present     Press a button!
alert should not be present     zzzzzzzzzz
capture element screenshot  xpath://*[@id="gallery"]/li[1]/img    C:/Robot_Framework/files/ele.png
capture page screenshot     C:/Robot_Framework/files/page.png

select frame    frame1     	 #we are selecting the 1st frame
click link      link_of_1   	 #we are clicking on the link present in 1st frame
unselect frame     		 #we are unselecting the frame or navigate back to default one
sleep  2
select frame     frame2     	 #again we are selecting the 2nd frame
click link       link_of_2       #we are clicking on the link present in 2nd frame

select window       Sakinalium | Home       #it will select window based on the title of next window

#Multi browser
open browser    https://www.bing.com/  ${browser}
${title}=   get title
log to console  ${title}
switch browser  1           #for switching between multiple open broswer
sleep  3
switch browser  2
${title}=   get title       #for getting the title
log to console  ${title}

#GoTo_GoBack_GetLoc
open browser    https://www.google.co.in/  ${browser}
${loc}=     get location
log to console  ${loc}
sleep  2
go to   https://www.bing.com/           #for go to the next url in same window
${loc}=     get location                #for getting the locations
log to console  ${loc}
sleep  2
go back                                 #for navigate back to the previous url
${loc}=     get location
log to console  ${loc}

#upload file
Choose File     xpath://*[@id="HTML10"]/div[1]/    E://Project/Publish/SampleTest.1500/rose.jpg

open context menu       xpath://demo	#Mouse_Right click
double click element    xpath://*[@id="HTML10"]/div[1]/button	#Mouse_Double click
drag and drop       xpath://*[@id="gallery"]/li[1]/img      xpath://*[@id="trash"] 	#Drag and Drop

#Scroll
execute javascript  window.scrollTo(0,document.body.scrollHeight)
execute javascript  window.scrollTo(0,-document.body.scrollHeight)
scroll element into view    xpath://*[@id="gallery"]/li[2]/img

${AllLinksCount}=   get element count   xpath://a
log to console      ${AllLinksCount}
@{linktext}     create list
    :FOR    ${i}    IN RANGE    1   ${AllLinksCount}+1
    \   ${linktext}=    get text    xpath:(//a)[${i}]
    \   log to console  ${linktext}

Suite Setup     log to console  open_browser        #execute once before Test case execution starts
Suite Teardown      log to console   close_browser  #execute once after Test case execution ends

Test Setup  log to console  sign_in     #execute before each and every test case
Test Teardown  log to console   sign_out    #execute after each and every test case

#HTML table
${rows}=    get element count   xpath://table[@name='BookTable']/tbody/tr
${cols}=    get element count   xpath://table[@name='BookTable']/tbody/tr[1]/th

${data}=    get text    xpath://table[@name='BookTable']/tbody/tr[4]/td[1]
log to console  ${data}

table column should contain     xpath://table[@name='BookTable']    2   Author
table row should contain    xpath://table[@name='BookTable']    4   Learn JS
table cell should contain   xpath://table[@name='BookTable']    5   2   Mukesh
table header should contain     xpath://table[@name='BookTable']    BookName

*** Keywords ***
#For loop
ForLoop1
    : FOR   ${i}    IN RANGE    1   10
    \   log to console  ${i}

ForLoop2
    : FOR   ${i}    IN    1 2 3 4 5     #for single space b/w values will give o/p in same line
    \   log to console  ${i}

ForLoop3
    : FOR   ${i}    IN    1  2  3  4  5         #for double space b/w values will give o/p in new line
    \   log to console  ${i}

ForLoopWithLists
    @{list}     create list  1  2   3   4       #creating lists in Robot framework
    : FOR   ${i}    IN    @{list}
    \   log to console  ${i}

ForLoopWithListsString
    @{list}     create list  Ayan Aparna Chandra Dutta       #creating lists in Robot framework
    : FOR   ${i}    IN    @{list}
    \   log to console  ${i}

ForLoopWithExit
    @{list}     create list  1  2   3   4   5   6   7       #creating lists in Robot framework
    : FOR   ${i}    IN    @{list}
    \   log to console  ${i}
    \   exit for loop if  ${i}==3

##############################################

TC1
    [Tags]  sanity
    log to console  Ayan
TC2
    [Tags]  ff
    log to console  Aparna
TC3
    [Tags]  ff
    log to console  Chandra
TC4
    [Tags]  sanity
    log to console  Dutta
TC5
    [Tags]  sanity
    log to console  Howrah

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
