from tkinter import *
import db.dao as dao

def create():
    mem_list=[]

    id = id_text.get()
    pw = pw_text.get()
    name = name_text.get()
    tel = tel_text.get()

    mem_list.append(id)
    mem_list.append(pw)
    mem_list.append(name)
    mem_list.append(tel)

    dao.create(mem_list)

    # 강사님 풀이이
   # vo = [id_text.get(),pw_text.get(),name_text.get(),tel_text.get()]
    # dao.create(vo)
def delete():
    id = id_text.get()

    dao.delete([id])

# w=틀
w = Tk()
w.geometry('500x800')
w.config(bg='lightgray')

icon=PhotoImage(file='../db_test/팬케이크쿠키.png')
dogLabel=Label(w,image=icon)
dogLabel.pack()
#.pack() : 그래프에 올려주는 역할

id_label = Label(w,text='아이디입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
id_label.pack()

id_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
id_text.pack()

pw_label = Label(w,text='패스워드입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
pw_label.pack()

pw_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
pw_text.pack()

name_label = Label(w,text='이름입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
name_label.pack()

name_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
name_text.pack()

tel_label = Label(w,text='전화번호입력',font=('맑은 고딕',20),bg='lightgray',fg='blue')
tel_label.pack()

tel_text=Entry(w,font=('맑은 고딕',20),bg='yellow',fg='red')
tel_text.pack()

# font =(,) : 입력값이 튜플
button = Button(w,width=30,height=3,bg='green',font=('맑은 고딕',10),text='회원가입',command=create)
button.pack()

button2 = Button(w,width=30,height=3,bg='green',font=('맑은 고딕',10),text='회원탈퇴',command=delete)
button2.pack()

# 창이 계속 떠있어야 하기 때문에 제일 아래에 써줘야한다.
w.mainloop()