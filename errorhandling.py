"""
try
except
finally
"""

# for i in range(1,4):
#     try:
#         rand_num=int(input('enter a number>> '))
#         print(f"the is num {rand_num}")

#     except ValueError:
#         print("enter an integer")

num = [1, 2, 3]
try: 
    print ("Second element = %d" %(num[3]))   #%d is a placeholder to collect  the index (as decimal) coming from num and %(a[1]) is called formatting

    print ("Fourth element = %d" %(num[2]))

except IndexError:
    print ("index out of range")
finally:
    print("program completed" )