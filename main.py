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
        return f"\nStaff member employed for {self.daysWeek} days/Week, completing {self.hoursShift} hours per Day." \
               f"\nThe employee is entitled {self.entitlement} Holidays/Year, from which {self.alTaken} have already been taken."
    def total_holidays(self):
        if self.yearsService <5:
            totalHolidays = (self.daysWeek * self.hoursShift) + self.carriedHours
        else: #Company's policy assumption: if employee has 5 or more years of service, they get 2 extra days of holidays
            totalHolidays = (((self.daysWeek + 2) * self.hoursShift) + self.carriedHours)
        return f'\nTotal Holidays Entitled (inc. Carried Over hours): {totalHolidays} days, totalising {totalHolidays * self.hoursShift} hours.'

class Payroll:
    def __init__(self,contractedHours,annualSal):
        self.contractedHours = contractedHours
        self.annualSal = annualSal

    def __str__(self):
        return '\nThe staff member works {} hours a Week, with an annual salary of £{:,.2f}'.format(self.contractedHours,self.annualSal)

    def hour_rate(self):
        rate = round((self.annualSal/52/self.contractedHours),2)
        if rate > 9.9:
            return f'\nHour Rate: £{rate}.'
        else: #Company's policy assumption: living wage used as minimum salary reference
            return f'\nHour Rate: £9.90.'

    def income_tax (self, taxBand):
        IncomeTaxBand = {'A':0,'B':0.2,'C':0.4,'D':0.5}
        for taxBand in IncomeTaxBand:
            taxPaid = self.annualSal * IncomeTaxBand[taxBand]
            return "\nSalary After Tax: £{:,.2f} /year".format((self.annualSal - taxPaid))


#Layout of the user interface window

#To see all PySimpleGUI themes available: sg.preview_all_look_and_feel_themes()
#Define the theme:
sg.theme('DarkGreen6')
sg.set_options(text_justification='left')

layout = [
    [sg.Text("Welcome to the Employee's Overview Page", font=('Arial',15,'bold'))],
    [sg.Text("To see your payroll and annual leave summary, \nfill in the fields below with the required information.\n")],

    [sg.Frame (layout=[
    [sg.Text("Annual Salary (£): ", size=25),
    sg.Input(size=10, font=('Arial', 10),key='-SALARY-')],
    [sg.Text("Tax Band: ", size=25),
     sg.Spin(values=['A','B','C','D'], size=8, key='-TAX-')],
    [sg.Text("Contracted Hours: ", size=25),
     sg.Input(size=10, font=('Arial', 10),key='-CONTRACTED-')],
    [sg.Text("Years of Service: ", size=25),
     sg.Input(size=10, font=('Arial', 10), key='-YEARS SERVICE-')],
    [sg.Text("Days Worked per Week: ", size=25),
     sg.Spin(values=[i for i in range(1,8)], initial_value=5, size=8, key='-DAYS/WEEK-')],
    [sg.Text("Holidays Taken (Days): ", size=25),
     sg.Input(size=10, font=('Arial', 10), key='-AL TAKEN-')],
    [sg.Text("Holidays Entitlement (Days): ", size=25),
     sg.Input(size=10, font=('Arial', 10), key='-ENTITLE-')],
    [sg.Text("Carried Days from Previous Year: ", size=25),
     sg.Spin(values=[i for i in range(0,11)], initial_value=0, size=8, key='-CARRIED-')]],
    title = "Staff's Info", title_color="black")],

    [sg.Button('Check Summary'),
    sg.Cancel('Exit')]

]

#Parameters for the window (title, etc)

window = sg.Window("Employee's Planner", layout, size=(800,450), element_justification='c')

while True:
    event, values = window.read()

#Setting Variables with User Input:

    annualSalary = float(values['-SALARY-'])
    taxBand = values['-TAX-']
    contractedHours = float(values['-CONTRACTED-'])
    yearsService = int(values['-YEARS SERVICE-'])
    daysperWeek = int(values['-DAYS/WEEK-'])
    holidaysTaken = int(values['-AL TAKEN-'])
    alEntitlement = float(values['-ENTITLE-'])
    alCarried = int(values['-CARRIED-'])
    hoursShift = (contractedHours/daysperWeek)

    holidaysSummary =AnnualLeave(daysperWeek,hoursShift, yearsService, contractedHours,
        alEntitlement, alCarried, holidaysTaken)
    payrollSummary = Payroll(contractedHours,annualSalary)

#Events and interactions:

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Check Summary":
        sg.popup(holidaysSummary, holidaysSummary.total_holidays())
        sg.popup(payrollSummary, payrollSummary.hour_rate(), payrollSummary.income_tax(taxBand))

window.close()