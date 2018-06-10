
# coding: utf-8

# In[66]:


#########################################################################
class Animal:
    count = 0
    def __init__(self, species):
        self.species = True
        self.living = True
        self.bioKingdom = "Animalia"
        self.firstStage = "Blastula"
        Animal.count += 1
        
#########################################################################        
class Male(Animal):
    count = 0
    def __init__(self):
        self.gender = "male"
        Male.count += 1
        
#########################################################################        
class Female(Animal):
    count = 0
    def __init__(self):
        self.gender = "female"
        Female.count += 1

#########################################################################        
class Human(Animal):
    count = 0
    
    def __init__(self, info):
        Human.count += 1
        self.info = info
        keyList = self.info.keys()
        if ("gender" in keyList):
            gender = info["gender"].lower()
            if (gender == "female"):
                Female.__init__(self)
            elif (gender == "male"):
                Male.__init__(self)
        for key in keyList:
            if ((isinstance(key,str)) and (key.lower() != "gender")):
                val = info[key]
                setattr(self, key, val)
        
    def name(self):
        self.name = "{} {}".format(self.first, self.last)
        return self.name
    
    def __repr__(self):
        string = "HUMAN DETAILS: \n"
        for key in self.info:
            tempString = "{}: {} \n".format(key, self.info[key])
            string += tempString
        return string
            
        

#########################################################################
def debug():
    dictInfo = {"first": "Test1", "last": "Test2", "age": 0, "weight": 0, "height": "0'0\"", 
                "gender": "male", "ethnicity": "ZZZ", "nationality": "Earth"}
    me = Human(dictInfo)
    print(me)
    print(Animal.count)
    print(Male.count, ",", Female.count)
    print(Human.count)
debug()

