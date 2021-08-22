class Student:
    name=""
    id=""
    cgpa=""

    def set_value(self,name,id,cgpa):
        self.name=name;
        self.id=id;
        self.cgpa=cgpa;

    def display(self):
            print(self.name,self.id,self.cgpa)

bishajit=Student();
bishajit.set_value("Bishajit",2018000000010,3.68);
bishajit.display();

