*** Settings ***
Library                     SeleniumLibrary
Library                     OperatingSystem

Suite Teardown  Close Browser

*** Variables ***
${USER OPENCART URL}        http://192.168.110.60/opencart/
${BROWSER}                  Firefox
${FIRST NAME FIELD}         id:input-firstname
${LAST NAME FIELD}          id:input-lastname
${EMAIL FIELD}              id:input-email
${TELEPHONE FIELD}          id:input-telephone
${PASSWORD FIELD}           id:input-password
${PASSWORD CONFIRM FIELD}   id:input-confirm
${ADD PRODUCT TO CART}      id:button-cart
${OPEN BASKET BUTTON}       id:cart-total
${CONTENT TABLE}            id:content
${LOGIN EMAIL FIELD}        id:input-email
${LOGIN PASSWORD FIELD}     id:input-password
${REMOVE PRODUCT}           xpath://button[@title='Remove']
${ADD TO WISH LIST}         xpath://button[@title='Add to Wish List']
${WISH LIST BUTTON}         xpath://button[@title='Wish List (1)']
${POLICY AGREE BUTTON}      xpath://input[@name='agree']
${CONTINUE REGISTER}        xpath://input[@value='Continue']
${LOGIN LOGIN BUTTON}       xpath://input[@type='submit']
${MY ACCOUNT BUTTON}        xpath://a[@title='My Account']
${TABLETS BUTTON}           xpath://a[@href='http://192.168.110.60/opencart/index.php?route=product/category&path=57']
${GALAXY TAB PRODUCT}       xpath://a[@href='http://192.168.110.60/opencart/index.php?route=product/product&path=57&product_id=49']
${BASKET PRODUCT TABLE}     xpath://a[@href='http://192.168.110.60/opencart/index.php?route=product/product&product_id=49']
${CAMERAS BUTTON}           xpath://a[@href='http://192.168.110.60/opencart/index.php?route=product/category&path=33']
${CANON EOS 5D}             xpath://a[@href='http://192.168.110.60/opencart/index.php?route=product/product&path=33&product_id=30']
${REGISTER BUTTON}          xpath://a[@href='http://192.168.110.60/opencart/index.php?route=account/register']
${LOGIN BUTTON}             xpath://a[@href='http://192.168.110.60/opencart/index.php?route=account/login']
${LOGOUT BUTTON}            xpath://a[@href='http://192.168.110.60/opencart/index.php?route=account/logout']


*** Keywords ***
Open user opencart
    Open Browser            url=${USER OPENCART URL}
    ...                     browser=${BROWSER}

*** Test Cases ***
Add product to basket
    Open user opencart
    Click Element           locator=${TABLETS BUTTON}
    Click Element           locator=${GALAXY TAB PRODUCT}
    Click Element           locator=${ADD PRODUCT TO CART}
    Click Element           locator=${OPEN BASKET BUTTON}
    Table Should Contain    locator=${BASKET PRODUCT TABLE}
    ...                     expected=Samsung Galaxy Tab 10.1
    Click Element           locator=${REMOVE PRODUCT}
    Close Browser

Add new user
    Open user opencart
    Click Element           locator=${MY ACCOUNT BUTTON}
    Click Element           locator=${REGISTER BUTTON}
    Input Text              locator=${FIRST NAME FIELD}
    ...                     text=support
    Input Text              locator=${LAST NAME FIELD}
    ...                     text=support
    Input Text              locator=${EMAIL FIELD}
    ...                     text=support@otus.ru
    Input Text              locator=${TELEPHONE FIELD}
    ...                     text=89111111111
    Input Password          locator=${PASSWORD FIELD}
    ...                     password=elephant
    Input Password          locator=${PASSWORD CONFIRM FIELD}
    ...                     password=elephant
    Click Element           locator=${POLICY AGREE BUTTON}
    Click Element           locator=${CONTINUE REGISTER}
    Table Should Contain    locator=${CONTENT TABLE}
    ...                     expected=Congratulations! Your new account has been successfully created!
    Close Browser

Login to opencart
    Open user opencart
    Click Element           locator=${MY ACCOUNT BUTTON}
    Click Element           locator=${LOGIN BUTTON}
    Input Text              locator=${LOGIN EMAIL FIELD}
    ...                     text=support@otus.ru
    Input Password          locator=${LOGIN PASSWORD FIELD}
    ...                     password=elephant
    Click Element           locator=${LOGIN LOGIN BUTTON}
    Table Should Contain    locator=${CONTENT TABLE}
    ...                     expected=My Account
    Close Browser

Logout from opencart
    Open user opencart
    Click Element           locator=${MY ACCOUNT BUTTON}
    Click Element           locator=${LOGIN BUTTON}
    Input Text              locator=${LOGIN EMAIL FIELD}
    ...                     text=support@otus.ru
    Input Password          locator=${LOGIN PASSWORD FIELD}
    ...                     password=elephant
    Click Element           locator=${LOGIN LOGIN BUTTON}
    Click Element           locator=${MY ACCOUNT BUTTON}
    Click Element           locator=${LOGOUT BUTTON}
    Table Should Contain    locator=${CONTENT TABLE}
    ...                     expected=You have been logged off your account. It is now safe to leave the computer.
    Close Browser

Add product to wish list
    Open user opencart
    Click Element           locator=${MY ACCOUNT BUTTON}
    Click Element           locator=${LOGIN BUTTON}
    Input Text              locator=${LOGIN EMAIL FIELD}
    ...                     text=support@otus.ru
    Input Password          locator=${LOGIN PASSWORD FIELD}
    ...                     password=elephant
    Click Element           locator=${LOGIN LOGIN BUTTON}
    Click Element           locator=${CAMERAS BUTTON}
    Click Element           locator=${CANON EOS 5D}
    Click Element           locator=${ADD TO WISH LIST}
    Click Element           locator=${WISH LIST BUTTON}
    Table Should Contain    locator=${CONTENT TABLE}
    ...                     expected=Canon EOS 5D
    Close Browser
