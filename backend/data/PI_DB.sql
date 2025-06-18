CREATE DATABASE IF NOT EXISTS PI_DB;
USE PI_DB;


/*
Al momento de crear la base de datos modificar el siguiente comando modificando el nombre vscode_user con el user que tenga en su BD, este debe coincidir con el que se asignara en el codigo.
*/
-- CREATE USER 'vscode_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user123';
-- GRANT ALL PRIVILEGES ON PI_DB.* TO 'vscode_user'@'localhost';   


-- DROP TABLE usuario;
-- DROP TABLE diagnostico;
-- DROP TABLE resumen;


-- ----------------------------------------------------------------------------------------------------------------------------------
-- Creacion de tablas de la base de datos.
CREATE TABLE usuario(
	id_usuario VARCHAR(10) NOT NULL,   -- Llave primaria de la tabla, cada usuario independiente del tipo de este tendra un id
    u_password VARCHAR(45) NOT NULL, 
    nombre VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL, 
    tipo_u VARCHAR(2) NOT NULL,  	   -- existiran tres tipos de usuarios 'm' para medico, 'p' para paciente y 'su' para super usuario, este tercero se pretende usar para administradores del sistema
    tipo_sangre VARCHAR(45), 		   -- puede aceptar valores nulos ya que para los usuarios 'm' y 'su' no sera relevante esta informacion 
    d_especialidad VARCHAR(45),  	   -- el mismo caso que en el anterior, solo sera valido para 'm'. Los 'p' y  'su' no tendran informacion aqui
    QR_acceso VARCHAR(255),  		   -- el acceso de QR sera solo para los pacientes, ya que el sistema leera su codigo QR y le aparecera la informacion al medico en el momento de la consulta
    PRIMARY KEY(id_usuario)  
);

CREATE TABLE diagnostico( 			   -- Esta tabla será consultada de forma de lectura por el usuario paciente, el usuario medico tendrá la posibilidad de crear nuevas entradas de datos en el sistema
	id_diagnostico INT AUTO_INCREMENT, -- La llave primaria de esta tabla no tendrá relevancia puesto a que se buscará conforme el id del usuario o del médico
    id_medico VARCHAR(10) NOT NULL,
    id_usuario VARCHAR(10) NOT NULL,  
    diagnostico VARCHAR(700),          
    PRIMARY KEY(id_diagnostico)
);

CREATE TABLE resumen( 				   -- El usuario creará entradas a esta tabla con la herramienta de generación de resumenes automáticos con base a los diagnósticos que seleccione.
	id_resumen INT AUTO_INCREMENT,	   -- guardar en cuanto se genere**
    id_usuario VARCHAR(10),
    resumen VARCHAR(700),
    PRIMARY KEY(id_resumen)
);



-- ------------------------------------------------------------------------------------------------------------------------------------
-- Creacion de usuarios base para visualizar el funcionamiento de la base de datos.
SELECT * FROM usuario;
INSERT INTO usuario (id_usuario,u_password,nombre,fecha_nacimiento,tipo_u,tipo_sangre)  -- Pacientes
VALUES 
('RaDam95','sfX2359','David Alejandro Ramirez Dominguez','1995-11-03','p','o positivo'),
('Lanah38','sablaIx45','Laura Angelica Hernanrez','1981-12-12','p','o positivo'),
('MemnL97','ausxje234A','Lucero Mendez Martinez','1997-02-03','p','o positivo'),
('Johana322','asfee3542A','Johan Arturo Gomez Oceza','1999-01-01','p','o negativo'),
('Nehtlen88','gidngri2342A','Nauron Acosta Tellez','1955-03-09','p','ab positivo'),
('Gibral5334','trip2025I','Gibralthar Corazon de Poeta Gutierrez','1990-11-03','p','ab negativo');
SHOW COLUMNS FROM usuario;

-- ----------------------------------------------------------------------------------------
-- Creacion de usuarios tipo medico para realizar las pruebas de insercion de diagnosticos. 
INSERT INTO usuario (id_usuario,u_password,nombre,fecha_nacimiento,tipo_u,d_especialidad)
VALUES
('draHeart88','ashdi24','Meliana Gutierrez Almaraz','1988-01-31','m','Cardiologia'),
('drCornelio','gege234','Augusto Comne Cornelio','1955-03-11','m','Omeopatia'),
('draMeaLoba','dfnkgri452','Meana Alejandra De la Hoya','1990-05-17','m','Psicologia'),
('drNeotro24','fgr25242','Joel Meotro Neruda','1975-11-12','m','Otorrinolaringologo'),
('drHehe1231','sdfkjbd92929','Neoel Neneli Broazgi','1964-12-25','m','Ortopedia');