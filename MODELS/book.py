from bookfiltering import CollaborativeRecommender, preprocessBooks, preprocessMovies
from tkinter import *
from tkinter import ttk
import tkinter as tk


def mbook():
    #     base = Tk()
    #     base.geometry("500x500")
    #     base.title("Movie Prediction")

    #     e=Entry(base,width=30,borderwidth=8)
    #     e.pack()
    #     e_placeholder=Label(base,text='Enter movie:',fg='grey')
    #     e_placeholder.place(x=55,y=5)
    #     entry = []
    #     rating = ""
    #     def myEnter(a: Event):
    #         movieinput=e.get()
    #         e.delete(0, tk.END)
    #         print(movieinput)
    #         entry.append([movieinput, int(rating)])
    #         print(entry)
    #         myLabel=Label(base,text= str(entry))
    #         myLabel.pack()

    #     def myClick():
    #         # label.config(text= e.get(), font= ('Helvetica 13'))

    #         recommender.putPrefs(entry)
    #         op = recommender.getSimilarToMovies().index
    #         Label( base, text= f"{op}" ).pack()

    #     def on_rating_clicked(value):
    #         nonlocal rating
    #         print("Selected rating:",  value)
    #         rating = value

    #     def on_movie_selected(ex):
    #         print(ex)
    #         e.delete(0, tk.END)

    #         e.insert(0, ex)

    #     def show_dropdown():
    #     # Create a new window for the dropdown
    #         dropdown_window = tk.Toplevel(base)
    #         label.config(text= e.get(), font= ('Helvetica 13'))
    #         moviesearch = e.get()
    #         # print("moviesearch",moviesearch)
    #         # Create a list of options for the dropdown
    #         # options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    #         options = bookrecom.find_closest_matches(moviesearch)
    #         # print(options)
    #         # Create a StringVar to hold the selected option
    #         selected_option = tk.StringVar()

    #         # Set the default selected option
    #         selected_option.set(options[0])

    #         # Create the OptionMenu widget
    #         dropdown = ttk.OptionMenu(dropdown_window, selected_option, *options, command=on_movie_selected)
    #         dropdown.pack()

    # selected_rating = tk.StringVar(base)
    # selected_rating.set("1")
    # rating_dropdown = ttk.OptionMenu(base, selected_rating, "1", "2", "3", "4", "5", command=on_rating_clicked)
    # rating_dropdown.pack()

    # dropbutton = tk.Button(base, text='Show Dropdown', command=show_dropdown)

    # dropbutton.pack()
    # label= Label(base, text="", font=('Helvetica 13'))
    # label.pack()
    # e.bind('<Return>', myEnter)
    # ttk.Button(base, text= "Click to enter preferences", command= myClick).place(relx= .7, rely= .5, anchor= CENTER)

    # # make sure to preprocess the movie and book datasets
    movieratings = preprocessMovies()
    bookratings = preprocessBooks()
    # print(bookratings.head(20))
    # print(movieratings.head(20))
    recommender = CollaborativeRecommender(
        movieratings, 'userId', 'title', 'rating', 5)
    bookrecom = CollaborativeRecommender(
        bookratings, 'User-ID', 'Book-Title', 'Book-Rating', 10)
    recommender.loadCorrelationMatrix()
    # testprefs = [("Shawshank Redemption, The (1994)",5),("Alice in Wonderland (2010)",1),("Aliens (1986)",1),("2001: A Space Odyssey (1968)",2)]
    data1 = input("enter book name: ")
    data2 = int(input("enter rating: "))
    bookprefs = [[data1, data2]]
    bookrecom.putPrefs(bookprefs)
    # recommender.putPrefs(testprefs)
    toitles = bookrecom.getRatingsByUserId().columns.tolist()
    # print(toitles)

    print(bookrecom.getSimilarToMovies())
    # # print(fuzz.ratio("shawshank redemption", "Red"))
    # # save the trained correlation matrix
    # recommender.saveCorrelationMatrix()
    # print(recommender.find_closest_matches("pride and prejudice"))

    # save the trained correlation matrix
    # recommender.saveCorrelationMatrix()
