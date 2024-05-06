class MyClass:
    def __init__(self, value):
        self.value = value  

    def private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("Calling private method from public method:")
        self.private_method()

obj = MyClass(42)
obj.public_method()
# obj.__private_method() 
