# Usa una imagen oficial de Python como imagen base
FROM python:3.12

# Establece un directorio de trabajo
WORKDIR /mentalia

# Copia los archivos de requisitos y los instala
COPY requirements.txt /mentalia/
RUN pip install -r requirements.txt

# Copia el resto del código fuente de la aplicación
COPY app/ /mentalia/

COPY datos_examenes_completo.json /mentalia/datos_examenes_completo.json

# Expone el puerto que Django utilizará
EXPOSE 8007

# Ejecuta el servidor de Django
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
