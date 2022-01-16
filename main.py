#Imports:
import PySimpleGUI as sg

#Layout of the user interface window

#To see all PySimpleGUI themes available: sg.preview_all_look_and_feel_themes()
#Define the theme:
sg.theme('DarkGreen6')
sg.set_options(text_justification='left')

layout = [
    [sg.Text("Welcome to the Employee's Overview Page", font=('Arial',15,'bold'))],
    [sg.Text("To see your payroll and annual leave summary, \nfill in the fields below with the required information.\n")],
    #[]

    [sg.Text("Annual Salary (£): ", size=25),
    sg.Input(size=10, font=('Arial', 10))],
    [sg.Text("Tax Band: ", size=25),
     sg.Spin(values=['A','B','C','D'], size=8)],
    #sg.Input(size=10, font=('Arial', 10))],
    [sg.Text("Contracted Hours: ", size=25),
     sg.Input(size=10, font=('Arial', 10))],
    [sg.Text("Days Worked per Week: ", size=25),
     sg.Spin(values=[i for i in range(1,8)], initial_value=5, size=8)],
    [sg.Text("Holidays Entitlement (Days): ", size=25),
     sg.Input(size=10, font=('Arial', 10))],
    [sg.Text("Carried Days from Previous Year: ", size=25),
     sg.Spin(values=[i for i in range(0,11)], initial_value=0, size=8)],

    [sg.Button('Check Summary'),
    sg.Cancel('Exit')]

]

#Parameters for the window (title, etc)

window = sg.Window("Employee's Planner", layout, size=(800,450), element_justification='c')

event, values = window.read()

#if event == "Check Summary":

window.close()