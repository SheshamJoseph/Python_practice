import requests
import io
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Button, Canvas
# import pillow for processing images
from PIL import Image, ImageTk  

PAGE_NUMBER = 1

window = Tk()
window.title("XKCD Comics scraper")
window.minsize(width=400, height=500)
window.config(background="black", padx=50, pady=50)
# TODO: figure out how to get another image when we go next, 
# TODO: refresh on crawler models

comics_base = "https://imgs.xkcd.com/comics/a"
home_link = "https://xkcd.com/"
nav_links = []
current_comic = None

# this function gets the page with the comic
def get_page(link):
    global nav_links
    # nav_links.clear()
    try:
        response = requests.get(url=link)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        image = soup.find(id="comic").find("img").get("src")
        full_img_link = "".join(["https:", image])
        # comic = get_image(full_img_link)
        buttons = soup.find(class_="comicNav").find_all("a")
        nav_links = [button.get("href") for button in buttons]
        return full_img_link


# this fuctions retrieves the image
def get_image(image_url):
    try:
        image = requests.get(url=image_url)
        image.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
    else:
        im = Image.open(io.BytesIO(image.content))
        img = ImageTk.PhotoImage(im)
        return img
    
def update_comic(link):
    global current_comic
    img = get_image(link)
    if img is not None:
        current_comic = img
        canvas.itemconfig(comic_image, image=current_comic)
        window.update()

def get_first_page():
    if nav_links and len(nav_links) > 0:
        link = "".join(["https://xkcd.com", nav_links[0]])
        image_link = get_page(link)
        update_comic(image_link)

def get_prev_page():
    if nav_links and len(nav_links) > 1:
        link = "".join(["https://xkcd.com", nav_links[1]])
        image_link = get_page(link)
        update_comic(image_link)

def get_random_page():
    if nav_links and len(nav_links) > 2:
        link = "".join(["https:", nav_links[2]])
        image_link = get_page(link)
        update_comic(image_link)

def get_next_page():
    if nav_links and len(nav_links) > 3:
        link = "".join(["https://xkcd.com", nav_links[3]])
        image_link = get_page(link)
        update_comic(image_link)

def get_last_page():
    if nav_links and len(nav_links) > 3:
        link = "".join(["https://xkcd.com", nav_links[4]])
        image_link = get_page(link)
        update_comic(image_link)


image_link = get_page(home_link)
if image_link:
    current_comic = get_image(image_link)
    if current_comic:

# label = Label(window, image=image, height=294, width=294)
# label.grid(row=1, column=1, columnspan=5)
        canvas = Canvas(height=500, width=800)
        comic_image = canvas.create_image(400, 250, image=current_comic)
        canvas.grid(row=1, column=1, columnspan=5, padx=20, pady=20)

        first_page_btn = Button(text="First page", command=get_first_page)
        first_page_btn.grid(row=2, column=1, padx=20, pady=20)

        prev_page_btn = Button(text="Prev", command=get_prev_page)
        prev_page_btn.grid(row=2, column=2, padx=20, pady=20)

        random_page_btn = Button(text="Random", command=get_random_page)
        random_page_btn.grid(row=2, column=3, padx=20, pady=20)

        next_page_btn = Button(text="Next", command=get_next_page)
        next_page_btn.grid(row=2, column=4, padx=20, pady=20)

        last_page_btn = Button(text="Last page", command=get_last_page)
        last_page_btn.grid(row=2, column=5, padx=20,pady=20)

        window.mainloop()


