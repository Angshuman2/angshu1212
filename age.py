#imported tkinter
from tkinter import *
#font class imported from tkinter
from tkinter.font import Font
#imported combobox from tkinter (ttk) class
from tkinter.ttk import Combobox
#imported message box
import tkinter.messagebox as tmsg
#import time
import time
#root 
root=Tk()
#title
root.title("Age Detector.")
#font style that use later
font=Font(family="Times",size=10,weight="bold",underline=1,slant="italic")
font1=Font(family="Times",size=15,weight="bold",underline=1,slant="italic")
font3=Font(family="Times",size=12,weight="bold",underline=1,slant="italic")
font2=Font(family="Helvetica",size=14,weight="bold",underline=1,slant="italic")
#counter the first frame where age will show 
frame_number=0
#counter the second frame where age will show
frame_number2=0
#counter the compare button
compareCounter=0
#counter to show compare button 
a=0
#used to compare the two different times
#year month day changes the value of the below list
compareYYlist=[0,0]
compareMMlist=[0,0]
compareDDlist=[0,0]
#function of geting age
def getAge():
    #try to give the age
    try:
        #get the name value
        name_entry_get=name_entry.get()
        #local time from main root widget
        global timee
        #present month value as number
        present_month=timee.tm_mon
        #value of present day
        present_day=timee.tm_mday
        global list_month
        global list_monthDay
        global last_year
        global frame_number
        global frame_number2
        global compareCounter
        global a
        #get value from combobox widget
        #day value
        dayGet=day_combobox.get()
        #month value
        monthGet=month_combobox.get()
        #year value
        yearGet=year_combobox.get()
        #take month1 var 
        #it increase as the month got subtract from total value of day
        month1=0
        global compareYYlist
        global compareMMlist
        global compareDDlist
        #compare function
        def comp():
            #compare month that increase as the total day subtracted
            compare_Month=0
            global compareYYlist
            global compareMMlist
            global compareDDlist
            #to get the current day
            #from the started month
            comD=0
            global list_monthDay1
            global list_month1
            #takes var 
            #changes the var name from first
            compareYlist=compareYYlist
            compareMlist=compareMMlist
            compareDlist=compareDDlist
            #keep the first number small every time
            #it helps to know the compare time
            if int(compareYlist[0])>int(compareYlist[1]):
                compareYlist=compareYlist[::-1]
                compareMlist=compareMlist[::-1]
                compareDlist=compareDlist[::-1]
            elif int(compareYlist[0])==int(compareYlist[1]) and list_month1.index(compareMlist[0])>list_month1.index(compareMlist[1]):
                compareYlist=compareYlist[:]
                compareMlist=compareMlist[::-1]
                compareDlist=compareDlist[::-1]
            elif int(compareYlist[0])==int(compareYlist[1]) and list_month1.index(compareMlist[0])==list_month1.index(compareMlist[1]) and int(compareDlist[0])>int(compareDlist[1]):
                compareYlist=compareYlist[:]
                compareMlist=compareMlist[:]
                compareDlist=compareDlist[::-1]
            else:
                compareYlist=compareYlist[:]
                compareMlist=compareMlist[:]
                compareDlist=compareDlist[:]
            #if both dates are same 
            if compareYlist[0]==compareYlist[1] and compareMlist[0]==compareMlist[1] and compareDlist[0]==compareDlist[1]:
                tmsg.showinfo("DIFFERENCE..","Same Year...\nNo Differences...")
            #if both days are not same 
            else:
                #compare middle year
                comY=int(compareYlist[1])-((int(compareYlist[0])+1))
                #to get starting month day
                #if february
                if compareMlist[0]=="February":
                    #if leap year
                    if int(compareYlist[0])%4==0:
                        comD=29-int(compareDlist[0])
                    #if not leap year
                    else:
                        comD=28-int(compareDlist[0])
                #if month is april june september november
                elif compareMlist[0]=="April" or compareMlist[0]=="June" or compareMlist[0]=="September" or compareMlist[0]=="November":
                    comD=30-int(compareDlist[0])
                #if month are 31 days
                else:
                    comD=31-int(compareDlist[0])
                #for first year
                #change february day if leap year or not
                if int(compareYlist[0])%4==0:
                    list_monthDay1[1]=29
                else:
                    list_monthDay1[1]=28
                #total day of first year
                comFM=sum(list_monthDay1[(list_month1.index(compareMlist[0])+1):13])+(list_monthDay1[list_month1.index(compareMlist[0])]-int(compareDlist[0]))
                #for last year
                #change february day if leap year or not
                if int(compareYlist[1])%4==0:
                    list_monthDay1[1]=29
                else:
                    list_monthDay1[1]=28
                #total day of last year
                comLM=sum(list_monthDay1[0:list_month1.index(compareMlist[1])])+int(compareDlist[1])
                #to check and change february day as leap year or not (for first year)
                if int(compareYlist[0])%4==0:
                    list_monthDay1[1]=29
                else:
                    list_monthDay1[1]=28
                #subtract started date
                for i3 in list_monthDay1[((list_month1.index(compareMlist[0]))+1):]:
                    comFM-=i3
                    compare_Month+=1
                #subtract last date
                for i4 in list_monthDay1[:(list_month1.index(compareMlist[1]))]:
                    comLM-=i4
                    compare_Month+=1
                #total of remaining day
                comT=comFM+comLM
                #compare with started month's day
                if comT>=list_monthDay1[list_month1.index(compareMlist[0])]:
                    comT-=list_monthDay1[list_month1.index(compareMlist[0])]
                    compare_Month+=1
                if compare_Month>=12:
                    #subtract if greater and add 1 year with total year
                    compare_Month=compare_Month-12
                    comY+=1
                #show difference on message box
                tmsg.showinfo("DIFFERENCE...","Difference= "+str(comY)+" Year. "+str(compare_Month)+" Month. "+str(comT)+" Day.")
            pass
        #first remove function
        def finish1():
            #take some global var
            global a
            global frame_number
            global compareCounter
            #incement of a 
            #it is used to stop compare button to show in some way
            a+=1
            #to destroy and regenerate first day option
            frame_number=0
            #destroy frame
            frame5.destroy()
            crossF.destroy()
            #decrease compare counter if following var is true
            if a%2==0 and compareCounter==1:
                compareCounter-=1
            #try to destroy compare button frame 
            try:
                frame7.destroy()
                compareCounter-=1
            #if any exception pass
            except Exception as e:
                pass
        #second remove function
        def finish2():
            #global var
            global frame_number2
            global compareCounter
            #frame number 2 will be 0 to use it again
            frame_number2=0
            frame6.destroy()
            crossF2.destroy()
            #try
            try:
                frame7.destroy()
                compareCounter-=1
            #except pass
            except Exception as e:
                pass
        #if two output of age 
        #show error in message box
        if frame_number>=1 and frame_number2>=1:
            tmsg.showerror("ERROR..","Sorry,.. Maximum Widget..\nRemove One....")
        #else enter
        else:
            #if no name error
            if name_entry_get=="":
                tmsg.showerror("ERROR","DID NOT GET ANY NAME")
            #if no information means day not mention error message on message box
            elif dayGet=="" or monthGet=="" or yearGet=="":
                tmsg.showerror("ERROR","WE DID NOT GET ALL INFORMATION")
            #else enter
            else:
                #var to use all months in there adject day
                #else it will show an error message
                #get this day var in integer 
                errorShown=int(dayGet)
                #error month list
                errorM=["April","June","September","November"]
                #error on 30 day months if choose any extra
                if monthGet in errorM and errorShown>=31:
                    tmsg.showerror("ERROR...","Sorry...\n{} has only 30 days".format(monthGet))
                #error on february on leap year
                elif monthGet=="February" and int(yearGet)%4==0 and errorShown>=30:
                    tmsg.showerror("ERROR...","Sorry...\n{c}  It's a Leap Year..\n{a} doesn't have {b} days".format(a=monthGet,b=dayGet,c=yearGet))
                #error on february without leap year
                elif monthGet=="February" and int(yearGet)%4!=0 and errorShown>=29:
                    tmsg.showerror("ERROR...","Sorry...\n{c}  Not a Leap Year...\n{a} doesn't have {b} days".format(a=monthGet,b=dayGet,c=yearGet))
                #else enter
                else:
                    #count day of starting month through age day var
                    if monthGet=="February":
                        if int(yearGet)%4==0:
                            age_day=29-int(dayGet)
                        else:
                            age_day=28-int(dayGet)
                    elif monthGet=="April" or monthGet=="June" or monthGet=="September" or monthGet=="November":
                        age_day=30-int(dayGet)
                    else:
                        age_day=31-int(dayGet)
                    #reverse the month name for first year
                    reverseMonth=list_month[::-1]
                    #reverse the month day for last year
                    reverse_monthDay=list_monthDay[::-1]
                    #get february month day by checking leap year
                    if last_year%4==0:
                        list_monthDay[1]=29
                    else:
                        list_monthDay[1]=28
                    #get february month day by checking leap year in reverse month day
                    if int(yearGet)%4==0:
                        reverse_monthDay[10]=29
                    else:
                        reverse_monthDay[10]=28
                    #last year monyh list
                    list_present=list(list_monthDay[0:(present_month-1)])
                    #first year monyh list
                    list_selected=list(reverse_monthDay[0:(reverseMonth.index(monthGet))])
                    #sum of all day from last year
                    sum_presentDay=sum(list_present)+present_day
                    ##check for the greater one
                    just=[]
                    for i in range(last_year+1):
                        if i%4==0:
                            just.append(366)
                        else:
                            just.append(365)
                    just1=sum(just)
                    just3=[]
                    for ii in range(int(yearGet)+1):
                        if ii%4==0:
                            just3.append(366)
                        else:
                            just3.append(365)
                    just4=sum(just3)
                    #for greater year that selected
                    correctDate=sum_presentDay+just1
                    greaterDate=sum(list_monthDay[:list_month.index(monthGet)])+int(dayGet)+just4
                    #sum of all day from first year
                    sum_selectedDay=sum(list_selected)+age_day
                    #middle year
                    TotYear=last_year-(int(yearGet)+1)
                    if int(yearGet)%4==0:
                        list_monthDay[1]=29
                    else:
                        list_monthDay[1]=28
                    #subtract total day according to month
                    #first month
                    for i in reverse_monthDay[:reverseMonth.index(monthGet)]:
                        sum_selectedDay-=i
                        #increment month
                        month1+=1
                    #subtract total day according to month
                    #second month
                    for i2 in list_monthDay[:(present_month-1)]:
                        sum_presentDay-=i2
                        month1+=1
                    ToTaL=sum_presentDay+sum_selectedDay
                    if ToTaL>=list_monthDay[list_month.index(monthGet)]:
                        ToTaL-=list_monthDay[list_month.index(monthGet)]
                        month1+=1
                    #if month number greater than 12 increase a year
                    if month1>=12:
                        month1=month1-12
                        TotYear+=1
                    #if selected greater year then present date
                    if correctDate<greaterDate:
                        tmsg.showerror("ERROR....","You are selected a greater date\nthen the present date...")
                    else:
                        #to show first output
                        if frame_number==0:
                            #set empty string
                            name_var.set("")
                            day_combobox.set("")
                            month_combobox.set("")
                            year_combobox.set("")
                            name_entry.focus()
                            #use it for compare
                            #change the value of the following list
                            compareYYlist[0]=yearGet
                            compareMMlist[0]=monthGet
                            compareDDlist[0]=dayGet
                            #frame number is 1 
                            #so it can not use again without remove
                            frame_number=1
                            #increment compare counter to show compare button
                            compareCounter+=1
                            #increment a
                            a+=1
                            #output frame
                            global frame7
                            frame5=Frame(root,bg="light green")
                            frame5.pack(side="top",fill="x",pady=3)
                            crossF=Frame(frame5,bg="light green")
                            crossF.pack(side="right",padx=2)
                            name_show=Label(frame5,text="Name..  =   "+name_entry_get.title(),font=font3,bg="light green",fg="maroon")
                            name_show.pack(side="top",padx=3,anchor="w") 
                            detail_show=Label(frame5,text="Age..  = "+str(TotYear)+" Year.  "+str(month1)+" Month.  "+str(ToTaL)+" Day.",bg="light green",fg="black",font="Helvetica 10 bold")
                            detail_show.pack(side="top",padx=3,anchor="w")
                            selectedShowD=Label(frame5,text="DOB...  = "+dayGet+" / "+monthGet+" / "+yearGet,bg="light green",fg="black",font="Helvetica 10 bold")
                            selectedShowD.pack(side="top",padx=3,anchor="w")
                            cross=Button(crossF,text="REMOVE",fg="red",bg="black",height=1,width=7,command=finish1,font="Times 8 bold")
                            cross.pack(side="top",anchor="e")
                            #if two output day show compare button
                            if compareCounter==2:
                                frame7=Frame(root,bg="pink")
                                frame7.pack(side="bottom",fill="x",pady=5)
                                compareBottom=Button(frame7,text="Compare...",fg="white",bg="black",font="Times 10 italic bold",height=1,bd=3,relief="sunken",width=8,command=comp)
                                compareBottom.pack(side="right",padx=6)
                        #to show second frame of output
                        elif frame_number2==0:
                            #set empty string
                            name_var.set("")
                            day_combobox.set("")
                            month_combobox.set("")
                            year_combobox.set("")
                            name_entry.focus()
                            #change the second element fromk following list
                            compareYYlist[1]=yearGet
                            compareMMlist[1]=monthGet
                            compareDDlist[1]=dayGet
                            #set a is 0
                            a=0
                            #stop to show another out put
                            frame_number2=1
                            #for compare button
                            compareCounter+=1
                            #frames for out put
                            frame6=Frame(root,bg="yellow")
                            frame6.pack(side="top",fill="x",pady=3)
                            crossF2=Frame(frame6,bg="yellow")
                            crossF2.pack(side="right",padx=2)
                            name_show=Label(frame6,text="Name..  =   "+name_entry_get.title(),font=font3,bg="yellow",fg="maroon")
                            name_show.pack(side="top",padx=3,anchor="w") 
                            detail_show=Label(frame6,text="Age..  = "+str(TotYear)+" Year.  "+str(month1)+" Month.  "+str(ToTaL)+" Day.",bg="yellow",fg="black",font="Helvetica 10 bold")
                            detail_show.pack(side="top",padx=3,anchor="w")
                            selectedShowD=Label(frame6,text="DOB...  = "+dayGet+" / "+monthGet+" / "+yearGet,bg="yellow",fg="black",font="Helvetica 10 bold")
                            selectedShowD.pack(side="top",padx=3,anchor="w")
                            cross1=Button(crossF2,text="REMOVE",fg="red",bg="black",height=1,width=7,command=finish2,font="Times 8 bold")
                            cross1.pack(side="top",anchor="e")
                            #compare button
                            if compareCounter==2:
                                frame7=Frame(root,bg="pink")
                                frame7.pack(side="bottom",fill="x",pady=5)
                                compareBottom=Button(frame7,text="Compare...",fg="white",bg="black",font="Times 10 italic bold",height=1,bd=3,relief="sunken",width=8,command=comp)
                                compareBottom.pack(side="right",padx=6)
    #if any exception from getting any value from widget
    except Exception as Error:
        tmsg.showerror("ERROR....","Oppppssss,...\nSomething went wrong....")
        pass 
