from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Docente

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///demobase.db')


Session = sessionmaker(bind=engine)
session = Session()

print("EJEMPLOS DE CONSULTAS")

print("Ejemplo 8")
print("""Obtener todos los registros de·
la tabla Docente que tengan dentro del valor del atributo ciudad
la cadena "ora" y
el atributo nombre sea diferente de None.
Finalmente que se ordenen por el atributo de la clase Docente nombre""")

docentes = session.query(Docente).filter(Docente.ciudad.like("%ora%"), \
        Docente.nombre!=None).order_by(Docente.nombre).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de todos los Docentes")

print("--------------------------------")
for s in docentes:
    print("%s" % (s))
    print("---------")

print("--------------------------------")
