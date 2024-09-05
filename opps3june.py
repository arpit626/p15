class Add:
    def _init_(self, n):
        self.__n = n

    def _str_(self):
        return f"{self.__n}"

    def showN(self):
        return self.__n

    def _add_(self, other):
        sum = Add(self._n + other._n)
        return sum


n1 = Add(12)
n2 = Add(18)
print(n1 + n2)
      
class Products:
    __count = 0

    def _init_(self, name, price, description):
        self.__name = name
        self.__price = price
        self.__description = description
        Products.__count += 1

    # python calls the method _str_(dunder/magic) itself,
    # when we print object
    def _str_(self):
        return f"{self.__productdetails()}"

    @classmethod
    def productcount(cls):
        return cls.__count

    def productname(self):
        return self.__name

    def productprice(self):
        return self.__price

    def productdescription(self):
        return self.__description

    def __productdetails(self):
        return f"""PRODUCT DETAILS
Name: {self.__name}
Price: {self.__price}
Description: {self.__description}"""


p1 = Products("Iphone", 60000, "iphone 15")
p2 = Products("Macbook", 195000, "m3 latest")
p3 = Products("Airpods", 23000, "pro version")

print(p1)
print(p2)
print(p3)      