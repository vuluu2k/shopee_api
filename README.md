# Shopee Clone

## Development

1. set permission for window with powershell run administrator
```cmd
# For Window
Set-ExecutionPolicy RemoteSigned
```

2. create venv with python 3.12.0
```cmd
python -m venv venv
```

3. activate venv
```cmd
# MacOs or Linux
source ./venv/bin/activate

# Window <PowerShell, Bash, etc>
./venv/Scripts/active
```

4. installing requirements.txt
```cmd
pip install -r requirements.txt
```

5. running app
```cmd
python manage.py runserver
```


## Tricks Tips

### Fix generic migrations in uuid is primary key
    * not call function uuid4()
    * use uuid4 with primary key, it's auto generate key 128bit unique
### Get params with django framework
    * in path call params (arg function)
    * form post call body or form data (request.data)
    * after ? call query (request.GET)
