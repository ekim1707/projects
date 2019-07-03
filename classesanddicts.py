class Person():

    population = 0

    def __init__(self,persondict):
        self.first = persondict.get('first')
        self.last = persondict.get('last')
        self.age = persondict.get('age')
        self.setgreeting()
        Person.population +=1

    def __resp__(self):
        return "{} {}".format(self.first,self.last)
    
    def setgreeting(self):
        if self.age < 5:
            self.greeting ='Waaaahh'
        elif self.age < 18:
            self.greeting = 'Sup'
        else:
            self.greeting = 'Hello'
        
    def greet(self):
        self.setgreeting()
        print(self.greeting)
    
    @staticmethod
    def build_dictionary(mystr):
        parts = mystr.split(',')
        if len(parts) == 3:
            return {
                'first': parts[0],
                'last': parts[1],
                'age': int(parts[2])
            }
        else:
            raise Exception('Error: Supply the right parameters')


    @classmethod
    def from_string(cls, mystr):
        return cls(cls.build_dictionary(mystr))



gary = Person.from_string('Gary,Storey,48')
print(gary.__dict__)