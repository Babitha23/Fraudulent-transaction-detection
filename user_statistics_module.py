try:
    import load_dataset_module as l
#**********************************************************************
#Calculates Minimum and Maximum transaction amount for the given userID:
#**********************************************************************
    def minmax(user):
        newlist = []
        i = 0
        for key in l.data[user]:
            newlist.insert(i, l.data[user][key][1])
            i = i+1
        return [min(newlist),max(newlist)]

#*************************************************************************************
#Calculates centroid based on locations of all the transactions made by a given userID:
#*************************************************************************************
    def centroid(user):
        x,y,i,j = [],[],0,0
        for key in l.data[user]:
            x.insert(i, l.data[user][key][2])
            i+=1
        for k in l.data[user]:
            y.insert(i, l.data[user][k][3])
            j+=1
        xcent = sum(x)/len(x)
        ycent = sum(y)/len(y)
        return (round(xcent,2),round(ycent,2))
        #return ((sum(x)/len(x)),(sum(y)/len(y)))

#************************************************************************************************
#Finding distance of any given transaction from the calculated centroid for that particular user:
#************************************************************************************************
    def distance(user, transid):
        (x1,y1) = centroid(user)
        for key,value in l.data.items():
            for i in value:
                if i == transid:
                    x2 = l.data[user][i][2]
                    y2 = l.data[user][i][3]
                    return round((((x1-x2)**2+(y1-y2)**2)**0.5),2)
        return False #UnboundLocalError("Transaction ID not found in data")

#***************************************************************
#Calculating variance for all the transactions made by any user:
#***************************************************************
    def variance(user):
        trans = []
        i = 0
        for key in l.data[user]:
            trans.insert(i, l.data[user][key][1])
            i += 1
        mean = round(sum(trans)/len(trans),2)
        var = round((sum((x-mean)**2 for x in trans) / len(trans)),2)
        return var

#*************************************************************************
#Calculating Standard deviation for all the transactions made by any user:
#*************************************************************************
    def stddev(usr):
        return round((variance(usr) ** 0.5),2)

#*******************************************
#A function to support printing the details:
#*******************************************
    def printdetails(trans):
        for k,v in l.data.items():
            for i in v:
                if i == trans:
                    print(f"""                    UserID: {k}
                    Transaction ID : {i}
                    Description: {l.data[k][i][0]}
                    Amount : {l.data[k][i][1]}
                    location : ({l.data[k][i][2]},{l.data[k][i][3]})
                    distance from centroid : {centroid(k)}
                    Fraud ? : {l.data[k][i][4]}
                    """)

#******************************************************
#Finding whether the transaction is fraudulent or not :
#******************************************************            
    def fraud(transid):
        for key,value in l.data.items():
            for i in value:
                if i == transid:
                    if l.data[key][i][4]=='false\n':
                        return("Relax! This transaction is NOT Fraudlent; the details of the transaction are as follows:")
                        #printdetails(transid)
                    elif l.data[key][i][4]=='true\n':
                        return("BEWARE! This transaction IS FRAUDULENT; the details of the transaction are as follows:")
                        #printdetails(transid)
        return False

#********************************************************************
#Calculating distance between any two transactions of user's choice:
#********************************************************************
    def transdistanceT(trans1,trans2):
        for key,value in l.data.items():
            for i in value:
                if i == trans1:
                    x1 = l.data[key][i][2]
                    y1 = l.data[key][i][3]
                elif i == trans2:
                    x2 = l.data[key][i][2]
                    y2 = l.data[key][i][3]
        return round((((x1-x2)**2+(y1-y2)**2)**0.5),2)
        
#********************************************************************
#Calculating distance between any two random transactions of same user:
#********************************************************************
    import random
    def transdistanceU(user):
        transid = []
        i = 0
        for key in l.data[user]:
            transid.insert(i, key)
            i += 1
        transid1=random.choice(transid)
        transid2=random.choice(transid)
        print(f"First random transcation ID of user {user} is : {transid1} ")
        print(f"Second random transcation ID of user {user} is : {transid2} ")
        return transdistanceT(transid1,transid2)
#********************************************************************

except ModuleNotFoundError:
    print('Please check again! Load_dataset_module is not found in your current working directory.')
    
######################################################################################################################