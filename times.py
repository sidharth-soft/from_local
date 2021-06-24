import time
# time.sleep(15)
# print('jaya')
# time.sleep(10)
# print('krishna')
# print(time.time())
print(time.localtime())
print(time.asctime())

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%d-%m-%Y, %H/%M:%S", named_tuple)

print(time_string)


#date

#os

