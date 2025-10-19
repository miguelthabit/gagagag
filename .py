print("********$$$$$$$$^^^^^")
class Uppercase :
    def __init__(self,text):
        self.text=text
    
    def touppercase(self):
        return self.text.upper()
    
converter = Uppercase("Hello guys today is taco monday")
res