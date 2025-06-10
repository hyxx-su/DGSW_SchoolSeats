from tkinter import *
tk = Tk()

counter = 0
def clicked():
    global counter #전역변수 counter
    counter += 1
    label1['text'] = '버튼 클릭 수: ' + str(counter)


def reset():
    global counter
    counter = 0
    label1['text'] = '옆에 버튼이 있습니다.'


tk.title('GUI예제') 


label1=Label(tk, text='옆에 버튼이 있습니다.',fg='blue',font=20) # fg는 글자 색 지정, font로 글자 설정
label1.pack(side=LEFT, padx=10, pady=10)

button3 = Button(tk,text='클릭해 보세요.',bg='green',font=15,width=30,height=5,command= clicked) #command로 버튼 클릭 시 동작할 함수 지정, bg로 색상지정, width,height로 각각 넓이 높이 지정
button3.pack(side=LEFT, padx=10, pady=10)

button4 = Button(tk,text='reset',bg='red',width=30,height=5,font=15,command=reset)
button4.pack(side=LEFT,padx=10, pady=10)
tk.mainloop()