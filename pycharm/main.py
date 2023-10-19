b = 0 #simulated b > 1

try:
    if(b < 1):
        raise ValueError("B cannot be divided by zero")

except ValueError as error:
    print("The error we generated caught by exception: ", str(error))
#

str_list = ["apples","oranges","tomatoes"]
for i in str_list:
    print(i)


# print("apples" in str_list)
# assert "mandarin" in str_list

try:
    if("mandarin" not in str_list):
        raise ValueError("mandarin")
except ValueError as error:
    print("Array needs to contain word: ",str(error))


def func(a,b):
    print(a,b)

func(1,2)

func(2,3)
