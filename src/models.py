import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)


class Personas(Base):
    __tablename__ = 'personas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True,  nullable=False)
    genero = Column(String(50), nullable=False)
    nacimiento = Column(String(20), nullable=False)
    color_ojos = Column(String(20), nullable=False)  
    color_piel = Column(String(20), nullable=False) 
    color_pelo = Column(String(20), nullable=False)   
    peso = Column(Integer, nullable=False) 
    altura = Column(Integer, nullable=False) 
    

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True,  nullable=False)
    diametro = Column(Integer, nullable=False)
    rotacion = Column(Integer, nullable=False)
    orbital = Column(Integer, nullable=False)  
    gravedad = Column(String(50), nullable=False) 
    poblacion = Column(Integer, nullable=False) 
    clima = Column(String(50), nullable=False) 
    terreno = Column(String(50), nullable=False) 
    superficie_liquida = Column(Integer, nullable=False)   


class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True,  nullable=False)
    modelo = Column(String(50), nullable=False)
    clase = Column(String(20), nullable=False)
    constructor = Column(String(20), nullable=False)  
    coste = Column(Integer, nullable=False) 
    longitud = Column(Integer, nullable=False)  
    tripulacion = Column(Integer, nullable=False)  
    pasajeros = Column(Integer, nullable=False)
    velocidad = Column(Integer, nullable=False) 
    carga = Column(Integer, nullable=False) 
    provisiones = Column(String(100), nullable=False) 

class Favoritos_personas(Base):
    __tablename__ = 'favoritos_personas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(String(50), nullable=False)
    personas_id = Column(String(50), ForeignKey('personas.id')) 
    usuario_id = Column(Integer, ForeignKey('usuario.id'))  
    
class Favoritos_planetas(Base):
    __tablename__ = 'favoritos_planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(String(50), nullable=False)
    planetas_id = Column(String(20), ForeignKey('planetas.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))  

class Favoritos_vehiculos(Base):
    __tablename__ = 'favoritos_vehiculos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, nullable=False)
    vehiculos_id = Column(String(20), ForeignKey('vehiculos.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))  
  


# person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
