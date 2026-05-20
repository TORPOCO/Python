from usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log

opcion = None
while opcion != 5:
    print('Obciones:')
    print('1.Listar usuarios')
    print('2.Agregar usuario')
    print('3.Modificar usuario')
    print('4.Eliminar usuario')
    print('5.Salir')
    opcion = int(input('Ingrese su opcion (1-5): '))
    if opcion == 1:
        usuario = UsuarioDAO.seleccionar()
        for usuario in usuario:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(username=username_var,password=password_var)
        usuario_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuario_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input('Ingrese el id del usuario a modificar: '))
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Ingrese el id del usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
    else:
        log.info('Salimos de la aplicación')