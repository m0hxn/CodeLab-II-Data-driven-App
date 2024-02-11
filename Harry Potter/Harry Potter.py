import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import io
import random
import time



def fetch_potions():
    response = requests.get('https://api.potterdb.com/v1/potions')
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def fetch_characters():
    response = requests.get('https://api.potterdb.com/v1/characters')
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def fetch_books():
    response = requests.get('https://api.potterdb.com/v1/books')
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def fetch_spells():
    response = requests.get('https://api.potterdb.com/v1/spells')
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []
    
def fetch_movies():
    response = requests.get('https://api.potterdb.com/v1/movies')
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []
    
def fetch_and_display_image(image_url, image_label):
    if image_url:
        try:
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_data = Image.open(io.BytesIO(image_response.content))
                image_data.thumbnail((200, 200), Image.Resampling.LANCZOS)
                image = ImageTk.PhotoImage(image_data)
                image_label.config(image=image, bg="lightblue")
                image_label.image = image 
        except Exception as e:
            print(f"An error occurred: {e}")
            image_label.config(image='', text='Image not available')
    else:
        image_label.config(image='', text='No image URL provided')    

def display_potion(potion, image_label, details_label):
    potion_attributes = potion['attributes']
    potion_details = f"Name: {potion_attributes['name']}\n" \
                     f"Ingredients: {potion_attributes['ingredients']}\n" \
                     f"Slug Name: {potion_attributes['slug']}\n" \
                     f"Characteristics: {potion_attributes['characteristics']}\n" \
                     f"Effects: {potion_attributes['effect']}"

    details_label.config(text=potion_details)
    image_url = potion_attributes.get('image')
    fetch_and_display_image(image_url, image_label)
                     
def fetch_random_potion(image_label, details_label):
    potions = fetch_potions()
    if potions:
        random_potion = random.choice(potions)
        display_potion(random_potion, image_label, details_label)

        
def display_character(character, image_label, details_label):
    character_attributes = character['attributes']
    character_details = f"Name: {character_attributes.get('name', 'N/A')}\n" \
                        f"House: {character_attributes.get('house', 'N/A')}\n" \
                        f"Role: {character_attributes.get('role', 'N/A')}\n" \
                        f"Blood Status: {character_attributes.get('bloodStatus', 'N/A')}"

    details_label.config(text=character_details)
    image_url = character_attributes.get('image')
    fetch_and_display_image(image_url, image_label)        

def fetch_random_character(image_label, details_label):
    characters = fetch_characters()
    if characters:
        random_character = random.choice(characters)
        display_character(random_character, image_label, details_label)
        
def display_book(book, image_label, details_label):
    book_attributes = book['attributes']
    book_details = f"Title: {book_attributes.get('title', 'Unknown Title')}\n" \
                   f"ISBN: {book_attributes.get('isbn13', 'N/A')}\n" \
                   f"Number of Pages: {book_attributes.get('numberOfPages', 'N/A')}\n" \
                   f"Description: {book_attributes.get('description', 'No description available.')}"

    details_label.config(text=book_details)
    image_url = book_attributes.get('cover')
    
    fetch_and_display_image(image_url, image_label)

def fetch_random_book(image_label, details_label):
    books = fetch_books()
    if books:
        random_book = random.choice(books)
        display_book(random_book, image_label, details_label)

def display_spell(spell,  image_label, details_label):
    spell_attributes = spell['attributes']
    spell_details = f"Name: {spell_attributes['name']}\n" \
                    f"Type: {spell_attributes.get('type', 'N/A')}\n" \
                    f"Effect: {spell_attributes.get('effect', 'N/A')}"

    details_label.config(text=spell_details)
    image_url = spell_attributes.get('image')
    fetch_and_display_image(image_url, image_label)

def fetch_random_spell( image_label, details_label):
    spells = fetch_spells()
    if spells:
        random_spell = random.choice(spells)
        display_spell(random_spell, image_label, details_label)
        
def display_movie(movie, image_label, details_label):
    movie_attributes = movie['attributes']
    movie_details = f"Title: {movie_attributes.get('title', 'N/A')}\n" \
                    f"Year: {movie_attributes.get('year', 'N/A')}\n" \
                    f"Director: {movie_attributes.get('director', 'N/A')}\n"

    details_label.config(text=movie_details)
    image_url = movie_attributes.get('poster')
    fetch_and_display_image(image_url, image_label)

def fetch_random_movie(image_label, details_label):
    movies = fetch_movies()
    if movies:
        random_movie = random.choice(movies)
        display_movie(random_movie, image_label, details_label)

