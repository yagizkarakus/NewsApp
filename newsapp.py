import customtkinter
import tkinter
from PIL import Image, ImageTk
import urllib.request
import requests
import io
import webbrowser
import tkcalendar as tkc

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry = ("1920x1080")
root.title("NewsApp")

root.iconbitmap("icon.ico")

tabview = customtkinter.CTkTabview(root)
tabview.pack(pady=20, padx=10, fill="y", expand=False, side=customtkinter.LEFT)

#Search News Method


def searchNews():
    CategoryValue = []
    CountryValue = []
    url = "https://newsapi.org/v2/top-headlines?"
    countrystring = "country="
    categorystring = "category="
    apikey = "Your Api Key"
    for x,y in  enumerate(categoryList):
        if(y.get() == 1):
            CategoryValue.append(category[x].lower())
    for x,y in enumerate(countryList):
        if(y.get() == 1):
            CountryValue.append(countries[x])

    if CountryValue:
        for code in CountryValue:
            countrystring += code+"&"
        url += countrystring

    if CategoryValue:
        for code in CategoryValue:
            categorystring += code+"&"
        url += categorystring

    query = entry.get()
    if len(query) > 0:
        url += "q=" + query +"&"

    entry.delete(0, last_index=len(query))


    url += apikey

    getNews(url)
    
    


#### TOP Headlines TAB
tabview.add("Top-headlines")


entry = customtkinter.CTkEntry(master=tabview.tab("Top-headlines"), placeholder_text="Search News")
entry.pack(padx=20, pady=10, fill="none", expand=True, side=customtkinter.TOP)


#Category

frameCategory = customtkinter.CTkFrame(master=tabview.tab("Top-headlines"))
frameCategory.pack(pady=20, padx=10, fill="y", expand=True, side=customtkinter.TOP)

labelCategory = customtkinter.CTkLabel(master=frameCategory, text="Category")
labelCategory.pack(padx=12, pady=10)

categoryList = [customtkinter.IntVar(), customtkinter.IntVar(), customtkinter.IntVar(), customtkinter.IntVar(), customtkinter.IntVar(), customtkinter.IntVar(), customtkinter.IntVar()]
category = ["Bussiness", "Entertainment", "General", "Health", "Science", "Sports", "Technology"]

for x, y in zip (categoryList, category):
    check1_t1 = customtkinter.CTkCheckBox(master=frameCategory, text=y, variable=x)
    check1_t1.pack(padx=20, pady=10, anchor = customtkinter.W)


#Country

frameCountry = customtkinter.CTkFrame(master=tabview.tab("Top-headlines"))
frameCountry.pack(pady=20, padx=10, fill="y", expand=True, side=customtkinter.TOP)

labelCountry = customtkinter.CTkLabel(master=frameCountry, text="Country")
labelCountry.pack(padx=12, pady=10)

countryList = [customtkinter.IntVar(), customtkinter.IntVar()]
countries =["tr", "us"]

for x, y in zip (countryList, countries):
    check2_t2 = customtkinter.CTkCheckBox(master=frameCountry, text= y, variable=x)
    check2_t2.pack(padx=20, pady=10, anchor = customtkinter.W)


# Search news Button
searchnews = customtkinter.CTkButton(master=tabview.tab("Top-headlines"),width=120,height=32,border_width=0,corner_radius=8,text="Search News",command=searchNews)
searchnews.pack(anchor=tkinter.CENTER, pady=20)


##### EveryThing Tab
tabview.add("Everything")

entry2 = customtkinter.CTkEntry(master=tabview.tab("Everything"), placeholder_text="Search News")
entry2.pack(padx=20, pady=10, fill="none", expand=True, side=customtkinter.TOP)

FromDateLabel = customtkinter.CTkLabel(master=tabview.tab("Everything"), text="FromDate")
FromDateLabel.pack(padx=10, pady=20)

cal = tkc.Calendar(master=tabview.tab("Everything"), selectmode="day", year= 2022, month=2, day= 23, selectforeground= "#2FA572", normalforeground="#000000", weekendforeground="#000000")
cal.config(normalbackground="white")
cal.pack(pady = 20)

ToDateLabel = customtkinter.CTkLabel(master=tabview.tab("Everything"), text="ToDate")
ToDateLabel.pack(padx=10, pady=20)

cal2 = tkc.Calendar(master=tabview.tab("Everything"), selectmode="day", year= 2022, month=2, day= 23, selectforeground= "#2FA572", normalforeground="#000000", weekendforeground="#000000")
cal2.config(normalbackground="white")
cal2 .pack(pady = 20)


