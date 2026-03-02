import datetime

print(datetime)

print(datetime.datetime)

print(datetime.datetime.now())

current_datetime = datetime.datetime.now()

# fdate = datetime.datetime.strptime('2018-03-23', '%Y-%m-%d')
# print(fdate)

print(current_datetime.strftime("%a"))
print(current_datetime.strftime("%A"))
print(current_datetime.strftime("%w"))
print(current_datetime.strftime("%d"))
print(current_datetime.strftime("%b"))
print(current_datetime.strftime("%B"))
print(current_datetime.strftime("%y"))
print(current_datetime.strftime("%Y"))
print(current_datetime.strftime("%m"))
print(current_datetime.strftime("%H"))
print(current_datetime.strftime("%I"))
print(current_datetime.strftime("%M"))
print(current_datetime.strftime("%S"))

print("--------------------------------------")
print(current_datetime.strftime("%d-%b-%Y"))
print(current_datetime.strftime("%I:%M:%S %p"))



"""
Directive	Description	                                    Example	
%a	        Weekday, short version	                        Wed	
%A	        Weekday, full version	                        Wednesday	
%w	        Weekday as a number 0-6, 0 is Sunday	        3	
%d	        Day of month 01-31	                            31	
%b	        Month name, short version	                    Dec	
%B	        Month name, full version	                    December	
%m	        Month as a number 01-12	                        12	
%y	        Year, short version, without century	        18	
%Y	        Year, full version	                            2018	
%H	        Hour 00-23	                                    17	
%I	        Hour 00-12	                                    05	
%p	        AM/PM	                                        PM	
%M	        Minute 00-59	                                41	
%S	        Second 00-59	                                08	
%f	        Microsecond 000000-999999	                    548513	
%j	        Day number of year 001-366	                    365	
%U	        Week number of year, Sunday as the first day of week, 00-53	52	
%W	        Week number of year, Monday as the first day of week, 00-53	52	
%c	        Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	        Century	                                        20	
%x	        Local version of date	                        12/31/18	
%X	        Local version of time	                        17:41:00	
%%	        A % character	                                %	
%G	        ISO 8601 year	                                2018	
%u	        ISO 8601 weekday (1-7)	                        1	
%V	        ISO 8601 weeknumber (01-53)	                    01
"""