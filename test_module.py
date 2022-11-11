#!/usr/bin/env python
# coding: utf-8

try:
    import user_statistics_module as us
    def main():
        try:
            print("Greetings! What would you like to investigate today?")
            n = int(input("""Please select from the below options:
            1. Find Minimum and Maximum transaction amount of a user;
            2. Find Centroid for all transaction locations of a user;
            3. Find distance of a transaction location from the centroid;
            4. Calculate Variance of the transactions made by a user;
            5. Calculate Standard deviation of the transactions made by a user;
            6. Find whether a transaction is fraudulent;
            7. Calculate distance between any two transactions' location of my choice;
            8. Calculate distance between any two random transactions' location of a user;
            """))
            if n == 1 :
                u = input("Please enter the User ID:")
                try:
                    (mini,maxi) = us.minmax(u)
                    print(f"Minimum transaction amount by user '{u}' was: £", mini)
                    print(f"And Maximum transaction amount by user '{u}' was: £", maxi)
                except KeyError:
                    print(f"UserID '{u}' not found! Please enter the correct userID!")
            elif n == 2 :
                u = input("Please enter the User ID:")
                try:
                    print(f"The location centroid of all the transactions made by {u} is :", us.centroid(u))
                except KeyError:
                    print(f"UserID '{u}' not found! Please enter the correct userID!")
            elif n == 3 :
                u = input("Please enter the User ID:")
                t = input("Please enter the transaction ID that you want to investigate:")
                try:
                    if not us.distance(u,t):
                        raise UnboundLocalError
                    else:
                        print(f"Distance of the transaction {t} from its centroid is : {us.distance(u,t)}")
                except KeyError:
                    print("Uh-Oh..!! Please verify if the entered userID-TransactionID duo is valid!!")
                except UnboundLocalError:
                    print("Oops! Transaction ID not found in data")
            elif n == 4 :
                u = input("Please enter the User ID:")
                try:
                    print(f"Variance for all the transactions made by user {u} is : {us.variance(u)}")
                except KeyError:
                    print(f"UserID '{u}' not found! Please enter the correct userID!")
            elif n == 5 :
                u = input("Please enter the User ID:")
                try:
                    print(f"Standard deviation for all the transactions made by user {u} is : {us.stddev(u)}")
                except KeyError:
                    print(f"UserID '{u}' not found! Please enter the correct userID!")
            elif n == 6 :
                t = input("Please enter the transaction ID: ")
                try:
                    if not us.fraud(t):
                        raise UnboundLocalError
                    else:
                        print(us.fraud(t))
                        us.printdetails(t)
                except KeyError:
                    print(f"UserID '{u}' not found! Please enter the correct userID!")
                except UnboundLocalError:
                    print("Oops! Transaction ID not found in data")
            elif n == 7 :
                t1 = input("Please enter the first transaction ID: ")
                t2 = input("Please enter the second transaction ID: ")
                try:
                    print(f"Distance between the transactions {t1} and {t2} is : {us.transdistanceT(t1,t2)}")
                except KeyError:
                    print("Uh-Oh..!! Please verify if the entered TransactionIDs are valid!!")
                except UnboundLocalError:
                    print("Uh-Oh..!! Please verify if the entered TransactionIDs are valid!!")
            elif n == 8 :
                u = input("Please enter the User ID:")
                try:
                    print(f"The distance between two random transactions of user '{u} is : {us.transdistanceU(u)}")
                except KeyError:
                    print(f"UserID '{u}' not found! Please enter the correct userID!")            
            else:
                print("You have entered the wrong option! GoodBye!")
        except ValueError:
            print("Oops!! Please enter valid input!")
except ModuleNotFoundError:
    print('Please check again! user_statistics_module is not found in your current working directory.')

main()