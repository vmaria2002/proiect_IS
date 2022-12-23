from sendMail import *
class Subject:
 
    """Represents what is being observed"""

    def __init__(self):
 
        """create an empty observer list"""
 
        self._observers = []
 
    def notify(self, modifier = None):
 
        """Alert the observers"""
 
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
 
    def attach(self, observer):
 
        """If the observer is not in the list,
        append it into the list"""
 
        if observer not in self._observers:
            self._observers.append(observer)
 
    def detach(self, observer):
 
        """Remove the observer from the observer list"""
 
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
 
 
 
class Observer(Subject):
 
    """monitor the object"""
 
    def __init__(self, name =''):
        Subject.__init__(self)
        self.name = name
        self._data = ""
 
    @property
    def data(self):
        return self._data
 
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()
 
 
class UpdateEmail:
 
    """updates the Decimal viewer"""
 
    def update(self, request):
        qaa(request)
        
