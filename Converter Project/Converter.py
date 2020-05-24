from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import urllib.request
import webbrowser

root = Tk()
root.title("CONVERTER APP")
root.geometry("900x520")

def CurrencyConverter():
    ids = {"US Dollar": "USD", "Euros": "EUR", "Indian Rupees": "INR", "Qatar Doha": "QNA",
           "Arab Emirates Dirham": "AED", "Pound Sterling": "GBP", "Japanese Yen": "JPY"}

    def convert(amt, frm, to):
        html = urllib.request.urlopen(
            "http://www.exchangerate-api.com/%s/%s/%f?k=a28d653d2d4fd2727003e437" % (frm, to, amt))
        return html.read().decode('utf-8')

    def callback():
        try:
            amt = float(in_field.get())

        except ValueError:
            out_amt.set('Invalid Input')
            return None

        if in_unit.get == 'Select Unit' or out_unit.get == 'Select Unit':
            out_amt.set("Input or Output not chosen")
            return None

        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Currency Converter")

    frame = tk.Frame(root, bg="#ffca18")
    frame.pack(fill=BOTH, expand=2)

    title = Label(frame, bg="#ffca18", text="Currency Converter", font=("Arial", 12, "bold", "underline"), justify=CENTER)
    title.grid(column=1, row=1, columnspan=4, padx=10, pady=5)

    f = Label(frame, text="From",bg="#ffca18", font=("Arial", 12, "bold"), justify=CENTER)
    f.grid(column=1, row=2,  padx=5, pady=5)

    t = Label(frame, text="To", bg="#ffca18", font=("Arial", 12, "bold"), justify=CENTER)
    t.grid(column=2, row=2, padx=5, pady=5)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = tk.Entry(frame, width=15, textvariable=in_amt)
    in_field.grid( column=1, row=3, padx=10, pady=10)

    in_select = OptionMenu(frame, in_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha",
           "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen")
    in_select["highlightthickness"] = 0
    in_select.grid(column=1, row=4, padx=10, pady=10)

    out_field = tk.Entry(frame, width=15, textvariable=out_amt, state="readonly").grid(column=2, row=3, padx=10, pady=10)
    in_select = OptionMenu(frame, out_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha",
                           "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen")
    in_select["highlightthickness"] = 0
    in_select.grid(column=2, row=4, padx=10, pady=10)

    button = tk.Button(frame,  text="Calculate", command=callback, justify=CENTER).grid(column=1, row=5, columnspan=2, padx=10, pady=10)


def WeightConverter():
    factors = {'ton': 1000000, 'kg': 1000, 'hg': 100, 'dg': 10, 'g': 1, 'deg': 0.1, 'cg': 0.01, 'mg': 0.001,
               'lbs': 0.00220462, 'oz': 0.035274 }
    ids = {"Tonne": 'ton', "Kilogram": 'kg', "Hectagram": 'hg', "Decagram": 'dg', "Decigram": 'deg', "gram": 'g',
           "centigram": 'cg', "milligram": 'mg', "Pounds": 'lbs', "Ounce": 'oz'}

    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())

        except ValueError:
            out_amt.set('Invalid Input')
            return None

        if in_unit.get == 'Select Unit' or out_unit.get == 'Select Unit':
            out_amt.set("Input or Output not chosen")
            return None

        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Weight Converter")

    frame = tk.Frame(root, bg="#ff7f27")
    frame.pack(fill=BOTH, expand=1)

    title = Label(frame, text="Weight Converter", font=("Arial", 12, "bold", "underline"), bg="#ff7f27", justify=CENTER).grid(column=1, row=1, columnspan=4, padx=10, pady=5)

    f = Label(frame, text="From", bg="#ff7f27", font=("Arial", 12, "bold"), justify=CENTER)
    f.grid(column=1, row=2, padx=5, pady=5)

    t = Label(frame, text="To", bg="#ff7f27", font=("Arial", 12, "bold"), justify=CENTER)
    t.grid(column=2, row=2, padx=5, pady=5)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = tk.Entry(frame, width=15, textvariable=in_amt)
    in_field.grid(column=1, row=3, padx=10, pady=10)

    in_select = OptionMenu(frame, in_unit, "Tonne", "Kilogram", "Hectagram", "Decagram", "Decigram", "gram",
           "centigram", "milligram", "Pounds", "Ounce")
    in_select["highlightthickness"] = 0
    in_select.grid(column=1, row=4, padx=10, pady=10)

    out_field = tk.Entry(frame, width=15, textvariable=out_amt, state="readonly").grid(column=2, row=3, padx=10, pady=10)
    in_select = OptionMenu(frame, out_unit, "Tonne", "Kilogram", "Hectagram", "Decagram", "Decigram", "gram",
           "centigram", "milligram", "Pounds", "Ounce")
    in_select["highlightthickness"] = 0
    in_select.grid(column=2, row=4, padx=10, pady=10)

    button = tk.Button(frame,  text="Calculate", command=callback, justify=CENTER).grid(column=1, row=5, columnspan=2, padx=10, pady=10)


