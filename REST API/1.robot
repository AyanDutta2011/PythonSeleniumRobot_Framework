*** Settings ***
Library     RequestsLibrary

*** Variables ***
${base_url}     https://https://www.indiabix.com
${sub}     questions-and-answers

*** Test Cases ***
Get_WeatherInfo
    create session      mysession   ${base_url}
    ${response}=    get request     mysession      /computer-science/${sub}
    log to console      ${response.status_code}
    log to console      ${response.content}
    log to console      ${response.headers}

*** Keywords ***
