FROM python:3.6

#Install FreeTDS and dependencies for PyODBC
RUN apt-get update && apt-get install -y tdsodbc unixodbc-dev \
 && apt install unixodbc-bin -y  \
 && apt-get clean -y

#Create /etc/odbcinst.ini
RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

#Install pyodbc
RUN pip install --upgrade pip && \
    pip install pyodbc

# Search the path to libtdsodbc.so
RUN dpkg --search libtdsodbc.so
# Search the path to libtdsS.so
RUN dpkg --search libtdsS.so

WORKDIR /usr/src/app
COPY . .
CMD ["python", "sample.py"]
