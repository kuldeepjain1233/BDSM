from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# def openFile():
    # filepath = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("CSV files", "*.csv"), ("Image files", "*.png;*.jpg;*.jpeg")))
    # if filepath:
    #     if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
    #         # Handle image files
    #         image = Image.open(filepath)
    #         image.show()
    #     else:
    #         # Handle text and CSV files
    #         file = open(filepath, 'r')
    #         content = file.read()
    #         print(content)
    #         file.close()
    # return filepath
filepath=filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("CSV files", "*.csv"), ("Image files", "*.png;*.jpg;*.jpeg")))
print(filepath)
window = Tk()
# button = Button(text="Open", command=filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("CSV files", "*.csv"), ("Image files", "*.png;*.jpg;*.jpeg"))))
# button.pack()
window.mainloop()
