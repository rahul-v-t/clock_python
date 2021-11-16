from datetime import datetime
import time
import math
i=1
print(abs(math.sqrt(25)))
while i<2:
    date = datetime.now()
    current_time = date.strftime("%H:%M:%S")
    print( current_time, end="\r")
    time.sleep(1)


