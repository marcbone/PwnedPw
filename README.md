# PwnedPw
commandline tool to check if your password has been exposed in a data breach


This tool uses the pwnedpasswords.com API to detect if your password has been appeared in a data breach.

Your password is not send to the api. PwnedPw sends only the first 5 letters of your hashed password to the api and checks the results locally

# Usage
`python3 pwnedpw.py`
