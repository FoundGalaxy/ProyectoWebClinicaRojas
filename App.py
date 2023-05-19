from flask import Flask, render_template, request, redirect, url_for, flash, session, Response
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from fpdf import FPDF
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '587'
app.config['MAIL_USERNAME'] = 'clinicarojas.t4@gmail.com'
app.config['MAIL_PASSWORD'] = 'gycalyjyleydljrj'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

app.secret_key = 'CrRK'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '14271058lG.'
app.config['MYSQL_DB'] = 'Clinica'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def index_():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/indexli.html')
def indexli():
    return render_template('indexli.html')

@app.route('/especialidades.html')
def especialidades():
    return render_template('especialidades.html')

@app.route('/servicios.html')
def servicios():
    return render_template('servicios.html')

@app.route('/quienessomos.html')
def quienessomos():
    return render_template('quienessomos.html')

@app.route('/contactanos.html')
def contactanos():
    return render_template('contactanos.html')

@app.route('/registrarcita.html')
def registrarcita():
    return render_template('registrarcita.html')

@app.route('/registrarpaciente.html')
def registrarpaciente():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM pacientes')
    myresult = cursor.fetchall()
    #-Convertimos los datos a diccionario
    #insertObject = []
    #columnNames = [column[0] for column in cursor.description]
    #for record in myresult:
     #   insertObject.append(dict(zip(columnNames, record)))
    #cursor.close()
    return render_template('registrarpaciente.html', data=myresult)

@app.route('/citas.html')
def citas():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM citas')
    myresult = cursor.fetchall()
    return render_template('citas.html', data=myresult)

@app.route('/rp', methods=['POST'])
def regpac():
    nombre = request.form['nombre']
    ap_paterno = request.form['ap_paterno']
    ap_materno = request.form['ap_materno']
    fecha_nacimiento = request.form['f_nac']
    edad = request.form['edad']
    genero = request.form['genero']
    estado_civil = request.form['est_civil']
    tratamiento = request.form['tratamiento']
    num_familiares = request.form['Num_fam']
    nacionalidad = request.form['nacionalidad']
    estado = request.form['Estado']
    municipio = request.form['Municipio']
    direccion = request.form['direccion']
    codigo_postal = request.form['zip']
    telefono = request.form['telefono']

    if nombre and ap_paterno and ap_materno and fecha_nacimiento and edad and estado_civil and tratamiento and num_familiares and nacionalidad and estado and municipio and direccion and codigo_postal and telefono:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql = "INSERT INTO pacientes (nombre,ap_paterno,ap_materno,fecha_nacimiento,edad,genero,estado_civil,tratamiento,num_familiares,nacionalidad,estado,municipio,direccion,codigo_postal,telefono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
        data = (nombre,ap_paterno,ap_materno,fecha_nacimiento,edad,genero,estado_civil,tratamiento,num_familiares,nacionalidad,estado,municipio,direccion,codigo_postal,telefono)
        cursor.execute(sql,data)
        mysql.connection.commit()
    else:
        flash('Error: falta algun campo por llenar.')
    return redirect(url_for('registrarpaciente'))


@app.route('/rc', methods=['POST'])
def regcit():
    Nombre = request.form['Nombre']
    Ap_Paterno = request.form['Ap_Paterno']
    Ap_Materno = request.form['Ap_Materno']
    Fecha_Cita = request.form['Fecha_Cita']
    Hora_Cita = request.form['Hora_Cita']
    Medico = request.form['Medico']
    Asunto = request.form['Asunto']
    Correo = request.form['Correo']
    Telefono = request.form['Telefono']
    if Nombre and Ap_Paterno and Ap_Materno and Fecha_Cita and Hora_Cita and Medico and Asunto and Correo and Telefono:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql = "INSERT INTO citas (Nombre,Ap_Paterno,Ap_Materno,Fecha_Cita,Hora_Cita,Medico,Asunto,Correo,Telefono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )"
        data = (Nombre,Ap_Paterno,Ap_Materno,Fecha_Cita,Hora_Cita,Medico,Asunto,Correo,Telefono)
        cursor.execute(sql,data)
        mysql.connection.commit()
    else:
        flash('Error: falta algun campo por llenar.')
    return redirect(url_for('citas'))

@app.route('/delete/<string:folio>')
def delete(folio):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = "DELETE FROM pacientes WHERE folio=%s"
    data = (folio)
    cursor.execute(sql,data)
    mysql.connection.commit()
    return redirect(url_for('registrarpaciente'))

