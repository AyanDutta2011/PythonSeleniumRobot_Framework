*** Settings ***
Library  XML
Library  OS
Library  Collections

*** Test Cases ***
XML Data Validation
    ${xml_obj}=     parse xml  C:/Ayan/xmldata/emp.xml

    #validations

    #Check the single element value
    ${emp_firstname}=   get element text  ${xml_obj}    .//employee[1]/firstname
    should be equal  ${emp_firstname}    Ayan

    ${emp_firstname}=   get element  ${xml_obj}    .//employee[1]/firstname
    should be equal  ${emp_firstname.text}    Ayan

    element text should be  ${xml_obj}  Ayan    .//employee[1]/firstname

    #check no of elements
    ${emp_count}=   get element count  .//employee
    should be equal as integers  ${emp_count}   10

    #check attribute presence
    element attribute should be  ${xml_obj}     id  99  .//employee[1]

    #check values of child elements
    ${child_element}=   get child elements  ${xml_obj}    .//employee[1]
    should not be empty  ${child_element}

    ${fname}=   get element text  ${child_element[0]}
    ${lname}=   get element text  ${child_element[1]}
    ${title}=   get element text  ${child_element[2]}

    should be equal  ${fname}   Ayan
    should be equal  ${lname}   Dutta
    should be equal  ${title}   Engineer



