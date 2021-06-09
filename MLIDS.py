import sniffer
import modifier
import pickle
import sklearn
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import metrics
from tkinter import *
# ML Model training code
'''
df = pd.read_csv(r'allAttack0.csv',header=None)
df[0:5]
df[14]=df[13]
df[14]=1
#df[14].unique()

df1 = pd.read_csv(r'normal3.csv',header=None)
df1[0:5]
df1[14]=df1[13]
df1[14]=0
#df1[14].unique()



frames=[df,df1]
dataset=pd.concat(frames)

dataset.replace('?',-9999,inplace=True)
X=dataset.drop([0,1,14],axis="columns")
y=np.array(dataset[14])

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)
clf=svm.SVC()
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

print("Accuracy",metrics.accuracy_score(y_test,y_pred))
#print(results)

#Saving model
filename="microdatasetmodel.sav"
pickle.dump(clf,open(filename,'wb'))
'''

# list of table heads
lst = ['sip           ', 'dip            ', 'tcpCount', 'tcpSportCount', 'tcpDportCount', 'tcp_fin', 'tcpSyn', 'tcpPush', 'tcpAck',
        'tcpUrg', 'udpCount', 'udpSport', 'udpDport', 'icmp count', 'Type']

# Global Status Flag
flag = 0

# Globally Loading Machine Learning Model
filename = "microdatasetmodel.sav"
load_picklemodel = pickle.load(open(filename, 'rb'))

# Tkinter Start Button code
def start():
    print("Giving Flag to IDS")
    global flag
    flag = True


# Tkinter recursive loop code
def StartIDS():

    #Delete previous Entries before new loop
    print(len(tableFrame.winfo_children()))
    if len(tableFrame.winfo_children()):
        for i in tableFrame.winfo_children():
            i.destroy()

    #Displaying Table Heads
    for heads in range(len(lst)):
        e = Entry(tableFrame,width=len(lst[heads]))
        e.grid(row=0, column=heads, padx=0, pady=0)
        e.insert(END,lst[heads])

    # Run when Start is pressed i.e flag is True
    if flag:
        # Starting sniffer
        df = sniffer.sniff()
        # modifier.modify()

        # Pickle programn
        if len(df) > 0:
            df = df.fillna(value=np.nan)
            df = df.replace(np.nan, int(0))
            temp = df
            temp = temp.drop(['sip', 'dip'], axis=1)
            result = load_picklemodel.predict(temp)

            # output dataframe for GUI
            df[14] = result  # appending ML results to dataframe

            # table creation
            # total number of rows and columns in list
            total_columns = 15
            total_rows = len(df.index)
            print(total_rows)
            for i in range(total_rows):
                if df.iat[i,14]==1:
                    for j in range(total_columns):
                        e = Entry(tableFrame,bg="Red",width=len(lst[j]))
                        e.grid(row=i + 2, column=j, padx=0, pady=0)
                        e.insert(END, df.iat[i, j])
                else:
                    for j in range(total_columns):
                        e = Entry(tableFrame, width=len(lst[j]))
                        e.grid(row=i + 2, column=j, padx=0, pady=0)
                        e.insert(END, df.iat[i, j])
    root.after(3000,StartIDS)

# Tkinter Stop Button Code
def stop():
    print("Stopping IDS")
    global flag
    flag = 0

# Close button program
def close():
    print("Closing program")
    root.destroy()


root = Tk()
root.geometry("1280x720")
root.title("MLIDS")

controlFrame = Frame(root)
controlFrame.grid(row=0,column=0, padx=5, pady=0)

startButton = Button(controlFrame, text="Start", command=start)
startButton.grid(row=0, column=0, padx=0, pady=5)

stopButton = Button(controlFrame, text="Stop", command=stop)
stopButton.grid(row=1, column=0, padx=0, pady=5)

closeButton = Button(controlFrame, text="Close", command=close)
closeButton.grid(row=2, column=0, padx=0, pady=5)

tableFrame = Frame(root)
tableFrame.grid(row=0,column=1)

root.after(3000,StartIDS)

root.mainloop()

