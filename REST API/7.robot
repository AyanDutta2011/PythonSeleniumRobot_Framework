*** Settings ***
Library  Collections
Library  RequestsLibrary
Library  OperatingSystem

*** Variables ***
${base_url}     https://mphasis.com
${bearerToken}      "Bearer A536GHVBDSJMI347UY34UOVCJHBJBHJBJ63478V8Y8VYT8UV8GU8GG8GU8"

*** Test Cases ***
BearerAuthentication_Token
    create session      mysession   ${base_url}
    ${headers}  create dictionary  Authorization=${bearerToken}     Content-Type=text/xml
    ${req_body}=    get file  C:/Selenium/test/PostData.txt

    ${response}=    post request  mysession     /   data=${req_body}    headers=${headers}
    log to console  ${response.status_code}
    log to console  ${response.content}


