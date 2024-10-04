CREATE TABLE Personas (
    Id_Persona INT AUTO_INCREMENT PRIMARY KEY,
    Apellido VARCHAR(100) NOT NULL,
    Nombres VARCHAR(100) NOT NULL,
    DNI VARCHAR(15) NOT NULL,
    Domicilio VARCHAR(255),
    Fecha_Nac DATE,
    Telefono VARCHAR(20),
    FecHora_Registros TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FecHora_Modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    Edad INT,
    Genero ENUM('M', 'F', 'Otro'),
    Antiguedad INT,
    Email VARCHAR(100),
    Id_Reparticion INT,
    Id_Estado_Registro INT DEFAULT 1,
    FOREIGN KEY (Id_Reparticion) REFERENCES Reparticion(Id_Reparticion),
    FOREIGN KEY (Id_Estado_Registro) REFERENCES Estados_Registro(Id_Estado_Registro)
);

CREATE TABLE Reparticion (
    Id_Reparticion INT AUTO_INCREMENT PRIMARY KEY,
    Nombres VARCHAR(100) NOT NULL,
    Descripcion TEXT,
    Id_Estado_Registro INT DEFAULT 1,
    FOREIGN KEY (Id_Estado_Registro) REFERENCES Estados_Registro(Id_Estado_Registro)
);

CREATE TABLE Estados_Registro (
    Id_Estado_Registro INT AUTO_INCREMENT PRIMARY KEY,
    Descripcion VARCHAR(100) NOT NULL
);