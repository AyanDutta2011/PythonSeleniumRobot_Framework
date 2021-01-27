*** Settings ***
Library  Collections
Library  RequestsLibrary

*** Variables ***
${base_url}     https://mphasis.com

*** Test Cases ***
TestHeaders
    create session      mysession   ${base_url}     #main/base URL
    ${response}=    get request     mysession      /app/videogames
    log to console      ${response.headers}     #display all the headers
    # one header validation
    ${ContentTypeValue}=    get from dictionary  ${response.headers}    Content-Type   #this is one of the header
    should be equal  ${ContentTypeValue}    demo_data

TestCookies
    create session      mysession   ${base_url}     #main/base URL
    ${response}=    get request     mysession      /app/videogames

    log to console  ${response.cookies}     #display all the cookies

    ${CookieValue}=    get from dictionary  ${response.cookies}
    log to console  ${CookieValue}
