import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

def main():
    window = tk.Tk()
    the_convas = tk.Canvas(window, width=400, height=250, bg='grey', relief='raised')
    the_convas.pack()

    wind_lbl = tk.Label(window, text="Welcome!", bg='grey', fg='white')
    wind_lbl.config(font=('helvetica', 30, 'bold italic'))
    window.title("Image Converter")

    the_convas.create_window(200, 60, window=wind_lbl)

    browse_png = tk.Button(text="Select PNG file", command=get_png, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
    the_convas.create_window(100, 140, window=browse_png)

    browse_jpg = tk.Button(text="Select JPG file", command=get_jpg, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
    the_convas.create_window(300, 140, window=browse_jpg)

    save_as_jpg = tk.Button(text="Convert PNG to JPG", command=png_to_jpg, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
    the_convas.create_window(100, 190, window=save_as_jpg)

    save_as_png = tk.Button(text="Convert JPG to PNG", command=jpg_to_png, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
    the_convas.create_window(300, 190, window=save_as_png)

    window.mainloop()


def get_png():
    global img
    import_file_path = filedialog.askopenfilename()
    img = Image.open(import_file_path)
    img = img.convert("RGB")
    messagebox.showinfo("Notification", "An image has been selected!")


def get_jpg():
    global img
    import_file_path = filedialog.askopenfilename()
    img = Image.open(import_file_path)
    messagebox.showinfo("Notification", "An image has been selected!")


def png_to_jpg():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    img.save(export_file_path)
    messagebox.showinfo("Notification", "Conversion from PNG to JPG complete!")


def jpg_to_png():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    img.save(export_file_path)
    messagebox.showinfo("Notification", "Conversion from JPG to PNG complete!")


main()
