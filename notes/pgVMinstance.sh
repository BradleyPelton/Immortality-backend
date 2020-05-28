# Ubuntu 18.04 Bionic Beaver
# NOTE- Bionicis the name for 18.04 like mashemellow/KitKat are for android

# FRESH VM
sudo apt-get update
sudo apt-get install htop
sudo apt-get install nano

# SET ROOT PASSWORD
sudo -i passwd

### INSTALLING POSTGRES
# Create the file /etc/apt/sources.list.d/pgdg.list
# ADD THE FOLLOWING LINE TO PGDG.LIST : 
cat 'deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main' >> pgdg.list

# import repository signing key
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
# update the packages list
sudo apt-get update

# install from the , now linked, postgres repo
sudo apt-get install -y postgresql-12

# the postgres user will be created by default
# but the password is unknown to me
# SET THE POSTGRES USER PASSWORD
sudo passwd postgres



### CREATING USER AND GRANTING PERMISSIONS
# step 1
sudo -u postgres psql template1
# step 2 - alter the user 
ALTER USER postgres with encrypted password 'password';
# step 3 - change how users access postgres( peer authentication vs password authentication)
# see https://stackoverflow.com/questions/1471571/how-to-configure-postgresql-for-the-first-time
cd /etc/postgresql/12/main
sudo nano pg_hba.conf
# CHANGE THE LINE for postgres TO md5 INSTEAD OF peer
# step 4 - restart postgres
sudo /etc/init.d/postgresql restart

# step 5 - create a new user, grant it all privleges
sudo createuser -U postgres -d -e -E -l -P -r -s morpheus
# password= pill

# step 6- edit pg_hba.conf again, this time setting local all all (peer -> md5)
cd /etc/postgresql/12/main
sudo nano pg_hba.conf
# step 7 - restart postgres
sudo /etc/init.d/postgresql restart




### ALLOWING ALL CONNECTIONS
# DIDNT WORK(IN THIS ORDER)
# STEP 1 
psycopg2.connect (...)  # without any configurations
# STEP 2 - ADDING FIREWALL RULES
# open all ports to both ingress and egress using GCP firewall rule
# STEP 3 - CHANGING postbres binaries 
cd /etc/postgresql/12/main
echo "listen_addresses = '*'" >> postgresql.conf  # ADDING THIS LINE TO END OF THAT FILE, without >>
echo "host  all  all 0.0.0.0/0 md5" >> pg_hba.conf # ADDING THIS LINE TO END OF THAT FILE, wihout >>
# It allows access to all databases for all users with an encrpyted password
# SEE STACKOVERFLOW: https://stackoverflow.com/questions/32439167/psql-could-not-connect-to-server-connection-refused-error-when-connecting-to


### CREATE DUMMY TABLE FOR TESTING 
psql
create database beta;

CREATE TABLE public.user_credential(
   ID           SERIAL PRIMARY KEY     NOT NULL,
   username       VARCHAR(50)    NOT NULL,
   password       VARCHAR(50)     NOT NULL
);
CREATE TABLE testtable(
   ID           SERIAL PRIMARY KEY     NOT NULL,
   username       VARCHAR(50)    NOT NULL,
   password       VARCHAR(50)     NOT NULL
);

INSERT INTO public.user_credential (username, password)
VALUES
    ('testlocust01', 'Turing123'),
    ('testlocust02', 'Turing123'),
    ('testlocust03', 'Turing123'),
    ('testlocust04', 'Turing123'),
    ('testlocust05', 'Turing123'),
    ('testlocust06', 'Turing123'),
    ('testlocust07', 'Turing123'),
    ('testlocust08', 'Turing123'),
    ('testlocust09', 'Turing123')
;


GRANT ALL PRIVILEGES ON DATABASE "matrixdb" to postgres;


