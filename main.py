from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    passward = passward_entry.get()

    if website=="" or passward=="":
        messagebox.showwarning(title=" 🤨🤨🤨 ",message="hey do not leave any field empty")

    # messagebox.showinfo(title="Title", message="Message")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"these are the details entered \nEmail: {username}\nPassward: {passward}\n is it ok to save ?")

        if is_ok:
            f=open("passward_data.txt","a")

            f.write(f"{website} | {username} | {passward} \n")
            website_entry.delete(0,END)
            # username_entry.delete()
            passward_entry.delete(0,END)
            f.close()




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("passward manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)


website_label=Label(text="Website")
website_label.grid(column=0,row=1)

website_entry=Entry(width=40)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

username_label=Label(text="Email/Username")
username_label.grid(column=0,row=2)

username_entry=Entry(width=40)
username_entry.grid(column=1,row=2,columnspan=2)
username_entry.insert(0,"shukla.ayush2001@gmail.com") #the 0/END here is index calculated from where is cursor right now


passward_label=Label(text="Passward")
passward_label.grid(column=0,row=3)

passward_entry=Entry(width=22)
passward_entry.grid(column=1,row=3)

generate_button=Button(text="Generate passward")
generate_button.grid(column=2,row=3)

add_button=Button(text="Add",width=34,command=save)
add_button.grid(column=1,row=4,columnspan=2)



window.mainloop()

