import datetime
class Calendar():
    # mm/dd/yy
    
    def __init__(self,date = None):
        self.Calendar = []
        self.year = datetime.datetime.now().strftime("%Y")
        print(self.year)
        self.month = datetime.datetime.now().strftime("%m")
        self.day = datetime.datetime.now().strftime("%d")

    def six_month_calendar(self):
        Month31days = ['1','3','5','7','8','10','12']
        for mon in range(int(self.month),int(self.month)+6,1):
            print('mon',mon)
            if mon > 12 :
                mon = mon -12
            for day in range(1,32,1):
                print('day',day)
                if str(mon) not in Month31days and day == 31:
                    break
                if str(mon) == '2' and ((self.is_LeapYear(int(self.year)) and day == 30) or ((not self.is_LeapYear(int(self.year)) and day == 29))):
                    break
                self.Calendar.append(datetime.datetime(int(self.year),int(mon),int(day)).strftime("%x"))
                if str(mon) == '12' and str(day) == '31':
                    self.year = str(int(self.year)+1)
                # print(self.Calendar)
        return self.Calendar

    def is_LeapYear(self,year):
        # Checking if the given year is leap year  366 days
        if((year % 400 == 0) or  
            (year % 100 != 0) and  
            (year % 4 == 0)):   
            print("Given Year is a leap Year");
            return True  
        # Else it is not a leap year  
        else:  
            print ("Given Year is not a leap Year")  
            return False



