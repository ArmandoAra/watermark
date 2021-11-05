from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageGrab



tk = Tk()
tk.title("Watermark generator")
tk.minsize(width=800, height=500)


image_created = None
canvas = None
text_entry_value = ""
user_text = ""
position_water_mark = [100, 100]


#### Functions #######
def insert_image():
    global image_created,canvas
    if not canvas == None:
        canvas.delete(image_created)
    image = filedialog.askopenfilename(initialdir="C:/Users/arman\OneDrive\Desktop\Story")
    user_image = PhotoImage(file=image)
    new_image = user_image.subsample(5, 5)
    canvas = Canvas(width=new_image.width(), height=new_image.height())
    canvas.grid(row=2, column=1)
    image_created = canvas.create_image(new_image.width()/2, new_image.height()/2, image=new_image)
    position_water_mark[0] = new_image.width() - 35
    position_water_mark[1] = new_image.height() - 20
    tk.mainloop()
    return position_water_mark

def delete_image():
    canvas.delete(image_created)
    print("Delete")

def write_image():
    global user_text
    if user_text:
        canvas.delete(user_text)
    user_text = canvas.create_text(position_water_mark[0], position_water_mark[1], text=text_entry.get(), fill="white")
    tk.mainloop()


def process_image():
    canvas.update()
    x = tk.winfo_rootx()+canvas.winfo_x()
    y = tk.winfo_rooty()+canvas.winfo_y()
    x_1 = x+canvas.winfo_width()
    y_1 = y+canvas.winfo_height()

    ImageGrab.grab().crop((x,y,x_1,y_1)).save(f'{filename_entry.get()}.png')
    tk.mainloop()


######### Buttons and interface ############

write_button = Button(text="Write Image", command=write_image)
write_button.grid(row=1, column=2)

insert_button = Button(text="Insert Image", command=insert_image)
insert_button.grid(row=3, column=0)

delete_button = Button(text="Delete Image", command=delete_image)
delete_button.config(bg="red")
delete_button.grid(row=3, column=1)

process_button = Button(text="Process Image", command=process_image)
process_button.grid(row=3, column=2)

###### Labels ##########
my_label = Label(text="Insert your image", font=("Arial", 24))
my_label.grid(row=0, column=1)

filename_label = Label(text="File Name:", font=("Arial", 12))
filename_label.grid(row=4, column=1, sticky="e" )

text_entry_label = Label(text="What do you want write")
text_entry_label.grid(row=1, column=0)

text_entry = Entry( width=30)
text_entry.grid(row=1, column=1)

filename_entry = Entry( width=30)
filename_entry.grid(row=4, column=2)

tk.mainloop()
