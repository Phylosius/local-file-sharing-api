# Local File Sharing API

This is an api for local file sharing.

Forgive for the code quality, I'm still learning :].

I'm open to discussion.

# Installation

## 1. make a local copy

Use git to clone the project to your computer
```shell
git clone https://github.com/Phylosius/local-file-sharing-api.git
```

## 2. install dependencies

First you have to [install python](<https://docs.python.org/3/using/>).

Then create an virtual python environment on the project root

```shell
cd local-file-sharing-api
python -m venv .venv
```

And finally activate the virtual environment

```shell
source .venv/bin/activate
```

After the python environment set, you can now install all the dependencies by running the script `update-dependencies` on the `bin` folder.

```shell
cd bin/
./update-dependencies
```


## 3. set database

### a. database creation

The project use [postgresql](<https://www.postgresql.org/download/>), so you have to install it too.

And create a user and a database to used by the api.

Here's an example scripts for it:

```sql
CREATE USER avocado WITH PASSWORD 'avocadoPOSTGRES0';
CREATE DATABASE file_api_db;
ALTER DATABASE file_api_db OWNER TO avocado;
```

### b. database variables
The project use some environment variables so you have to set them before you can run the project.

Create a file named `.env` on the directory _api/file_api/_.

Here's an example:

```.dotenv
DB_USER='avocado'
DB_PASSWORD='avocadoPOSTGRES0'
DB_NAME='file_api_db'
```

As you see that file specify some info about the postgresql database the api will use.



# Running

For run the project, just run the `run` script on the `bin` directory of the project.

```shell
cd bin
./run
```

# Documentation

- [OpenAPI Specification](<./doc/openapi.yml>)
- Mail me at hei.phylosius@gmail.com for help, with object: "FSA help"