@app.route('/deletec/<string:idCita>')
def deletec(idCita):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = "DELETE FROM citas WHERE idCita=%s"
    data = (idCita)
    cursor.execute(sql,data)
    mysql.connection.commit()
    return redirect(url_for('citas'))

@app.route('/edit/<string:folio>', methods=['POST'])
def edit(folio):
    nombre = request.form['nombre']
    ap_paterno = request.form['ap_paterno']
    ap_materno = request.form['ap_materno']
    fecha_nacimiento = request.form['f_nac']
    edad = request.form['edad']
    genero = request.form['genero']
    estado_civil = request.form['est_civil']
    tratamiento = request.form['tratamiento']
    num_familiares = request.form['Num_fam']
    nacionalidad = request.form['nacionalidad']
    estado = request.form['Estado']
    municipio = request.form['Municipio']
    direccion = request.form['direccion']
    codigo_postal = request.form['zip']
    telefono = request.form['telefono']

    if nombre and ap_paterno and ap_materno and fecha_nacimiento and edad and genero and estado_civil and tratamiento and num_familiares and nacionalidad and estado and municipio and direccion and codigo_postal and telefono:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql = "UPDATE pacientes SET nombre=%s,ap_paterno=%s,ap_materno=%s,fecha_nacimiento=%s,edad=%s,genero=%s,estado_civil=%s,tratamiento=%s,num_familiares=%s,nacionalidad=%s,estado=%s,municipio=%s,direccion=%s,codigo_postal=%s,telefono=%s WHERE folio=%s"
        data = (nombre,ap_paterno,ap_materno,fecha_nacimiento,edad,genero,estado_civil,tratamiento,num_familiares,nacionalidad,estado,municipio,direccion,codigo_postal,telefono,folio)
        cursor.execute(sql, data)
        mysql.connection.commit()
    return redirect(url_for('registrarpaciente'))

@app.route('/editc/<string:idCita>', methods=['POST'])
def editc(idCita):
    Nombre = request.form['Nombre']
    Ap_Paterno = request.form['Ap_Paterno']
    Ap_Materno = request.form['Ap_Materno']
    Fecha_Cita = request.form['Fecha_Cita']
    Hora_Cita = request.form['Hora_Cita']
    Medico = request.form['Medico']
    Asunto = request.form['Asunto']
    Correo = request.form['Correo']
    Telefono = request.form['Telefono']

    if Nombre and Ap_Paterno and Ap_Materno and Fecha_Cita and Hora_Cita and Medico and Asunto and Correo and Telefono:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql = "UPDATE citas SET Nombre=%s,Ap_Paterno=%s,Ap_Materno=%s,Fecha_Cita=%s,Hora_Cita=%s,Medico=%s,Asunto=%s,Correo=%s,Telefono=%s WHERE idCita=%s"
        data = (Nombre,Ap_Paterno,Ap_Materno,Fecha_Cita,Hora_Cita,Medico,Asunto,Correo,Telefono,idCita)
        cursor.execute(sql, data)
        mysql.connection.commit()
    return redirect(url_for('citas'))


    
