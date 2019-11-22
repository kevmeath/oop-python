class MyClass (object):
    class_attribute = 'world'

    def my_method (self, param1):
        print('\nhello {}'.format(param1))
        print('The object that called this method is: {}'.format(str(self)))
        self.instance_attribute = param1

my_instance = MyClass()
print(dir(my_instance))
my_instance.my_method('world')
