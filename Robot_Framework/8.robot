#taking keywords from 7.robot
*** Keywords ***
Launch_LogIn2
    [Arguments]     ${appurl}   ${appbrowser}
    open browser    ${appurl}  ${appbrowser}
    maximize browser window



*** Test Cases ***
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
