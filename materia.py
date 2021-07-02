import controller

class Materia:
    table = "materias"

    def setNome(self,nome):
        self.nome = nome

    def post(self):
        
        columns = "name"
        values = f"'{self.nome}'"
        controller.create(self.table,columns,values)

    def get(self):
        materias = controller.select_all(self.table)
        return materias

    def get_nome(self, id):
        return controller.find(self.table,id) 