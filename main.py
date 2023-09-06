from tkinter import *
import imdb
from tkinter import messagebox
###################Functinality part

def search():
    if movieEntry.get()=='':
        messagebox.showerror(('Error','Please Type Movie'))
    else:
        root1=Toplevel()


        root1.geometry('890x600+200+50')
        root1.title('Movie info')
        root1.config(bg='purple')

        titleLabel=Label(root1,text='Title : ',font=('gold',30,'bold'),fg='gold',bg='purple')
        titleLabel.place(x=60,y=30)

        titlenameLabel=Label(root1,font=('algerian',20,'bold'),fg='gold',bg='purple')
        titlenameLabel.place(x=300,y=30)

        directorLabel = Label(root1, text='Director : ', font=('gold', 30, 'bold'), fg='gold', bg='purple')
        directorLabel.place(x=60, y=100)

        directornameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='gold', bg='purple')
        directornameLabel.place(x=300, y=100)

        yearLabel = Label(root1, text='Year : ', font=('gold', 30, 'bold'), fg='gold', bg='purple')
        yearLabel.place(x=60, y=170)

        yearnameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='gold', bg='purple')
        yearnameLabel.place(x=300, y=170)

        runtimeLabel = Label(root1, text='RunTime : ', font=('gold', 30, 'bold'), fg='gold', bg='purple')
        runtimeLabel.place(x=60, y=240)

        runtimenameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='gold', bg='purple')
        runtimenameLabel.place(x=300, y=240)

        genreLabel = Label(root1, text='Genres : ', font=('gold', 30, 'bold'), fg='gold', bg='purple')
        genreLabel.place(x=60, y=310)

        genrenameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='gold', bg='purple')
        genrenameLabel.place(x=300, y=310)

        ratingLabel = Label(root1, text='Rating : ', font=('gold', 30, 'bold'), fg='gold', bg='purple')
        ratingLabel.place(x=60, y=380)

        ratingnameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='gold', bg='purple')
        ratingnameLabel.place(x=300, y=380)

        castLabel = Label(root1, text='Cast : ', font=('gold', 30, 'bold'), fg='gold', bg='purple')
        castLabel.place(x=60, y=450)

        castnameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='gold', bg='purple',wraplength=615,justify=LEFT)
        castnameLabel.place(x=300, y=450)

        imdbobject=imdb.IMDb()
        movie_name=movieEntry.get()
        movies=imdbobject.search_movie(movie_name)
        index=movies[0].getID()
        movie=imdbobject.get_movie(index)
        title=movie['title']
        titlenameLabel.config(text=title)

        year = movie['year']
        yearnameLabel.config(text=year)

        rating = movie['rating']
        ratingnameLabel.config(text=rating)

        genre = movie['genre']
        genrenameLabel.config(text=genre)

        for director in movie['director']:
            directornameLabel.config(text=director)

        for runtime in movie['runtime']:
            hours=int(runtime)//60
            minutes=int(runtime)%60
            runtimenameLabel.config(text=f'{hours} hour {minutes} minutes')

        cast = movie['cast']
        castlist = list(map(str, cast))
        slicelist=castlist[:10]
        strr = ''
        for i in slicelist:
            if i == slicelist[9]:
                strr = strr + i + '.'
            else:
                strr = strr + i + ','

        castnameLabel.config(text=strr)

        root1.mainloop()



###################GUI part
root=Tk()

root.geometry('1057x650+100+50')
root.title('Movie Details By Vivek')
root.resizable(False,False)

bgpic=PhotoImage(file='2.png')

bgLabel=Label(root,image=bgpic)
bgLabel.place(x=0,y=0)

movieLabel=Label(root,text='Movie Name:',font=('algerian',30,'bold'),bg='#272D31')
movieLabel.place(x=200,y=570)

movieEntry=Entry(root,font=('FELIX TITLING',20,'bold'),bd=5,relief=GROOVE,justify=CENTER)
movieEntry.place(x=490,y=575)
movieEntry.focus_set()

moviesearchButton=Button(root,text='SEARCH',font=('FELIX TITLING',20,'bold'),bd=5,relief=GROOVE,command=search)
moviesearchButton.place(x=880,y=565)


root.mainloop()
