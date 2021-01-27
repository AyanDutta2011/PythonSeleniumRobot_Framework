*** Settings ***
Library  XML
Library  OS
Library  Collections

*** Test Cases ***
XML_validations
    ${xml}=     parse xml  C:/selenium/REST_API/customer.xml

    element text should be  ${xml}  Ayan    .//customer[1]/firstname

    ${count}=   get element count  .//customer
    should be equal as integers  ${count}   100

    element attribute should be  ${xml}     id  100     .//customer[1]

    ${child}=   get child elements  ${xml}  .//customer[1]
    should not be empty  ${child}

    ${id}=  get element text  ${child[1]}
    ${name}=  get element text  ${child[2]}

    should be equal     ${child[1]}     100
    should be equal     ${child[2]}     Ayan