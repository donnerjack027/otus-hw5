*** Settings ***
Library  SeleniumLibrary
Library  DatabaseLibrary

Suite Setup     Open user opencart
Suite Teardown  Close Browser

*** Variables ***
${USER OPENCART URL}                http://192.168.110.60/opencart/admin/
${BROWSER}                          Firefox
${USER NAME}                        admin
${PASSWORD}                         admin
${USER NAME FIELD}                  id:input-username
${PASSWORD FIELD}                   id:input-password
${NEW PRODUCT NAME}                 id:input-name1
${META TAG}                         id:input-meta-title1
${CONTENT FIELD}                    id:content
${FILTER NAME}                      id:input-name
${FILTER BUTTON}                    id:button-filter
${PRODUCT TABLE}                    id:form-product
${MODEL FILED}                      id:input-model
${CATALOG BUTTON}                   id:menu-catalog
${PRODUCTS BUTTON}                  link:Products
${ACCEPT LOGIN BUTTON}              xpath://button[@type='submit']
${CLOSE ALERT}                      xpath://button[@class='close']
${ADD PRODUCT BUTTON}               xpath://a[@data-original-title='Add New']
${DATA TAB}                         xpath://a[@href='#tab-data']
${SAVE NEW PRODUCT}                 xpath://button[@data-original-title='Save']
${CHOOSE PRODUCTS}                  xpath://input[@name='selected[]']
${REMOVE BUTTON}                    xpath://button[@data-original-title='Delete']
${PRODUCT}                          class:img-thumbnail

*** Keywords ***
Open user opencart
    Open Browser                    url=${USER OPENCART URL}
    ...                             browser=${BROWSER}
    Capture Page Screenshot

Login opencart
    Input Text                      locator=${USER NAME FIELD}
    ...                             text=${USER NAME}
    Input Password                  locator=${PASSWORD FIELD}
    ...                             password=${PASSWORD}
    Capture Page Screenshot
    Click Element                   locator=${ACCEPT LOGIN BUTTON}
    Click Element                   locator=${CLOSE ALERT}
    Capture Page Screenshot

*** Test Cases ***
Add product
    Login opencart
    Click Element                   locator=${CATALOG BUTTON}
    Capture Page Screenshot
    Click Element                   locator=${PRODUCTS BUTTON}
    Capture Page Screenshot
    Click Element                   locator=${ADD PRODUCT BUTTON}
    Capture Page Screenshot
    Input Text                      locator=${NEW PRODUCT NAME}
    ...                             text=Test Product
    Capture Page Screenshot
    Input Text                      locator=${META TAG}
    ...                             text=Test Tag
    Capture Page Screenshot
    Click Element                   locator=${DATA TAB}
    Capture Page Screenshot
    Input Text                      locator=${MODEL FILED}
    ...                             text=Test Model
    Capture Page Screenshot
    Click Element                   locator=${SAVE NEW PRODUCT}
    Capture Page Screenshot
    Input Text                      locator=${FILTER NAME}
    ...                             text=Test Product
    Capture Page Screenshot
    Click Element                   locator=${FILTER BUTTON}
    Capture Page Screenshot
    Table Should Contain            locator=${PRODUCT TABLE}
    ...                             expected=Test Product
    Capture Page Screenshot

Remove product
    Input Text                      locator=${FILTER NAME}
    ...                             text=Test Product
    Capture Page Screenshot
    Click Element                   locator=${FILTER BUTTON}
    Capture Page Screenshot
    Click Element                   locator=${CHOOSE PRODUCTS}
    Capture Page Screenshot
    Click Element                   locator=${REMOVE BUTTON}
    Capture Page Screenshot
    Alert Should Be Present         action=ACCEPT
    Capture Page Screenshot
    Page Should Not Contain         text=Text Product
    Wait Until Element Is Enabled   locator=${CATALOG BUTTON}
    ...                             timeout=5
    Capture Page Screenshot
    ${count}=   Get Count           ${PRODUCT}  ${PRODUCT TABLE}
    Log                             ${count}
    should be equal                 '${count}'     '0'