def LengthConverter():
    factors = {'nmi': 1852, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1, 'cm': 0.01,
               'mm': 0.001}
    ids = {"Nautical Miles": 'nmi', "Miles": 'mi', "Yards": 'yd', "Feet": 'ft', "Inches": 'inch', "Kilometers": 'km',
           "meters": 'm', "centimeters": 'cm', "millimeters": 'mm'}

    def convert(amt, frm, to):
        if frm != 'm':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())

        except ValueError:
            out_amt.set('Invalid Input')
            return None

        if in_unit.get == 'Select Unit' or out_unit.get == 'Select Unit':
            out_amt.set("Input or Output not chosen")
            return None

        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Length Converter")

    frame = tk.Frame(root, bg="#00a8f3")
    frame.pack(fill=BOTH, expand=1)

    title = Label(frame, bg="#00a8f3", text="Length Converter", font=("Arial", 12, "bold", "underline"), justify=CENTER)
    title.grid(column=1, row=1, columnspan=4, padx=10, pady=5)

    f = Label(frame, text="From",bg="#00a8f3", font=("Arial", 12, "bold"), justify=CENTER)
    f.grid(column=1, row=2,  padx=5, pady=5)

    t = Label(frame, text="To", bg="#00a8f3", font=("Arial", 12, "bold"), justify=CENTER)
    t.grid(column=2, row=2, padx=5, pady=5)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = tk.Entry(frame, width=15, textvariable=in_amt)
    in_field.grid( column=1, row=3, padx=10, pady=10)

    in_select = OptionMenu(frame, in_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers",
                           "meters", "centimeters", "millimeters")
    in_select["highlightthickness"] = 0
    in_select.grid(column=1, row=4, padx=10, pady=10)

    out_field = tk.Entry(frame, width=15, textvariable=out_amt, state="readonly").grid(column=2, row=3, padx=10, pady=10)
    in_select = OptionMenu(frame, out_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers",
                           "meters", "centimeters", "millimeters")
    in_select["highlightthickness"] = 0
    in_select.grid(column=2, row=4, padx=10, pady=10)

    button = tk.Button(frame,  text="Calculate", command=callback, justify=CENTER).grid(column=1, row=5, columnspan=2, padx=10, pady=10)


