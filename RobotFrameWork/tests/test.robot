*** Settings ***
Library   ../keywords/YahooLibrary.py

*** Variables ***
${browser}   chrome
${url}  https://finance.yahoo.com/
${firstName}   Abhishek
${lastName}    Yadav
${email}    Abhishek.yadav@gmail.com
${birthYear}    1998

*** Test Case ***
Yahoo SignUp Test
    Open Browser And Go To Url    ${browser}    ${url}
    Click Sign In Button
    Click Create A Account Button
    Perform Sign Up    ${firstName}    ${lastName}    ${email}    ${birthYear}
    Close Browser

