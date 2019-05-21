import psycopg2
from dao.departamento import Departamento
from dao.funcionario import Funcionario
class server():
    def conectar(self):
        banco = "dbname=banco user=postgres password=postgres host=localhost port=5432"
        return psycopg2.connect(banco)
    def buscarDepartamento(self, codigo):
        conexao = self.conectar()
        cur = conexao.cursor()
        try:
            codigo = int(codigo)
            try:
                cur.execute("SELECT * FROM departamento WHERE codigo = %s", [codigo])
                resposta = cur.fetchall()
                depto = Departamento(resposta[0][1])
                depto.alterarCodigo(resposta[0][0])
                depto.alterarGerente(resposta[0][2])
                return depto
            except IndexError:
                dep = Departamento("None")
                dep.alterarCodigo("None")
                dep.alterarGerente("None")
                return dep
        except:
            dep = Departamento("None")
            dep.alterarCodigo("None")
            dep.alterarGerente("None")
            return dep
        cur.close()
        conexao.close()
    def buscarFuncionario(self, codigo):
        conexao = self.conectar()
        cur = conexao.cursor()
        if(type(codigo)!=int):
            func = Funcionario("None","None")
            func.alterarCodigo("None")
            return func
        else: 
            try:
                cur.execute("SELECT * FROM funcionario WHERE codigo = %s", [codigo])
                resposta = cur.fetchall()
                func = Funcionario(resposta[0][1], resposta[0][2])
                func.alterarCodigo(resposta[0][0])
                if(str(func.obterDepartamento())=='None'):
                    func.alterarDepartamento("desempregado")
                return func
            except IndexError:
                fun = Funcionario("None","None")
                fun.alterarCodigo("None")
                return fun
        cur.close()
        conexao.close()
    def inserirDepartamento(self, dep):
        conexao = self.conectar()
        cur = conexao.cursor()
        try:
            cur.execute("INSERT INTO departamento(nome) VALUES(%s)", [dep.obterNome()])
            conexao.commit()
            a = 'Depto adicionado com sucesso!'
            return a
        except IndexError:
            a = 'Ops, houve um erro ao inserir o departamento!'
            return a
        cur.close()
        conexao.close()
    def inserirFuncionario(self, func):
        conexao = self.conectar()
        cur = conexao.cursor()
        try:
            codigo = int(func.obterDepartamento())
            x = self.buscarDepartamento(codigo)
            if(str(x.obterNome())=="None"):
                a = "Esse departamento não existe, se liga!"
                return a
            try:
                cur.execute("INSERT INTO funcionario(nome,coddepartamento) VALUES(%s,%s)", [func.obterNome(),func.obterDepartamento()])
                conexao.commit()
                a = 'Funcionario adicionado com sucesso!'
                return a
            except IndexError:
                a = 'Ops, houve um erro ao inserir o funcionario!'
                return a
        except:
            a = "coloca um codigo direito brô"
            return a
        cur.close()
        conexao.close()
    def listarDepartamento(self):
        conexao = self.conectar()
        cur = conexao.cursor()
        try:
            cur.execute("SELECT * FROM departamento")
            resposta = cur.fetchall()
            return resposta
        except IndexError:
            return 'Há um erro no banco de dados, sinto muito!'
        cur.close()
        conexao.close()
    def listarFuncionario(self):
        conexao = self.conectar()
        cur = conexao.cursor()
        try:
            cur.execute("SELECT * FROM funcionario")
            resposta = cur.fetchall()
            return resposta
        except IndexError:
            return 'Há um erro no banco de dados, sinto muito!'
        cur.close()
        conexao.close()
    def deletarDepartamento(self, codigo):    
        conexao = self.conectar()
        cur = conexao.cursor()
        try:
            cur.execute("DELETE FROM departamento WHERE codigo = %s", [codigo])
            conexao.commit()
            a = "departamento deletado com sucesso"
            return a
        except IndexError:
            a = 'Código incorreto!'
            return a
        cur.close()
        conexao.close()
    def deletarFuncionario(self, codigo):
        conexao = self.conectar()
        cur = conexao.cursor()
        try:
            cur.execute("DELETE FROM funcionario WHERE codigo = %s", [codigo])
            conexao.commit()
            a = "funcionario deletado com sucesso"
            return a
        except IndexError:
            a = 'Código incorreto!'
            return a
        cur.close()
        conexao.close()
    def alterarDepartamento(self, dep):
        conexao = self.conectar()
        cur = conexao.cursor()
        try:
            dep.alterarGerente(int(dep.obterGerente()))
            dep.alterarCodigo(int(dep.obterCodigo()))
            cur.execute("UPDATE departamento SET nome = %s, codgerente = %s WHERE codigo = %s", [dep.obterNome(), dep.obterGerente(), dep.obterCodigo()])
            conexao.commit()
            a = "Departamento alterado com sucesso!"
            return a
        except:
            a = "Algum dado foi inserido incorretamente"
            return a
        cur.close()
        conexao.close()
    def alterarFuncionario(self, func):
        conexao = self.conectar()
        cur = conexao.cursor()
        try:
            func.alterarDepartamento(int(func.obterDepartamento()))
            func.alterarCodigo(int(func.obterCodigo()))
            cur.execute("UPDATE funcionario SET nome = %s, coddepartamento = %s WHERE codigo = %s", [func.obterNome(), func.obterDepartamento(), func.obterCodigo()])
            conexao.commit()
            return "funcionario alterado com sucesso!"
        except:
            return "Algum dado foi inserido incorretamente"
        cur.close()
        conexao.close()
a = server()