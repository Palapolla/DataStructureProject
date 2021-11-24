import datetime
class Calendar():
    # mm/dd/yy
    
    def __init__(self,date = None):
        self.Calendar = []
        self.year = datetime.datetime.now().strftime("%Y")
        # print(self.year)
        self.month = datetime.datetime.now().strftime("%m")
        self.day = datetime.datetime.now().strftime("%d")

    def one_month_calendar(self,month = None):
        Month31days = ['1','3','5','7','8','10','12']
        if month is None:
            for mon in range(int(self.month),int(self.month)+1,1):
                if mon > 12 :
                    mon = mon -12
                for day in range(1,32,1):
                    if str(mon) not in Month31days and day == 31:
                        break
                    if str(mon) == '2' and ((self.is_LeapYear(int(self.year)) and day == 30) or ((not self.is_LeapYear(int(self.year)) and day == 29))):
                        break
                    self.Calendar.append(datetime.datetime(int(self.year),int(mon),int(day)).strftime("%x"))
                    if str(mon) == '12' and str(day) == '31':
                        self.year = str(int(self.year)+1)
                    # print(self.Calendar)
        else : 
            for mon in range(month,month+1,1):
                if mon > 12 :
                    mon = mon -12
                for day in range(1,32,1):
                    if str(mon) not in Month31days and day == 31:
                        break
                    if str(mon) == '2' and ((self.is_LeapYear(int(self.year)) and day == 30) or ((not self.is_LeapYear(int(self.year)) and day == 29))):
                        break
                    self.Calendar.append(datetime.datetime(int(self.year),int(mon),int(day)).strftime("%x"))
                    if str(mon) == '12' and str(day) == '31':
                        self.year = str(int(self.year)+1)
                    # print(self.Calendar)
        return self

    def is_LeapYear(self,year):
        # Checking if the given year is leap year  366 days
        if((year % 400 == 0) or  
            (year % 100 != 0) and  
            (year % 4 == 0)):   
            return True  
        # Else it is not a leap year  
        else:  
            return False



