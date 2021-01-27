*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     https://localhost:8000

*** Test Cases ***
TC1: Returns all the video games (GET)
    create session      mysession   ${base_url}     #main/base URL
    ${response}=    get request     mysession      /app/videogames
    log to console      ${response.status_code}
    log to console      ${response.content}
    log to console      ${response.headers}

    #validations
    ${status_code}=     convert to string       ${response.status_code}
    should be equal  ${status_code} 200

TC2: Add a new video game (POST)
    create session      mysession   ${base_url}
    ${body}=    create dictionary  id=100  name=COD  catagory=Action
    ${header}=  create dictionary  Content-Type=application/json
    ${response}=    post request  mysession     /app/videogames     data=${body}    header=${header}  #relative URL

    ${status_code}=     convert to string       ${response.status_code}
    should be equal  ${status_code} 200

    ${res_body}=     convert to string       ${response.content}
    should be equal  ${res_body}  Record added successfully

TC3: Returns the details of a single game by ID (GET)   #extracted specific game record by ID
    create session      mysession   ${base_url}     #main/base URL
    ${response}=    get request     mysession      /app/videogames/100  #relative URL
    log to console      ${response.status_code}
    log to console      ${response.content}
    log to console      ${response.headers}

    #validations
    ${status_code}=     convert to string       ${response.status_code}
    should be equal  ${status_code} 200

    ${res_body}=     convert to string       ${response.content}
    should be equal  ${res_body}  COD

TC4: Update an exsisting video game by specifying a new body (PUT)
    create session      mysession   ${base_url}
    ${body}=    create dictionary  id=100  name=PUBG  catagory=Action
    ${header}=  create dictionary  Content-Type=application/json
    ${response}=    put request     mysession     /app/videogames/100     data=${body}    header=${header}  #relative URL

    ${status_code}=     convert to string       ${response.status_code}
    should be equal  ${status_code} 200

    ${res_body}=     convert to string       ${response.content}
    should be equal  ${res_body}  PUBG

TC5: Delete a video game by ID (DELETE)
    create session      mysession   ${base_url}
    ${response}=    delete request  /app/videogames/100

    ${status_code}=     convert to string       ${response.status_code}
    should be equal  ${status_code} 200

    ${res_body}=     convert to string       ${response.content}
    should be equal  ${res_body}  Record deleted successfully

*** Keywords ***
 