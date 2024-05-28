import os
import sys
from sq import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    nombre = Column(String(120), nullable=False)
    apellido = Column(String(120), nullable=False)
    fecha_subscripcion = Column(DateTime, nullable=False) 
    favoritos = relationship('Favorito', back_populates='usuario')
class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    descripcion = Column(String(250))
    favorito = relationship('Favorito', back_populates='personaje')
class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    descripcion = Column(String(250))
    favorito = relationship('Favorito', back_populates='planeta')
class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    usuario = relationship('Usuario', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favorito')
    planeta = relationship('Planeta', back_populates='favorito')
engine = create_engine('sqlite:///starwars_blog.db')
Base.metadata.create_all(engine)
render_er(Base, 'diagram.png')