def create_main_app(root):
    root.title("Harry Potter Random Information Generator")
    
    root.configure(bg="black")  

    details_frame = tk.Frame(root, borderwidth=2, relief="groove",bg="#cc9966")
    details_frame.pack(pady=20, padx=20, fill="both", expand=True)

    image_label = tk.Label(details_frame,bg="#cc9966")
    image_label.grid(row=0, column=0, padx=10, pady=10)

    details_label = tk.Label(details_frame, text="", justify=tk.LEFT, anchor="w",)
    details_label.grid(row=0, column=1, sticky="nsew")

    button_style = {"bg": "#6d553e", "fg": "white", "font": ("Arial", 12), "cursor": "hand2"}

    potion_button = tk.Button(root, text="Generate Random Potion", command=lambda: fetch_random_potion(image_label, details_label), **button_style)
    potion_button.pack(side=tk.LEFT, padx=10, pady=20)

    character_button = tk.Button(root, text="Generate Random Character", command=lambda: fetch_random_character(image_label, details_label), **button_style)
    character_button.pack(side=tk.RIGHT, padx=10, pady=20)

    spell_button = tk.Button(root, text="Generate Random Spell", command=lambda: fetch_random_spell(image_label, details_label), **button_style)
    spell_button.pack(side=tk.TOP, padx=10, pady=20)

    book_button = tk.Button(root, text="Generate Random Book", command=lambda: fetch_random_book(image_label, details_label), **button_style)
    book_button.pack(side=tk.BOTTOM, padx=10, pady=20)

    movie_button = tk.Button(root, text="Generate Random Movie", command=lambda: fetch_random_movie(image_label, details_label), **button_style)
    movie_button.pack(side=tk.BOTTOM, padx=10, pady=20)
    
def create_sparkle(canvas):
    distance_factor = 1.9 

    x = random.randint(0, canvas.winfo_width())
    y = random.randint(0, canvas.winfo_height())
    size = random.randint(2, 5)
    
    x += size * distance_factor
    y += size * distance_factor

    color = random.choice(['#ffffcc', '#ffcc99', '#ffccff'])  

    sparkle = canvas.create_oval(x, y, x + size, y + size, fill=color, outline='')

    return sparkle

def magical_sparkles(canvas):
    for _ in range(15):  
        create_sparkle(canvas)

    canvas.after(1000, lambda: clear_sparkles(canvas))
    canvas.after(1500, lambda: magical_sparkles(canvas))

def clear_sparkles(canvas):
    for sparkle in canvas.find_all():
        canvas.delete(sparkle)
        
def fade_in(label):
    for i in range(6):  
        label.configure(bg=f'#{int(255 * i/5):02x}{int(255 * i/5):02x}{int(255 * i/5):02x}')
        label.update()
        time.sleep(0.1)  

def fade_out(label):
    for i in range(5, -1, -1):  
        label.configure(bg=f'#{int(255 * i/5):02x}{int(255 * i/5):02x}{int(255 * i/5):02x}')
        label.update()
        time.sleep(0.1)


        

def create_welcome_window():
    welcome_root = tk.Tk()
    welcome_root.title("Welcome to Harry Potter App")

    welcome_root.configure(bg="black")  

    welcome_root.geometry("600x700")
    
    welcome_root.configure(bg="black")

    welcome_label = tk.Label(welcome_root, text="Welcome to Harry Potter! ", font=("Arial", 24), fg="white", bg="black")
    welcome_label.pack(padx=20, pady=50)

    fade_in(welcome_label)
    time.sleep(0.3)  
    fade_out(welcome_label)

    canvas = tk.Canvas(welcome_root, width=600, height=450, bg="black", highlightthickness=0)
    canvas.pack(pady=20)

    magical_sparkles(canvas)

    def on_enter(event):
        start_button.config(bg='#8c6d4f', fg='white') 

    def on_leave(event):
        start_button.config(bg='#6d553e', fg='white') 

    start_button = tk.Button(welcome_root, text="Start App", command=lambda: open_main_app(welcome_root), bg='#6d553e', fg='white', font=("Arial", 18), cursor="hand2")
    start_button.pack(pady=2)

    start_button.bind("<Enter>", on_enter)
    start_button.bind("<Leave>", on_leave)

    welcome_root.mainloop()


def open_main_app(welcome_root):
    welcome_root.destroy()
    main_root = tk.Tk()
    create_main_app(main_root)
    main_root.mainloop()

def main():
    create_welcome_window()

if __name__ == "__main__":
    main()