*** Settings ***
Library  Collections
Library  RequestsLibrary

*** Variables ***
${base_url}     https://mphasis.com

*** Test Cases ***
BasicAuthentication
    ${auth}=    create list  AyanUser   DuttaPassword
    create session      mysession   ${base_url}     auth=${auth}
    ${response}=    get request     mysession      /authentication/check
    log to console  ${response.content}
    should be equal as strings  ${response.status_code}     200

