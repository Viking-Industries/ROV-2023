from customtkinter import CTk
from customtkinter import CTkLabel

app = CTk()
app.title("Robot Monitor")
app.minsize(400, 600)

warning1 = False
warning2 = False

lmotor = "N/A"
rmotor = "N/A"
umotor = "N/A"

def update_status():

    if warning1:
        status.configure(text="WARNING! Water Detected")
        status.configure(fg_color="orange")
    elif warning2:
        status.configure(text="DANGER! REMOVE NOW")
        status.configure(fg_color="red")
    else:
        status.configure(text="No Water Detected")
        status.configure(fg_color="green")

    left.configure(text=lmotor)
    right.configure(text=rmotor)
    up.configure(text=umotor)


title = CTkLabel(
                app,
                font=("Terminal",50),
                text="VIK 01 Monitor",
                )

sensortitle = CTkLabel(
                app,
                font=("Terminal",25),
                text="Water Sensor Status:",
                )

status =  CTkLabel(
                app,
                font=("Terminal",25)
                )

#Motor Data
left_title = CTkLabel(
                app,
                font=("Terminal",25),
                text="Left Motor Speed:",
                )
left =  CTkLabel(
                app,
                font=("Terminal",25)
                )

right_title = CTkLabel(
                app,
                font=("Terminal",25),
                text="Right Motor Speed:",
                )

right =  CTkLabel(
                app,
                font=("Terminal",25)
                )

vertical_title = CTkLabel(
                app,
                font=("Terminal",25),
                text="Vertical Motor Speed:",
                )

up =  CTkLabel(
                app,
                font=("Terminal",25)
                )

title.grid(row=0, column=0, pady=5)
sensortitle.grid(row=1, column=0, pady=5)
status.grid(row=1,column=1, pady=5)

left_title.grid(row=2, column=0, pady=5)
left.grid(row=2, column=1, pady=5)

right_title.grid(row=3, column=0, pady=5)
right.grid(row=3, column=1, pady=5)

vertical_title.grid(row=4, column=0, pady=5)
up.grid(row=4, column=1, pady=5)

