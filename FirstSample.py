import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['jai_db']
mycol = mydb["jai_collection"]

class FirstSample:

    def add(self, name, address):
        if mycol.count_documents({'_id': name}) <= 0 :
            mdict = { "_id": name, "address": address }
            mycol.insert_one(mdict)
            print("\n *** After Insertion ***\n")
            self.show()
        else:
            print("Duplicate name found, please give another name")

    def remove(self,name):
        if mycol.count_documents({'_id': name}) > 0 :
            myquery = { "_id" : name}
            mycol.delete_one(myquery)
            print("\n *** After Deletion ***\n")
            self.show()
        else:
            print("Sorry no such document is present!!!!!!!!!")
	
    def modify(self,name,newaddress):
        if mycol.count_documents({'_id': name}) > 0 :
            myquery = { "_id" : name }
            newvalues = { "$set" : { "address" : newaddress } }
            mycol.update_one(myquery,newvalues)
            print("\n *** After Updation ***\n")
            self.show()
        else:
            print("Unable to Update, the document is not there !!!!!!!!")
		
    def show(self):
        for i in mycol.find():
            print(i)

flag = True
fs1 = FirstSample()
while flag :
	print("\n 1. Insertion\n 2. Updation \n 3. Deletion\n 4. Exit")
	response = int(input())
	if response == 1 :
		print("Please enter username and address to insert\n")
		username = str(input())
		address = str(input())
		fs1.add(username,address)
	elif response == 2 :
		print("Please enter username and new address to update\n")
		username = str(input())
		newaddress = str(input())
		fs1.modify(username,newaddress)
	elif response == 3 :
		print("please enter username to delete\n")
		username = str(input())
		fs1.remove(username)
	elif response ==4 :
		print("Thank you\n")
		flag = False
	else: 
		print("Please select valid option")
	
	



