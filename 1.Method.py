class MyClass:
    def method(self):
        return 'This is a instance method ,and now the instance method is called', self

    @classmethod
    def class_method(cls):
        return 'This is a class method, and now the class method is called', cls

    @staticmethod
    def static_method():
        return 'This is a static method, and now the static method is called'


print(MyClass.method())
