import pymongo
'make db connection'
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testDatabase"]

'a document in MongoDB same as record in SQl'

'insert a column into testDatabase'

mycol = mydb["customers"]

'add data'

mydict ={"name" : "John", "Address" : "23 London Road"}

x = mycol.insert_one(mydict)