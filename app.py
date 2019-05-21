from serverDAO import server
from dao.departamento import Departamento
from dao.funcionario import Funcionario
from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)
@app.route('/')
def init():
    return render_template('index.html')
@app.route('/listarDepartamento')
def listarDepartamento():
    dao = server()
    a = dao.listarDepartamento()
    b = []
    for lista in a:
        a = Departamento(lista[1])
        a.alterarGerente(lista[2])
        x = dao.buscarFuncionario(a.obterGerente()).obterNome()
        a.alterarGerente(x)
        a.alterarCodigo(lista[0])
        b.append(a)
    return render_template('listarDepartamento.html', dep=b)
@app.route('/listarFuncionario')
def listarFuncionario():
    dao = server()
    a = dao.listarFuncionario()
    b = []
    for lista in a:
        a = Funcionario(lista[1],lista[2])
        a.alterarCodigo(lista[0])
        x = dao.buscarDepartamento(a.obterDepartamento()).obterNome()
        a.alterarDepartamento(x)
        b.append(a)
    return render_template('listarFuncionario.html', func=b)
@app.route('/formBuscarDepartamento')
def formBuscarDepartamento():
    return render_template('buscarDepartamento.html')
@app.route('/buscarDepartamento',methods=['GET','POST'])
def buscarDepartamento():
    if request.method == 'POST': 
        cod = request.form['codigo']
        dao = server()
        a = dao.buscarDepartamento(cod)
        if(a.obterNome()=='None'):
            return render_template('erroCodigo.html',pag = "formBuscarDepartamento")
        else:
            x = dao.buscarFuncionario(a.obterGerente()).obterNome()
            a.alterarGerente(x)
            return render_template('templateDepartamento.html',depto=a)
@app.route('/formBuscarFuncionario')
def formBuscarFuncionario():
    return render_template('buscarFuncionario.html')
@app.route('/BuscarFuncionario',methods=['GET','POST'])
def buscarFuncionario():
    if request.method == 'POST': 
        cod = int(request.form['codigo'])
        dao = server()
        a = dao.buscarFuncionario(cod)
        if(a.obterNome()=='None'):
            return render_template('erroCodigo.html', pag="formBuscarFuncionario")
        else:
            x = dao.buscarDepartamento(a.obterDepartamento()).obterNome()
            a.alterarDepartamento(x)
            return render_template('templateFuncionario.html',func=a)
@app.route('/deletarFuncionario/<cod>')
def deletarFuncionario(cod):
    cod = int(cod)
    dao = server()
    a = dao.deletarFuncionario(cod)
    return redirect('/listarFuncionario')
@app.route('/deletarDepartamento/<cod>')
def deletarDepartamento(cod):
    cod = int(cod)
    dao = server()
    a = dao.deletarDepartamento(cod)
    return redirect('/listarDepartamento')
@app.route('/formInserirDepartamento')
def formInserirDepartamento():
    return render_template('inserirDepartamento.html')
@app.route('/inserirDepartamento',methods=['GET','POST'])
def inserirDepartamento():
    if request.method == 'POST': 
        nome = request.form['nome']
        dao = server()
        a = Departamento(nome)
        a = dao.inserirDepartamento(a)
        return redirect('listarDepartamento')
@app.route('/formInserirFuncionario')
def formInserirFuncionario():
    dao = server()
    a = dao.listarDepartamento()
    b = []
    for lista in a:
        a = Departamento(lista[1])
        a.alterarGerente(lista[2])
        a.alterarCodigo(lista[0])
        b.append(a)
    return render_template('inserirFuncionario.html', depto = b)
@app.route('/inserirFuncionario',methods=['GET','POST'])
def inserirFuncionario():
    if request.method == 'POST': 
        nome = request.form['nome']
        depto = request.form['departamento']
        dao = server()
        b = Funcionario(nome,depto)
        a = dao.inserirFuncionario(b)
        return redirect('listarFuncionario')
@app.route('/formAlterarDepartamento/<cod>')
def formAlterarDepartamento(cod):
    dao = server()
    a = dao.buscarDepartamento(cod)
    b = dao.buscarFuncionario(a.obterGerente())
    x = dao.listarFuncionario()
    c = []
    for lista in x:
        x = Funcionario(lista[1],lista[2])
        x.alterarCodigo(lista[0])
        c.append(x)
    return render_template('alterarDepartamento.html',depto=a,gerente=b,func = c)
@app.route('/alterarDepartamento',methods=['GET','POST'])
def alterarDepartamento():
    if request.method == 'POST': 
        nome = request.form['nome']
        gerente = request.form['gerente']
        cod = request.form['codigo']
        dao = server()
        depto = Departamento(nome)
        depto.alterarCodigo(cod)
        depto.alterarGerente(gerente)
        dao.alterarDepartamento(depto)
        return redirect('/listarDepartamento')
@app.route('/formAlterarFuncionario/<cod>')
def formAlterarFuncionario(cod):
    dao = server()
    a = dao.buscarFuncionario(int(cod))
    b = dao.buscarDepartamento(a.obterDepartamento())
    x = dao.listarDepartamento()
    d = []
    for lista in x:
        x = Departamento(lista[1])
        x.alterarCodigo(lista[0])
        x.alterarGerente(lista[2])
        d.append(x)
    return render_template('alterarFuncionario.html',func=a,departamento=b,depto=d)
@app.route('/alterarFuncionario',methods=['GET','POST'])
def alterarFuncionario():
    if request.method == 'POST': 
        nome = request.form['nome']
        cod = request.form['codigo']
        depto = request.form['departamento']
        dao = server()
        a = Funcionario(nome,depto)
        a.alterarCodigo(cod)
        dao.alterarFuncionario(a)
        return redirect('listarFuncionario')
# $app
def main():
    app.env = 'development'
    app.run(debug=True, port=7500)
if __name__ == "__main__":
    main()