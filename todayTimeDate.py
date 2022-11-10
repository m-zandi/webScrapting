import time
import datetime
import convertdate
from convertdate import persian
from datetime import timedelta
import calendar

class todayTimeDate:
           
            
            def tTDM(self):
                self.nowDateTime = datetime.datetime.now()    
                nowDate = self.now_date()
                nowTime = self.now_time()
                born = datetime.datetime.strptime(nowDate, '%Y-%m-%d').weekday() 
                weekDay = (calendar.day_name[born]) 
                ########
                wDO = self.weeksDayFuncPersian(weekDay)
                ########
                nowDateAlpha = self.seprateDateAlpha(nowDate)
                nowDateConvertedShamsi = self.dateConvertToShamsi(nowDate)
                nowDateAlphaSh = self.seprateDateShAlpha(nowDateConvertedShamsi)
                # todayOutput = "🗓🕰امروز : {}\n {}                          {}\n{}".format(self.weeksDayFuncPersian(weekDay),nowTime,nowDateAlpha,nowDateAlphaSh)
                todayOutput = "🗓امروز : {}🎋{} \n🕰 {} 🎋 {}".format(wDO,nowDateAlphaSh,nowTime,nowDateAlpha)
                return todayOutput
           #tTDM(self)  success test


            def now_date(self):
                      todayYear = self.nowDateTime.year
                      todayMonth = self.nowDateTime.month
                      todayDay = self.nowDateTime.day       
                      outPut_n_d = str("{}-{}-{}".format(todayYear,todayMonth,todayDay))
                #       print("outPut_n_d = ",outPut_n_d)
                      return outPut_n_d
           #now_date() success test


            
            def now_time(self):
            #today time
                 
                    todayHour = self.nowDateTime.hour
                    todayMinute = self.nowDateTime.minute
                    todaySecond = self.nowDateTime.second
                    #nowTime return
                    outPut_n_t =  str("{}:{}:{}".format(todayHour,todayMinute,todaySecond))
                #     print("outPut_n_t = ",outPut_n_t)
                    return outPut_n_t
            #now_time() success test

            
            def weeksDayFuncPersian(self,wD):
                    switcher = {
                        "Saturday": "شنبه", 
                        "Sunday": "یکشنبه",
                        "Monday": "دوشنبه", 
                        "Tuesday": "سه شنبه", 
                        "Wednesday": "چهارشنبه", 
                        "Thursday": "پنج شنبه", 
                        "Friday": "جمعه"
                        } 
                    outPutWDFP = switcher.get(wD, "nothing") 
                #     print("outPutWDFP = ",outPutWDFP)
                    return outPutWDFP
            #weeksDayFuncPersian(self,wD) success test

            def monthNumToAlpha(self,argument): 
                    self.argument = argument
                    switcher = { 
                        1: "January", 
                        2: "February", 
                        3: "March", 
                        4: "April", 
                        5: "May", 
                        6: "June", 
                        7: "July", 
                        8: "Agust", 
                        9: "September", 
                        10: "October", 
                        11: "November", 
                        12: "December", 
                        } 
                    outPutMNTA = switcher.get(self.argument, "nothing") 
                #     print("outPutMNTA = ",outPutMNTA)    
                    return outPutMNTA
            #monthNumToAlpha() success test

            #convert date to shamsi
            def dateConvertToShamsi(self,fe):
 
                    dateInput =str(fe)
                    a,b,c=map(int, dateInput.split("-"))
                    outPutDCTSh = convertdate.persian.from_gregorian(a,b,c)
                #     print("outPutDCTSh = ",outPutDCTSh)
                    return outPutDCTSh
            #dateConvertToShamsi() success test

            def monthNumToShamAlpha(self,argument): 
                    self.argument = argument
                    switcher = { 
                        1: "فروردین", 
                        2: "اردیبهشت", 
                        3: "خرداد", 
                        4: "تیر", 
                        5: "مرداد", 
                        6: "شهریور", 
                        7: "مهر", 
                        8: "آبان", 
                        9: "آذر", 
                        10: "دی", 
                        11: "بهمن", 
                        12: "اسفند", 
                        } 
                    outPutMNTShA = switcher.get(self.argument, "nothing")  
                #     print("outPutMNTShA =",outPutMNTShA)
                    return outPutMNTShA
           #monthNumToShamAlpha(self,argument) success test

            #Cristian functions
            def seprateDateAlpha(self,argument):
                    
                    argumentStr = str(argument)
                    year, month, day = map(int, argumentStr.split("-"))
                    monthName = self.monthNumToAlpha(month)
                    outPutSD = str("{}-{}-{}".format(day,monthName,year))
                #     print("outPutSD = ",outPutSD)
                    return outPutSD
            #seprateDateAlpha(self,argument) success test

            #  shamsi fuctions
            def seprateDateShAlpha(self,argument):
                    # print(f"argument = {argument}")
                    argumentStr = str(argument)
                    argumentStr = argumentStr.replace("(","")
                    argumentStr = argumentStr.replace(")","")
                    # print(f"argumentStr = {argumentStr}")
                    year, month, day = map(int, argumentStr.split(","))
                    monthName = self.monthNumToShamAlpha(month)
                    outPutSDShA = "{}-{}-{}".format(day,monthName,year)
                #     print("outPutSDSh = ",outPutSDShA)
                    return outPutSDShA
            #seprateDateShAlpha(self,argument) success test