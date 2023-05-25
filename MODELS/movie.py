from MODELS.collaborativefiltering import CollaborativeRecommender, preprocessMovies
from tkinter import *
from tkinter import ttk

def movie():
    base = Tk()
    base.geometry("650x500")
    base.title("Movie Recommendation")

    # Movie rating label
    rating_label = Label(base, text="select movie:", font= 'roboto')
    rating_label.grid(row=0, column=0, padx=5, pady=5)

    def on_rating_clicked(value):
        nonlocal rating
        print("Selected rating:", value)
        rating = value

    # Movie rating dropdown
    selected_rating = StringVar(base)
    selected_rating.set("1")
    Label(base, text= "select rating:", font= 'roboto').grid(row=0,column= 1)
    rating_dropdown = ttk.OptionMenu(base, selected_rating, "5", *map(lambda x: str(x), range(1, 6)), command=on_rating_clicked)
    rating_dropdown.grid(row=1, column=1, padx=5, pady=5)

    # Entry field
    e = Entry(base, width=35, borderwidth=8, font='roboto 11' )
    e.grid(row=1, column=0, padx=5, pady=5)

    entry = []
    rating = "5"

    def myEnter(a: Event):
        # Get movie input from the entry field
        movieinput = e.get()
        e.delete(0, END)
        print(movieinput)
        entry.append((movieinput, int(rating)))
        
        # Create a formatted string with star emoji
        entry_text = f"{movieinput} \u2B50{int(rating)}"
        
        # Create a new label for each entry
        myLabel = Label(base, text=entry_text , justify= "left", wraplength= 240,font= 'roboto 11')
        myLabel.grid(sticky= W ,row=2 + len(entry), column=0, padx=5, pady=5)

    def clickGetRecs():
        # Get recommendations based on the entered preferences
        movierecom.putPrefs(entry)
        ops = movierecom.getSimilarToMovies(15).index.to_list()[len(movierecom.prefs)+1:len(movierecom.prefs)+8]
        for _ in range(len(ops)):
            reclabel = Label(base, text=f"{_+1} | {ops[_]}", justify= "left", wraplength=240, font= 'roboto 11')
            reclabel.grid(sticky=W ,row=3 + _ , column=1, padx=5, pady= 5)


    def show_dropdown(val):
        # Create a listbox with movie suggestions
        moviesearch = e.get()
        options = movierecom.find_closest_matches(moviesearch)[:15]
        dropdown = Toplevel(base)
        if options and moviesearch:
            
            dropdown.wm_overrideredirect(True)  # Remove window decorations
            dropdown.wm_geometry(f"+{base.winfo_rootx()}+{base.winfo_rooty()+e.winfo_height()*2}")  # Position below the entry

            # Calculate the width of the dropdown window
            dropdown_width = e.winfo_width() + e.cget("borderwidth") * 2

            # Create a listbox inside the dropdown window
            lb = Listbox(dropdown, width=e.cget("width")+ e.cget("borderwidth")-7, font=e.cget("font"))
            lb.pack()

            for item in options:
                lb.insert(END, item)

            # Set the width of the dropdown window
            dropdown.geometry(f"{dropdown_width}x{lb.winfo_reqheight()}")

            # Handle item selection
            def on_select(event):
                index = lb.curselection()
                if index:
                    selected_item = lb.get(index)
                    e.delete(0, END)
                    e.insert(0, selected_item)
                    dropdown.destroy()

            lb.bind("<<ListboxSelect>>", on_select)
            lb.bind("<Return>", on_select)

            # Close the dropdown window when focus is lost
            dropdown.bind("<FocusOut>", lambda event: dropdown.destroy())
        else:
            # Remove the dropdown window if there are no options
            dropdown.destroy()
            
            
    e.bind('<KeyRelease>', show_dropdown)

    e.bind('<Return>', myEnter)

    butt = ttk.Button(base, text="click to get recommendations".capitalize(), command=clickGetRecs)
    butt.grid(row=2, column=1, padx=5, pady=5)

    # Preprocess the movie and book datasets
    movieratings = preprocessMovies()

    movierecom = CollaborativeRecommender(movieratings, 'userId', 'title', 'rating', 5 , 10)
    
    # movierecom.loadCorrelationMatrix('default-dataset')
    movierecom.getSearchableList()
    base.mainloop()
    movierecom.saveCorrelationMatrix('movie-corrmat')
    
# movie()
