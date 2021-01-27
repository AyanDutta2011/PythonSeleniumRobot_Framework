*** Settings ***
Library  XML
Library  OS
Library  Collections
Library  RequestsLibrary

*** Variables ***
${base_url}     https://mphasis.com

*** Test Cases ***
XML Response Validation
    create session      mysession   ${base_url}
    ${response}=    get request     mysession      /customer/15
    ${xml_string}=  convert to string  ${response.content}
    ${xml_obj}=     parse xml  ${xml_string}

    #check single element value
    element text should be    ${xml_obj}    15  .//ID

    #check multiple values
    ${child_element}=   get child elements  ${xml_obj}
    should not be empty  ${child_element}

    ${id}=  get element text  ${child_element[0]}
    ${fname}=  get element text  ${child_element[1]}
    ${lname}=  get element text  ${child_element[2]}

    should be equal  ${id}  15
    should be equal  ${fname}  Ayan
    should be equal  ${lname}  Dutta
