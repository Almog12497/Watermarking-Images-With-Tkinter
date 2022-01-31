import tkinter as tk
from tkinter import PhotoImage, filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
from sqlalchemy import column


window = tk.Tk()
window.title = "Watermark images"
window.minsize(400, 400)

def select_file():
    global my_image_viewer
    global watermark_image
    global img
    global img_and_txt
    global img_and_txt_view
    
    # Define possible file types
    filetypes = (
        ('images',"*.jpg",),
        ('All files', '*.*')
    )

    # Get the image you want to watermark
    filename = filedialog.askopenfile(mode='r', filetypes=filetypes)
    
    # Views the image without watermark
    my_image_viewer.config(image="")
    img_r = Image.open(filename.name,).convert("RGBA")
    img = ImageTk.PhotoImage(img_r)
    my_image_viewer = tk.Label(image=img)
    my_image_viewer.grid(row=2,column=0)
    
    # Views the image with watermark
    
    # Creates image with text
    txt = Image.new("RGBA", img_r.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)
    font = ImageFont.truetype("arial.ttf", 50)
    
    # Makes the text with 50% oppacity
    draw.text((100,100), "Almog", (255, 255, 255, 128), font=font)
    
    # Combines img and txt
    img_and_txt = Image.alpha_composite(img_r,txt)
    img_and_txt_view = ImageTk.PhotoImage(img_and_txt)
    watermark_image = tk.Label(image=img_and_txt_view )
    watermark_image.grid(row=2, column=1)
    save_btn = tk.Button(text="Save", command=save_file).grid(row=3,column=0,columnspan=2)


def save_file():
    filename = filedialog.asksaveasfile(mode="w", defaultextension=".png")
    if not filename:
        return
    img_and_txt.save(filename.name)

# Creates the simple gui
title = tk.Label(text="Image Watermarking").grid(row=0, column=0, columnspan=2)
button = tk.Button(text="Open image to watermark", command=select_file).grid(row=1,column=0, columnspan=2)
my_image_viewer = tk.Label()
watermark_image = tk.Label()


window.mainloop()