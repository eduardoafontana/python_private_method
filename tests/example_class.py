

class ExampleClass:

  def __my_private_method(self):
    return 'OK'

  def public_method(self):
    return self.__my_private_method()
