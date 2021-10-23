class Singleton:
 
    __shared_instance = 'SingletonClass'
 
    @staticmethod
    def getInstance():
 
        """Static Access Method"""
        if Singleton.__shared_instance == 'SingletonClass':
            Singleton()
        return Singleton.__shared_instance
 
    def __init__(self):
 
        """virtual private constructor"""
        if Singleton.__shared_instance != 'SingletonClass':
            raise Exception ("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self
 
# main method
if __name__ == "__main__":
 
    # create object of Singleton Class
    obj = Singleton()
    print(obj)
  
    # pick the instance of the class
    obj = Singleton.getInstance()
    print(obj)