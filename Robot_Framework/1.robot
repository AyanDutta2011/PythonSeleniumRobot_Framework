*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://appaccess.mphasis.com/oam/server/obrareq.cgi?encquery%3DL%2FamMvRDANotJPlt4XRQFdmbSdeMDOupUTYV5sPVuaeTkql2Df4PS9mud3TB63OJ0%2B42b%2FDWp%2BkITrfRnq2OFvpAFDbViXFzFlZZQ7PzdIWK7qA6rDoBNptCHN2iuQdBZ26HCjdyhjr05SNNPmO5EaiCMFszr9nnmPOv1IdInb1PXH%2B%2FwtTarf0d53XAcSFaiTlcw6dTJrE1BOoNVaLOjpzkZBXJXAeeT7FyWx2UEukLvgz4xWFCZbbS%2Fl7plBFHPUKm6JAo2mvrhERreVF2Ww5bingw94nS06CX4bBIVHVfGu%2BL6K4QO5oubz4UWSVe%20agentid%3DOHS1Agent%20ver%3D1%20crmethod%3D2
${browser}  chrome

*** Test Cases ***
Login
    open browser    ${url}  ${browser}
    maximize browser window
    input text  xpath://*[@id="textfield"]    23599151245
    input text  xpath://*[@id="password"]   Aparna%11201996
    click element   xpath://*[@id="submit"]
    title should be     AppAccess
    ${HCM}  set variable  xpath://*[@id="directsec"]/img    #creating variable
    element should be enabled   ${HCM}
    element should be visible  ${HCM}
    sleep  5 sec
    click element   xpath:/html/body/section[1]/div/div/div[5]/font/a/strong/img
    close browser

*** Keywords ***