#resizable false     
root.resizable(False,False)
#create menu
menu=Menu(root)
age_m=Menu(menu,tearoff=0)
age_m.add_command(label="Exit",command=root.quit)
age_m.add_separator()
age_m.add_command(label="Help")
menu.add_cascade(label="Option",menu=age_m)
#colour is pink
#show menu with config
root.config(menu=menu,bg="pink")
#get local time
timee=time.localtime()
#get last year in a var
last_year=timee.tm_year
#get present month
pm=timee.tm_mon
#get present day
pd=timee.tm_mday
#empty list day
list_day=[]
#dict var with all month name and day
dict_month={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
#list of month name that come from dict month name
list_month=list(dict_month.keys())
#list of month day that come from dict month name
list_monthDay=list(dict_month.values())
#set frame
frame0=Frame(root,bg="pink")
frame1=Frame(root,bg="pink")
frame2=Frame(root,bg="pink")
frame3=Frame(root,bg="pink")
frame4=Frame(root,bg="pink")
frame0.pack(side="top",fill="x",pady=3)
frame1.pack(side="top",fill="x",pady=3)
frame2.pack(side="top",fill="x",pady=3)
frame3.pack(side="top",fill="x",pady=3)
frame4.pack(side="top",fill="x",pady=3)
name_label=Label(frame1,text="Name:-",bg="pink",fg="maroon",font=font)
name_label.pack(side="left",padx=7)
#name var is stringvar
name_var=StringVar()
#to see present date
p_label=Label(frame0,text="Today's Date  :  "+str(pd)+" / "+list_month[pm-1]+" / "+str(last_year),bg="pink",fg="green",font=font1)
p_label.pack(padx=7,side="left")
#set emptty string
name_var.set("")
name_entry=Entry(frame1,textvariable=name_var,width=25,font="Helvetica 10 bold")
name_entry.pack(side="left",padx=5)
date_label=Label(frame2,text="Enter Your DOB:-",bg="pink",fg="maroon",font=font)
date_label.pack(padx=7,side="left")
#use it for compare function
list_monthDay1=list_monthDay
list_month1=list_month
#list year empty 
list_year=[]
#append list day with 31
for day in range(1,32):
    list_day.append(day)
#combobox that come from tkinter ttk
#combo box work as drop down button
day_combobox=Combobox(frame3,value=list_day,width=2)
day_combobox.pack(side="left",padx=7)
day_label=Label(frame3,text="Day",bg="pink",fg="dark green",font="Courior 10 roman bold")
day_label.pack(side="left")
month_combobox=Combobox(frame3,value=list_month,width=10)
month_combobox.pack(side="left",padx=7)
month_label=Label(frame3,text="Month",bg="pink",fg="dark green",font="Courior 10 roman bold")
month_label.pack(side="left")
#append list year with present year
for year in range(1900,last_year+1):
    list_year.append(year)
year_combobox=Combobox(frame3,value=list_year,width=4)
year_combobox.pack(side="left",padx=7)
year_lebel=Label(frame3,text="Year",bg="pink",fg="dark green",font="Courior 10 roman bold")
year_lebel.pack(side="left",padx=3)
get_button=Button(frame4,text="Get Age.....",bg="green",fg="white",height=1,width=10,font="Times 10 italic bold",activebackground="red",command=getAge)
get_button.pack(side="right",padx=10,pady=3)
#keep cursor
name_entry.focus()
root.mainloop()