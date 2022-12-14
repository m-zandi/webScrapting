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
                # todayOutput = "šš°Ų§ŁŲ±ŁŲ² : {}\n {}                          {}\n{}".format(self.weeksDayFuncPersian(weekDay),nowTime,nowDateAlpha,nowDateAlphaSh)
                todayOutput = "šŲ§ŁŲ±ŁŲ² : {}š{} \nš° {} š {}".format(wDO,nowDateAlphaSh,nowTime,nowDateAlpha)
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
                        "Saturday": "Ų“ŁŲØŁ", 
                        "Sunday": "ŪŚ©Ų“ŁŲØŁ",
                        "Monday": "ŲÆŁŲ“ŁŲØŁ", 
                        "Tuesday": "Ų³Ł Ų“ŁŲØŁ", 
                        "Wednesday": "ŚŁŲ§Ų±Ų“ŁŲØŁ", 
                        "Thursday": "Ł¾ŁŲ¬ Ų“ŁŲØŁ", 
                        "Friday": "Ų¬ŁŲ¹Ł"
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
                        1: "ŁŲ±ŁŲ±ŲÆŪŁ", 
                        2: "Ų§Ų±ŲÆŪŲØŁŲ“ŲŖ", 
                        3: "Ų®Ų±ŲÆŲ§ŲÆ", 
                        4: "ŲŖŪŲ±", 
                        5: "ŁŲ±ŲÆŲ§ŲÆ", 
                        6: "Ų“ŁŲ±ŪŁŲ±", 
                        7: "ŁŁŲ±", 
                        8: "Ų¢ŲØŲ§Ł", 
                        9: "Ų¢Ų°Ų±", 
                        10: "ŲÆŪ", 
                        11: "ŲØŁŁŁ", 
                        12: "Ų§Ų³ŁŁŲÆ", 
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