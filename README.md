# Calculator modal API testing

## Pre-requisites
    1. Python 3.11 or newer
    2. Powershell

## Test execution - Powershell
    python -m venv .venv
    .venv/Scripts/activate
    pip install -r .\requirements.txt
    pytest .\unit_tests\ --html=report.html

This will create a report report.html, which will display the test report. 

I have also added my own generated report named final_report.html, in case previous instructions fail and report is not generated.