def AreaConverter():
    wind = Toplevel( bg="#ec1c24")
    wind.minsize(width=300, height=150)
    wind.maxsize(width=400, height=150)

    meterFactor = {'square meter': 1, 'square km': 1000000, 'square rood': 1011.7141056, 'square cm': 0.0001,
                   'square foot': 0.09290304,
                   'square inch': 0.00064516, 'square mile': 2589988.110336, 'millimeter': 0.000001,
                   'square rod': 25.29285264,
                   'square yard': 0.83612736, 'square township': 93239571.9721, 'square acre': 4046.8564224,
                   'square are': 100,
                   'square barn': 1e-28, 'square hectare': 10000, 'square homestead': 647497.027584}

    def convert(x, fromUnit, toUnit):
        if fromVar.get() in meterFactor.keys() and toVar.get() in meterFactor.keys():
            resultxt.delete(0, END)
            result = (float(str(x)) * meterFactor[fromUnit]) / (meterFactor[toUnit])
            resultxt.insert(0, str(result))

    title= Label(wind, text="Area Converter", bg="#ec1c24", font=("Arial", 12, "bold", "underline"), justify=CENTER)
    title.grid(column=1, row=1, columnspan=4, padx=10, pady=5)

    f = Label(wind, text="From",bg="#ec1c24", font=("Arial", 12, "bold"), justify=CENTER)
    f.grid(column=1, row=2,  padx=5, pady=5)

    t = Label(wind, text="To", bg="#ec1c24", font=("Arial", 12, "bold"), justify=CENTER)
    t.grid(column=2, row=2, padx=5, pady=5)

    e = Entry(wind)
    e.grid(column=1, row=3, padx=10, pady=10)
    values = list(meterFactor.keys())

    fromVar = StringVar(wind)
    toVar = StringVar(wind)
    fromVar.set("Select Unit")
    toVar.set("Select Unit")

    fromOption = OptionMenu(wind, fromVar, *values, command=lambda y: convert(e.get(), fromVar.get(), toVar.get()))
    fromOption["highlightthickness"] = 0
    fromOption.grid(column=1, row=4, padx=10, pady=10)

    toOption = OptionMenu(wind, toVar, *values, command=lambda x: convert(e.get(), fromVar.get(), toVar.get()))
    toOption["highlightthickness"] = 0
    toOption.grid(column=2, row=4, padx=10, pady=10)

    resultxt = Entry(wind)
    resultxt.grid(column=2, row=3, padx=10, pady=10)

def TemperatureConverter():

    ids = {"Celsius": "c", "Fahrenheit": "f"}

    def convert(amt, frm, to):
        if frm == to:
            return amt
        elif (frm == 'c') and (to == 'f'):
            return (amt * 9 / 5) + 32
        elif (frm == 'f') and (to == 'c'):
            return (amt - 32) * 5 / 9

    def callback():
        try:
            amt = float(in_field.get())

        except ValueError:
            out_amt.set('Invalid Input')
            return None

        if in_unit.get == 'Select Unit' or out_unit.get == 'Select Unit':
            out_amt.set("Input or Output not chosen")
            return None

        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Temperature Converter")

    frame = tk.Frame(root, bg="#3f48cc")
    frame.pack(fill=BOTH, expand=1)

    title = Label(frame, bg="#3f48cc", text="Temperature Converter", font=("Arial", 12, "bold", "underline"), justify=CENTER)
    title.grid(column=1, row=1, columnspan=4, padx=10, pady=5)

    f = Label(frame, text="From", bg="#3f48cc", font=("Arial", 12, "bold"), justify=CENTER)
    f.grid(column=1, row=2, padx=5, pady=5)

    t = Label(frame, text="To", bg="#3f48cc", font=("Arial", 12, "bold"), justify=CENTER)
    t.grid(column=2, row=2, padx=5, pady=5)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = tk.Entry(frame, width=15, textvariable=in_amt)
    in_field.grid( column=1, row=3, padx=10, pady=10)

    in_select = OptionMenu(frame, in_unit, "Celsius", "Fahrenheit")
    in_select["highlightthickness"] = 0
    in_select.grid(column=1, row=4, padx=10, pady=10)

    out_field = tk.Entry(frame, width=15, textvariable=out_amt, state="readonly").grid(column=2, row=3, padx=10,
                                                                                       pady=10)
    in_select = OptionMenu(frame, out_unit, "Celsius", "Fahrenheit")
    in_select["highlightthickness"] = 0
    in_select.grid(column=2, row=4, padx=10, pady=10)

    button = tk.Button(frame,  text="Calculate", command=callback, justify=CENTER).grid(column=1, row=5, columnspan=2, padx=10, pady=10)


