## Practice Python GUI. 
```
1.You have to put the picture to c drive-> Temp.
2.You have to install chrome driver.
```
+ Go to chrome and select chrome driver and click first website.
+ And check your chrome version.
+ Check your top right (near by your profile).
+ Find help and continue to find chrome information.
----------
```python
from tkinter import*
```
```python
from selenium import webdriver
```
```python
def login():
    driver=webdriver.Chrome("C:\Temp/chromedriver.exe")
    ...
```
+ This is call chrome driver.
----------
```python
btn.config(command=login)
```
+ Use command to active.
+ if you click the button then you can Auto login. 
----------