combobox = customtkinter.CTkOptionMenu(master=tabview.tab("Everything"), values=["relevancy", "popularity", "publishedAt"])
combobox.pack()







contentframe = customtkinter.CTkScrollableFrame(master=root)
contentframe.pack(pady=20, padx=10, fill="both", expand=True, side=customtkinter.RIGHT)
def create_news(imgurla, titlea, desca, contenta, datea, xa):
    for imgurl, title, desc, content, date, x in zip(imgurla, titlea, desca, contenta, datea, xa):
        cardframe = customtkinter.CTkFrame(master=contentframe, width=1000, height=150)
        cardframe.pack(pady= 5, padx=10, fill="x", expand= False)
        cardframe.wait_visibility()
        try:
            raw_data = urllib.request.urlopen(imgurl).read()  
        except:
            raw_data =urllib.request.urlopen("http://html-color.org/23B274.jpg").read()

        im = Image.open(io.BytesIO(raw_data))
        my_image = customtkinter.CTkImage(dark_image=im ,size=(150, 150))

        checknew = customtkinter.CTkCheckBox(master=cardframe, text="", variable=x)
        checknew.grid(row=2,column=0,padx=20, pady=10,sticky=customtkinter.W)
        checknew.wait_visibility()

        ImageLabel = customtkinter.CTkLabel(master=cardframe, image = my_image, text="")
        ImageLabel.grid(row = 0, column = 1,columnspan = 4, rowspan = 4, padx = 0, pady = 0, sticky=customtkinter.W)
        ImageLabel.wait_visibility()

        TitleLabel = customtkinter.CTkLabel(master=cardframe,text=title, font=("Times New Roman",20,"bold"), fg_color="transparent", text_color= "#2FA572")
        TitleLabel.grid(row = 0, column=7,columnspan =3, rowspan=1,  padx = 10, pady = 0, sticky= customtkinter.W)   
        TitleLabel.wait_visibility()

        DescLabel = customtkinter.CTkLabel(master=cardframe,text=desc, font=("Times New Roman",18), fg_color="transparent")
        DescLabel.grid(row = 1, column=7,columnspan =3, rowspan=1, padx = 10, pady = 0, sticky= customtkinter.W )
        DescLabel.wait_visibility()

        ContetnLabel = customtkinter.CTkLabel(master=cardframe,
                                            text=content, 
                                            font=("Times New Roman",12), 
                                            fg_color="transparent",
                                            justify = customtkinter.LEFT)
        ContetnLabel.grid(row = 2, column=7,columnspan =3, rowspan=1, padx = 30, pady = 0, sticky= customtkinter.W )   
        ContetnLabel.wait_visibility()

        DateLabel = customtkinter.CTkLabel(master=cardframe,text=date, font=("Times New Roman",18), fg_color="transparent")
        DateLabel.grid(row = 3, column=10, padx = 0, pady = 0, sticky= customtkinter.W )   
        DateLabel.wait_visibility()

Selected_news = []
All_News =[]
def getNews(url):
    for widget in contentframe.winfo_children():
        widget.destroy()

    news = requests.get(url).json()
    articles = news["articles"]

    Selected_news.clear()
    All_News.clear()

    images = []
    titles = []
    description = []
    content = []
    date = []
    

    for i,article in enumerate(articles):
        y = f"{article['url']}"
        All_News.append(y)

        x = customtkinter.IntVar()
        Selected_news.append(x)
          
        images.append(f"{article['urlToImage']}")
        titles.append(article["title"]) 
        description.append(" ".join(article["description"].split()) if article["description"] is not None else "no description") 
        content.append(" ".join(article["content"].split()) if article["content"] is not None else "no content") 
        date.append (article["publishedAt"]) 

    create_news(images, titles, description, content, date, Selected_news)                

def openNews():
    news =[]

    if Selected_news and All_News:
            for x,y in  enumerate(Selected_news):
                if (y.get() == 1):
                    news.append(All_News[x])

            for url in news:
                webbrowser.open(url, new=len(news))

def openaNews():
        if Selected_news and All_News:
            for url in  (All_News):
                    webbrowser.open(url, new=len(All_News))
                

open = customtkinter.CTkButton(master=root,width=120,height=32,border_width=0,corner_radius=8,text="Open Selected News",command=openNews, )
open.pack(pady=20, padx=10, side=customtkinter.BOTTOM)    

openAllNews = customtkinter.CTkButton(master=root,width=120,height=32,border_width=0,corner_radius=8,text="Open All News",command=openaNews, )
openAllNews.pack(pady=20, padx=10, side=customtkinter.BOTTOM)    

root.mainloop()