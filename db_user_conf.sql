 CREATE ROLE admin WITH PASSWORD'passmin';
 
 CREATE DATABASE star_logistics;
 
 GRANT ALL PRIVILEGES ON DATABASE star_logistics TO admin;
 
 ALTER DATABASE star_logistics OWNER TO admin;
 
 ALTER ROLE admin WITH LOGIN;
