*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     https://flipkart.com

*** Test Cases ***
GET_REST API
    create session  mysession   ${base_url}
    ${response}=    get request     mysession  /relative/url
    log to console  ${response.status_code}
    log to console  ${response.content}
    log to console  ${response.headers}

    ${sts_code}=    convert to string  ${response.status_code}
    should be equal  ${sts_code}    200

POST_Rest API
    create session  mysession   ${base_url}
    ${body}=    create dictionary  id=100   name=mobile
    ${headers}=     create dictionary  Content-Type=application/json
    ${response}=    post request  mysession     /relative/url   data=${body}    header=${headers}

    ${content}=     convert to string   ${response.content}
    should be equal  ${content}     Record Added Successfully

GET a single value_REST API
    create session  mysession   ${base_url}
    ${response}=    get request     mysession  /relative/url/100

    ${sts_body}=    convert to string  ${response.content}
    should be equal  ${sts_body}    mobile

PUT_REST API
    create session  mysession   ${base_url}
    ${body}=    create dictionary  id=100   name=fridge
    ${headers}=     create dictionary  Content-Type=application/json
    ${response}=    put request  mysession     /relative/url   data=${body}    header=${headers}

    ${content}=     convert to string   ${response.content}
    should be equal  ${content}     fridge

DELETE_REST API
    create session  mysession   ${base_url}
    ${response}=    delete request   mysession     /relative/url/100

    ${content}=     convert to string   ${response.content}
    should be equal  ${content}     Record deleted Successfully

