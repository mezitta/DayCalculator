
from datetime import date

##################################################
## Calculates the difference in days between
## two dates
##################################################
## Author: Michael Zitta
## Email: mezitta@mtu.edu
## Date Created: 02/11/2021
## Date Last Modified: 02/16/2021
##################################################

class day_count:
   
    def __init__(self, yy1, mm1, dd1, yy2, mm2, dd2 ):
        self.yy1 = yy1
        self.mm1 = mm1
        self.dd1 = dd1
        self.yy2 = yy2
        self.mm2 = mm2
        self.dd2 = dd2
    
    def make_dates(self):
        #Creates start and end date objects 
        date1 = date(self.yy1, self.mm1, self.dd1)
        date2 = date(self.yy2, self.mm2, self.dd2)
        return date1, date2

    def calc_days(self):
        #Calculates the difference in days between the two dates
        day1, day2 = day_count(yy1, mm1, dd1, yy2, mm2, dd2 ).make_dates()
        dif = day2 - day1
        print(f"{dif.days} days")

#Get date inputs from the user
yy1 = int(input("Enter start year(yyyy): "))
mm1 = int(input("Enter start month(mm): "))
dd1 = int(input("Enter start day(dd): "))

yy2 = int(input("Enter end year(yyyy): "))
mm2 = int(input("Enter end month(mm): "))
dd2 = int(input("Enter end day(dd): "))

num_days = day_count(yy1, mm1, dd1, yy2, mm2, dd2)
num_days.calc_days()