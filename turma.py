import controller

class Turma:
    table = "turmas"

    def setMateria(self,id_materia):
        self.id_materia = id_materia

    def setProfessor(self,id_professor):
        self.id_professor = id_professor

    def post(self):
        columns = "professor_id,materia_id,num_alunos"
        values = f"'{self.id_professor}','{self.id_materia}',0"
        controller.create(self.table,columns,values)   

    def get(self):
        turmas = controller.select_all(self.table)
        return turmas

    def setId(self,id): 
        self.id = id

    def put(self):
        controller.update(self.table, "professor_id", self.id_professor, self.id)  

    def add_aluno(self):
        num_alunos = controller.find(self.table,self.id)[0][3] + 1
        controller.update(self.table, "num_alunos",num_alunos,self.id)


def main():
    return 0;
    
if __name__ == '__main__':
    main()