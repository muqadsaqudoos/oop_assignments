class Class:
    def __init__(self,name,roll_no,department,gpa_in_each_subject):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.gpa_in_each_subject = gpa_in_each_subject

    @property 
    def name(self):
        return self.__name
    @name.setter
    def name(self,d):
        self.__name = d
        return self.__name
    
    @property 
    def roll_no(self):
        return self.__roll_no
    @roll_no.setter
    def roll_no(self,d):
        self.__roll_no = d
        return self.__roll_no
    
    @property 
    def department(self):
        return self.__department
    @department.setter
    def department(self,d):
        self.__department = d
        return self.__department
    
    @property 
    def gpa_in_each_subject(self):
        return self.__gpa_in_each_subject
    @gpa_in_each_subject.setter
    def gpa_in_each_subject(self,d):
        self.__gpa_in_each_subject = d
        return self.__gpa_in_each_subject
    

    def cgpa(self):
        sum = 0
        for i in range(len(self.gpa_in_each_subject)):
            sum += self.gpa_in_each_subject[i]

        return sum/len(self.gpa_in_each_subject)

   
