from datetime import datetime, timedelta
Yesterday = datetime.now() - timedelta(days=1)
Today = datetime.now()
Tommarow = datetime.now() + timedelta(days=1)
print("Yesrterday : ",Yesterday.date()) 
print("Today : ",Today.date()) 
print("Tommarow : ",Tommarow.date()) 