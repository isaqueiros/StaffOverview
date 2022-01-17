#Imports:
import PySimpleGUI as sg

#Classes and modules
class AnnualLeave:
    def __init__(self,daysWeek,hoursShift,yearsService,contractedHours, entitlement, carriedHours,alTaken):
        self.daysWeek = daysWeek
        self.hoursShift = hoursShift
        self.yearsService = yearsService
        self.contractedHours = contractedHours
        self.entitlement = entitlement
        self.carriedHours = carriedHours
        self.alTaken = alTaken

    def __str__(self):
        return f"Staff member employed for {self.daysWeek} days per Week, completing {self.hoursShift} hours per Day." \
               f"The employee is entitled {self.entitlement} Holidays per Year, from which {self.alTaken} have already been taken."
    def total_holidays(self):
        if self.yearsService <5:
            return (self.daysWeek * self.hoursShift) + self.carriedHours
        else: #Company's policy assumption: if employee has 5 or more years of servie, they get 2 extra days of holidays
            return ((self.daysWeek + 2) * self.hoursShift) + self.carriedHours

class Payroll:
    def __init__(self,contractedHours,annualSal,taxBand):
        self.contractedHours = contractedHours
        self.annualSal = annualSal
        self.taxBand = taxBand

    def __str__(self):
        return f'The staff member works {self.contractedHours} hours a Week, with an annual salary of £{self.annualSal}'

    def hour_rate(self):
        rate = round((self.annualSal/52/self.contractedHours),2)
        if rate > 9.9:
            return f'£{rate} per hour.'
        else: #Company's policy assumption: living wage used as minimum salary reference
            return 9.9

    def income_tax (self):
        IncomeTaxBand = {'A':0,'B':0.2,'C':0.4,'D':0.5}
        for self.taxBand in IncomeTaxBand:
            return self.annualSal * IncomeTaxBand[self.taxBand]


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

#Events and interactions:

#if event == "Check Summary":

window.close()