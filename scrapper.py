import tkinter as tk

## function to fetch stock's info using API call
def fetch():
    value = entry.get()
    stockinfo["text"] = value


window = tk.Tk()


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
stockinfo = tk.Label(master=window, text="")
stockinfo.grid(row=1, column=0)



window.mainloop()