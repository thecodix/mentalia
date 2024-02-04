# Usa una imagen oficial de Python como imagen base
FROM python:3.12

# Set the current working directory to root
WORKDIR /

# Copy the data file to the root directory of the container
COPY data/migration_data.json .

# Establece un directorio de trabajo
ARG APP_HOME=/app
WORKDIR $APP_HOME

# Copia los archivos de requisitos y los instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el resto del código fuente de la aplicación
COPY . .


# Expone el puerto que Django utilizará
EXPOSE 8007

# Ejecuta el servidor de Django
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
