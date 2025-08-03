class Usuario:
    def __init__(self,id_usuario,u_password,nombre,fecha_nacimiento,tipo_u,tipo_sangre,d_especialidad,qr_acceso, correo_electronico, telefono,pad_cronico,donador_organos,accede_transfucion):
        self.id_usuario = id_usuario
        self.u_password = u_password
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_u = tipo_u
        self.tipo_sangre = tipo_sangre
        self.d_especialidad = d_especialidad
        self.qr_acceso = qr_acceso
        self.correo_electronico=correo_electronico;
        self.telefono=telefono;
        self.pad_cronico=pad_cronico;
        self.donador_organos=donador_organos;
        self.accede_transfucion=accede_transfucion;