@app.route('/login.html', methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE username = % s AND password = % s', (username, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['id'] = user['idUser']
            session['username'] = user['username']
            msg = 'Inicio de sesion exitoso'
            return render_template('/indexli.html', msg = msg)
        else:
            msg = 'Nombre de usuario y/o contraseña incorrectos'
    return render_template('/login.html', msg = msg)

@app.route('/signup.html', methods=['GET','POST'])
def signup():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'mail' in request.form :
        username = request.form['username']
        password = request.form['password']
        mail = request.form['mail']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE username = % s', (username, ))
        user = cursor.fetchone()
        if user:
            msg = 'Cuenta existente'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', mail):
            msg = 'Direccion de correo invalida'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Usuario debe contener solo numeros y caracteres'
        elif not username or not password or not mail:
            msg = 'El campo de usuario o contraseña se encuentran vacios.'
        else:
            cursor.execute('INSERT INTO Users (username, password, mail) VALUES (%s, %s, %s)', (username, password, mail))
            mysql.connection.commit()
            msg = 'Se ha registrado exitosamente'
    elif request.method == 'POST':
        msg = 'Por favor llene todos los campos del formulario.'
    return render_template('/signup.html', msg = msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('idUser', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/recuperarpass.html')
def recuperarpass():
    return render_template('recuperarpass.html')

@app.route('/download/report/pdf/<idCita>',methods=['GET','POST'])
def download_report(idCita):
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM citas WHERE idCita = %s', (idCita))
        result = cursor.fetchall()
        
        pdf = FPDF(orientation="landscape", format="legal")
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin
        pdf.set_font('Times','B',18.0)
        pdf.cell(page_width, 0.0, 'CLINICA ROJAS | INFORMACION DE CITA', align='C')
        pdf.ln(10)
        pdf.set_font('Courier','',14)
        col_width = page_width/6
        col_width2 = page_width/4
        pdf.ln(1)
        th = pdf.font_size

        for row in result:
            pdf.cell(col_width, th, str(row['idCita']), border=1)
            pdf.cell(col_width, th, str(row['Nombre']), border=1)
            pdf.cell(col_width, th, str(row['Ap_Paterno']), border=1)
            pdf.cell(col_width, th, str(row['Ap_Materno']), border=1)
            pdf.cell(col_width, th, str(row['Fecha_Cita']), border=1)
            pdf.cell(col_width, th, str(row['Hora_Cita']), border=1)
            pdf.ln(th)
        
        pdf.ln(5)

        for row in result:
            pdf.cell(col_width2, th, str(row['Medico']), border=1)
            pdf.cell(col_width2, th, str(row['Asunto']), border=1)
            pdf.cell(col_width2, th, str(row['Correo']), border=1)
            pdf.cell(col_width2, th, str(row['Telefono']), border=1)
            pdf.ln(th)
        
        pdf.ln(10)

        pdf.image('./static/media/logo.png',140,80,80,80)
        pdf.set_font('Times','',14.0)
        pdf.cell(page_width, 0.0, '---------------------------------------------------------------- Fin de Reporte ----------------------------------------------------------------', align='C')

        return Response(pdf.output(dest='S').encode('latin-1'),mimetype='application/pdf',headers={'Content-Disposition':'attachment;filename=Reporte_Cita.pdf'})

    except Exception as e:
        print(e)
    finally:
        cursor.close()
    return redirect(url_for('citas'))

@app.route('/email/<idCita>',methods=['GET','POST'])
def email(idCita):

    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM citas WHERE idCita = %s', (idCita))
        result = cursor.fetchall()
        
        pdf = FPDF(orientation="landscape", format="legal")
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin
        pdf.set_font('Times','B',18.0)
        pdf.cell(page_width, 0.0, 'CLINICA ROJAS | INFORMACION DE CITA', align='C')
        pdf.ln(10)
        pdf.set_font('Courier','',14)
        col_width = page_width/6
        col_width2 = page_width/4
        pdf.ln(1)
        th = pdf.font_size

        for row in result:
            pdf.cell(col_width, th, str(row['idCita']), border=1)
            pdf.cell(col_width, th, str(row['Nombre']), border=1)
            pdf.cell(col_width, th, str(row['Ap_Paterno']), border=1)
            pdf.cell(col_width, th, str(row['Ap_Materno']), border=1)
            pdf.cell(col_width, th, str(row['Fecha_Cita']), border=1)
            pdf.cell(col_width, th, str(row['Hora_Cita']), border=1)
            pdf.ln(th)
        
        pdf.ln(5)

        for row in result:
            pdf.cell(col_width2, th, str(row['Medico']), border=1)
            pdf.cell(col_width2, th, str(row['Asunto']), border=1)
            pdf.cell(col_width2, th, str(row['Correo']), border=1)
            pdf.cell(col_width2, th, str(row['Telefono']), border=1)
            pdf.ln(th)
        
        pdf.ln(10)

        pdf.image('./static/media/logo.png',140,80,80,80)
        pdf.set_font('Times','',14.0)
        pdf.cell(page_width, 0.0, '---------------------------------------------------------------- Fin de Reporte ----------------------------------------------------------------', align='C')
        #pdf.output(('./static/pdf/info_cita.pdf', 'F').encode('latin-1'),mimetype='application/pdf')
        return Response(pdf.output('./static/pdf/info_cita.pdf', 'F').encode('latin-1'),mimetype='application/pdf',headers={'Content-Disposition':'attachment;filename=Reporte_Cita.pdf'})
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        #if request.method == 'POST':
        msg = Message("Clinica Rojas | Cita Registrada", sender='clinicarojas.t4@gmail.com',
                    recipients=['foundgalaxy343@gmail.com'])
        msg.body = "Saludos, a continuacion se envia le información de su cita agendada"
        with app.open_resource("./static/pdf/info_cita.pdf") as fp: msg.attach("./static/pdf/info_cita.pdf","application/pdf", fp.read())
        mail.send(msg)
        return redirect(url_for('citas'))
    #return redirect(url_for('citas'))
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug = True)