from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Length


class LoginForm(FlaskForm):
    usuario = StringField('Nombre de usuario', validators=[Required()])
    password = PasswordField('Contraseña', validators=[Required()])
    enviar = SubmitField('Ingresar')


class SaludarForm(FlaskForm):
    usuario = StringField('Nombre: ', validators=[Required()])
    enviar = SubmitField('Saludar')


class RegistrarForm(LoginForm):
    password_check = PasswordField('Verificar Contraseña', validators=[Required()])
    enviar = SubmitField('Registrarse')

#Formulario para buscar determinado producto.
class ProductForm(FlaskForm):
    product = StringField('Producto', validators=[Required(), Length(min=3, message='Ingresa al menos 3 caracteres.')])
    enviar = SubmitField('Buscar')

#Formulario para buscar determinado cliente.
class ClientForm(FlaskForm):
    client = StringField('Cliente', validators=[Required(), Length(min=3, message='Ingresa al menos 3 caracteres.')])
    send = SubmitField('Buscar')