def DigitalStorageConverter():
    factors = {'B': 1, 'KB': 1000, 'MB': 1e+6, 'GB': 1e+9, 'TB': 1e+12, 'PB': 1e+15, 'Bit': 1/8}
    ids = {"Byte": 'B', "Kilobyte": 'KB', "Megabyte": "MB", "Gigabyte": "GB", "Terabyte": 'TB',
           "Petabyte": 'PB', "Bit": 'Bit'}

    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())

        except ValueError:
            out_amt.set('Invalid Input')
            return None

        if in_unit.get == 'Select Unit' or out_unit.get == 'Select Unit':
            out_amt.set("Input or Output not chosen")
            return None

        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Digital Storage Converter")

    frame = tk.Frame(root, bg="#b83dba")
    frame.pack(fill=BOTH, expand=1)

    title = Label(frame, text="Digital Storage Converter", bg="#b83dba", font=("Arial", 12, "bold", "underline"), justify=CENTER)
    title.grid(column=1, row=1, columnspan=4, padx=10, pady=5)

    f = Label(frame, text="From", bg="#b83dba", font=("Arial", 12, "bold"), justify=CENTER)
    f.grid(column=1, row=2, padx=5, pady=5)

    t = Label(frame, text="To", bg="#b83dba", font=("Arial", 12, "bold"), justify=CENTER)
    t.grid(column=2, row=2, padx=5, pady=5)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = tk.Entry(frame, width=15, textvariable=in_amt)
    in_field.grid(column=1, row=3, padx=10, pady=10)

    in_select = OptionMenu(frame, in_unit, "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte",
           "Petabyte", "Bit")
    in_select["highlightthickness"] = 0
    in_select.grid(column=1, row=4, padx=10, pady=10)

    out_field = tk.Entry(frame, width=15, textvariable=out_amt, state="readonly").grid(column=2, row=3, padx=10, pady=10)
    in_select = OptionMenu(frame, out_unit, "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte",
           "Petabyte", "Bit")
    in_select["highlightthickness"] = 0
    in_select.grid(column=2, row=4, padx=10, pady=10)

    button = tk.Button(frame, text="Calculate", command=callback, justify=CENTER).grid(column=1, row=5, columnspan=2,
                                                                                       padx=10, pady=10)


def VolumeConverter():
    factors = {'ml': 1, 'l': 1000, 'g': 4546, 'o': 29, 'ts': 4.929, 'tb': 14.787}
    ids = {"Milliliters": 'ml', "Liters": 'l', "Gallons": 'g', "Fluid Ounces": 'o', "Teaspoon": 'ts', "Tablespoon": 'tb'}

    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())

        except ValueError:
            out_amt.set('Invalid Input')
            return None

        if in_unit.get == 'Select Unit' or out_unit.get == 'Select Unit':
            out_amt.set("Input or Output not chosen")
            return None

        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Volume Converter")

    frame = tk.Frame(root, bg="#05892a")
    frame.pack(fill=BOTH, expand=1)

    title = Label(frame, text="Volume Converter", bg="#05892a", font=("Arial", 12, "bold", "underline"), justify=CENTER)
    title.grid(column=1, row=1, columnspan=4, padx=10, pady=5)

    f = Label(frame, text="From",bg="#05892a", font=("Arial", 12, "bold"), justify=CENTER)
    f.grid(column=1, row=2,  padx=5, pady=5)

    t = Label(frame, text="To", bg="#05892a", font=("Arial", 12, "bold"), justify=CENTER)
    t.grid(column=2, row=2, padx=5, pady=5)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = tk.Entry(frame, width=15, textvariable=in_amt)
    in_field.grid(column=1, row=3, padx=10, pady=10)

    in_select = OptionMenu(frame, in_unit, "Milliliters", "Liters", "Gallons", "Fluid Ounces", "Teaspoon", "Tablespoon")
    in_select["highlightthickness"] = 0
    in_select.grid(column=1, row=4, padx=10, pady=10)

    out_field = tk.Entry(frame, width=15, textvariable=out_amt, state="readonly").grid(column=2, row=3, padx=10, pady=10)
    in_select = OptionMenu(frame, out_unit, "Milliliters", "Liters", "Gallons", "Fluid Ounces", "Teaspoon", "Tablespoon")
    in_select["highlightthickness"] = 0
    in_select.grid(column=2, row=4, padx=10, pady=10)

    button = tk.Button(frame,  text="Calculate", command=callback, justify=CENTER).grid(column=1, row=5, columnspan=2, padx=10, pady=10)

