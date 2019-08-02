*** Variables ***
${LIBRARIES}  ${EXECDIR}/../robot_hw/lib

*** Settings ***
Library  SeleniumLibrary
Library  ${LIBRARIES}/TestLib.py

*** Test Cases ***
Login user opencart
    User opencart test

Login admin opencart
    Admin opencart test


