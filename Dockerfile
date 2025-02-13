FROM postgres:17

ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

COPY sql-scripts /docker-entrypoint-initdb.d/

EXPOSE 5432