def TimeConverter():
    factors = {'sec': 1, 'min': 60, 'hr': 3600, 'wk': 604800, 'm': 3.8052e-7,
               'y':3.171e-8, 'd': 3.171e-9, 'c': 3.171e-10,
               'ns': 1/1e+9, 'mc': 1/1e+6, 'ml': 1/1e+3}
    ids = {"Seconds": 'sec', "Minutes": 'min', "Hour": 'hr', "Week": 'wk', "Month": 'm', "Year": 'y',
           "Decade": 'd', "Century": 'c', "Milliseconds": "ml", "Microseconds": "mc", "Nanoseconds": 'ns'}

    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())

        except ValueError:
            out_amt.set('Invalid Input')
            return None

        if in_unit.get == 'Select Unit' or out_unit.get == 'Select Unit':
            out_amt.set("Input or Output not chosen")
            return None

        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Time Converter")

    frame = tk.Frame(root, bg="#ffaec8")
    frame.pack(fill=BOTH, expand=1)

    title = Label(frame, text="Time Converter", bg="#ffaec8", font=("Arial", 12, "bold", "underline"), justify=CENTER)
    title.grid(column=1, row=1, columnspan=4, padx=10, pady=5)

    f = Label(frame, text="From",bg="#ffaec8", font=("Arial", 12, "bold"), justify=CENTER)
    f.grid(column=1, row=2,  padx=5, pady=5)

    t = Label(frame, text="To", bg="#ffaec8", font=("Arial", 12, "bold"), justify=CENTER)
    t.grid(column=2, row=2, padx=5, pady=5)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = tk.Entry(frame, width=15, textvariable=in_amt)
    in_field.grid( column=1, row=3, padx=10, pady=10)

    in_select = OptionMenu(frame, in_unit, "Seconds", "Minutes", "Hour", "Week", "Month", "Year",
           "Decade", "Century", "Milliseconds", "Microseconds", "Nanoseconds")
    in_select["highlightthickness"] = 0
    in_select.grid(column=1, row=4, padx=10, pady=10)

    out_field = tk.Entry(frame, width=15, textvariable=out_amt, state="readonly").grid(column=2, row=3, padx=10, pady=10)
    in_select = OptionMenu(frame, out_unit, "Seconds", "Minutes", "Hour", "Week", "Month", "Year",
           "Decade", "Century", "Milliseconds", "Microseconds", "Nanoseconds")
    in_select["highlightthickness"] = 0
    in_select.grid(column=2, row=4, padx=10, pady=10)

    button = tk.Button(frame,  text="Calculate", command=callback, justify=CENTER).grid(column=1, row=5, columnspan=2, padx=10, pady=10)


iarea=ImageTk.PhotoImage(Image.open("area.png"))
area=Button(root, image=iarea, width="200", height="235", bd=1, relief=SOLID, command=AreaConverter)
area.grid(row=0,column=0,padx=10,pady=10)

ivolume=ImageTk.PhotoImage(Image.open("volume.png"))
volume=Button(root, image=ivolume, width="200", height="235", bd=1, relief=SOLID, command=VolumeConverter)
volume.grid(row=0,column=3,padx=10,pady=10)

icurrency=ImageTk.PhotoImage(Image.open("currency.png"))
currency=Button(root, image=icurrency, width="200", height="235", bd=1, relief=SOLID, command=CurrencyConverter)
currency.grid(row=0,column=2,padx=10, pady=10)

iweight=ImageTk.PhotoImage(Image.open("weight.png"))
weight=Button(root, image=iweight, width="200", height="235", bd=1, relief=SOLID, command=WeightConverter)
weight.grid(row=0,column=1,padx=10,pady=10)

itime=ImageTk.PhotoImage(Image.open("time.png"))
time=Button(root, image=itime, width="200", height="235", bd=1, relief=SOLID, command=TimeConverter)
time.grid(row=1,column=3,padx=10,pady=10)

itemp=ImageTk.PhotoImage(Image.open("temperature.png"))
temp=Button(root, image=itemp, width="200", height="235", bd=1, relief=SOLID, command=TemperatureConverter)
temp.grid(row=1,column=1,padx=10,pady=10)

ilength=ImageTk.PhotoImage(Image.open("length.png"))
length=Button(root, image=ilength, width="200", height="235", bd=1, relief=SOLID, command=LengthConverter)
length.grid(row=1,column=0,padx=10,pady=10)

imemory=ImageTk.PhotoImage(Image.open("memory.png"))
memory=Button(root, image=imemory, width="200", height="235", bd=1, relief=SOLID, command=DigitalStorageConverter)
memory.grid(row=1,column=2,padx=10,pady=10)

root.mainloop()