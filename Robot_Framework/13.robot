*** Settings ***
Library  SeleniumLibrary

Suite Setup     log to console  open_browser        #execute once before Test case execution starts
Suite Teardown      log to console   close_browser  #execute once after Test case execution ends

Test Setup  log to console  sign_in     #execute before each and every test case
Test Teardown  log to console   sign_out    #execute after each and every test case

*** Test Cases ***
TC1
    log to console  Ayan
TC2
    log to console  Aparna
TC3
    log to console  Chandra
