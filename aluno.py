import controller

class Aluno:

    table = "alunos"

    def setNome(self,nome):
        self.nome = nome

    def post(self):
        columns = "name,turma_id"
        values = f"'{self.nome}',NULL"
        controller.create(self.table,columns,values)

    def get(self):
        alunos = controller.select_all(self.table)
        return alunos

    def setTurma(self,turma):
        self.turma = turma
    
    def setId(self,id): 
        self.id = id

    def put(self):
        controller.update(self.table, "turma_id", self.turma, self.id)