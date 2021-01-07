import tkinter as tk
from tkinter import messagebox
import datetime 
import yfinance as yf


## function to fetch stock's info using yfinance API call
def fetch():
    stockname = entry.get()
    print(stockname)
    try:  ## in case user enter invalid stock name
    	share = yf.Ticker(stockname)

    	hist  =  share.history()
    	
    	current = hist.tail(1)
    	Date_Time = current.index[0]
    	curr_date = str(Date_Time.year) + "-" + str(Date_Time.month) + "-"+ str(Date_Time.day)
    	open_price = current["Open"].values[0]
    	close_price = current["Close"].values[0]
    	high_price = current["High"].values[0]
    	low_price = current["Low"].values[0]
    	
    except:
    	messagebox.showinfo("Error", "Not a valid stock symbol")
    	return


    stockinfo["text"] = "Date: {}\nOpen: {}\nClose: {}\nHigh: {}\nLow: {}".format(curr_date,open_price,close_price,high_price,low_price)






window = tk.Tk()
window.title("Stock Price Checker")



## grid setting for the layout
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

name_label = tk.Label(master=window, text="Stock Symbol:")
name_label.grid(row=0, column=0)


## User input section
entry = tk.Entry()
entry.grid(row=0, column=1, sticky="nsew")


## search buttom
search = tk.Button(master=window, text="search", command=fetch)
search.grid(row=0, column=2, sticky="nsew")


## output section
stockinfo = tk.Label(master=window, text="",justify = tk.LEFT)
stockinfo.grid(row=1, column=0)



window.mainloop()