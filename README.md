# In order to run the backend
## Set up Local Environment only need to be set up once

```sh
python -m venv myenv
```


## Activate the Environment
```sh
.\myenv\Scripts\Activate.ps1
```

```sh
pip install -r requirements.txt
```

## Create an .env file in the flask-server folder

make sure there is a environment variable named `LOCAL_CONNECTION_URL` which is he connection string to the database

## Run server script

One needs to make sure they are in the activated Environment then run the server.py file

```sh
python server.py
```
