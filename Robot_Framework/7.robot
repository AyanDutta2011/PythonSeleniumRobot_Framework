*** Settings ***
Library  SeleniumLibrary
Resource  C:/Users/Ayan Dutta/PycharmProjects/Automation/Robot_Framework/8.robot

*** Variables ***
${url}  https://appaccess.mphasis.com/oam/server/obrareq.cgi?encquery%3DL%2FamMvRDANotJPlt4XRQFdmbSdeMDOupUTYV5sPVuaeTkql2Df4PS9mud3TB63OJ0%2B42b%2FDWp%2BkITrfRnq2OFvpAFDbViXFzFlZZQ7PzdIWK7qA6rDoBNptCHN2iuQdBZ26HCjdyhjr05SNNPmO5EaiCMFszr9nnmPOv1IdInb1PXH%2B%2FwtTarf0d53XAcSFaiTlcw6dTJrE1BOoNVaLOjpzkZBXJXAeeT7FyWx2UEukLvgz4xWFCZbbS%2Fl7plBFHPUKm6JAo2mvrhERreVF2Ww5bingw94nS06CX4bBIVHVfGu%2BL6K4QO5oubz4UWSVe%20agentid%3DOHS1Agent%20ver%3D1%20crmethod%3D2
${browser}  chrome


*** Test Cases ***
TC1
    Launch_LogIn2    ${url}  ${browser}         #importing Launch_LogIn2 keyword from another .robot file
    sleep  5
    close browser

*** Keywords ***
Launch_LogIn
    [Arguments]     ${appurl}   ${appbrowser}
    open browser    ${appurl}  ${appbrowser}
    maximize browser window

