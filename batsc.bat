:: This batch file checks for network connection problems.
ECHO OFF
:: View network connection details
ipconfig /all
:: Check if Google.com is reachable
ping google.com
:: Run a traceroute to check the route to Google.com
tracert google.com
PAUSE