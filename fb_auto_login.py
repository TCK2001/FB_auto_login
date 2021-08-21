from tkinter import*
from selenium import webdriver

win=Tk()
win.title("TCK FB_LOGIN")
win.geometry("500x300")
win.option_add("*Font","궁서,20")
win.configure(background="Ivory")

#image
labn=Label(win)
ima=PhotoImage(file="C:\Temp/fb.png")
img=ima.subsample(1)
labn.config(image=img)
labn.pack()

#id
lab1=Label(win)
lab1.config(text="ID",fg="blue")
lab1.pack()

ent1=Entry(win)
ent1.insert(0,"abcd@abcd.com")
def clear(event):
    if ent1.get()=="abcd@abcd.com":
        ent1.delete(0,len(ent1.get()))

ent1.bind("<Button -1>",clear) #이런 이런 기능이 들어왔을때 이것을 실행해라<Button -3>은 오른쪽
ent1.pack()

#pw
lab2=Label(win)
lab2.config(text="PASSWORD",fg="blue")
lab2.pack()

ent2=Entry(win)
ent2.config(show="*")
ent2.pack()

def login():
    driver=webdriver.Chrome("C:\Temp/chromedriver.exe")
    url="https://www.facebook.com/"
    driver.get(url)
    driver.implicitly_wait(5)
    xpath1="//input[@name='email']"
    driver.find_element_by_xpath(xpath1).send_keys(ent1.get())
    driver.implicitly_wait(5)
    xpath2="//input[@name='pass']"
    driver.find_element_by_xpath(xpath2).send_keys(ent2.get())
    driver.implicitly_wait(5)
    xpath3="//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']"
    driver.find_element_by_xpath(xpath3).click()
    driver.implicitly_wait(5)
    lab3.config(text="Login SUCCESS!",fg="blue")

#button
btn=Button(win)
btn.config(text="Login",fg="blue")
btn.config(command=login)
btn.pack()

#3
lab3=Label(win)
lab3.pack()


win.mainloop()