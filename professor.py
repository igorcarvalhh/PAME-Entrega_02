import controller

class Professor:
    table = "professores"

    def setNome(self,nome):
        self.nome = nome

    def post(self):
        columns = "name"
        values = f"'{self.nome}'"
        controller.create(self.table,columns,values)   

    def get(self):
        professores = controller.select_all(self.table)
        return professores

    def get_nome(self, id):
        return controller.find(self.table,id) 

    