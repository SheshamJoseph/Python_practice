import requests
import io
from bs4 import BeautifulSoup
from tkinter import Tk, Label
# import pillow for processing images
from PIL import Image, ImageTk  

window = Tk()
window.title("XKCD Comics scraper")
window.minsize(width=400, height=500)
window.config(background="white")
# TODO: figure out how to get another image when we go next, 
# TODO: refresh on crawler models

# Get the xkcd homepage
comics_base = "https://imgs.xkcd.com/comics/a"
response = requests.get(url="https://xkcd.com/")
soup = BeautifulSoup(response.text, "html.parser")
image = soup.find(id="comic").find("img").get("src")
full_img_link = "".join(["https:", image])
# print(full_img_link)

image = requests.get(url=full_img_link)
print(image.text)
im = Image.open(io.BytesIO(image.content))
img = ImageTk.PhotoImage(im)
label = Label(window, image=img)
label.pack()

window.mainloop()

