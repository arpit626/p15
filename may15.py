# exception handling 

# try:
#     try-Block
#     code which can raise error 
# catch Exception as err:
#     error holds the error message 

try:
    a = 12
    print(a+b) 
    print("all done well")

except Exception as err:
    print("error >>> ",err)



try:
    a = 12
    # b = "v"
    print(a/0) 
    print("all done well")

except TypeError as err:
    print("error >>> ", "Mismatch input")
except NameError as err:
    print("error >>>", "Variable Not Defined")
except Exception as err:
    print(err)


