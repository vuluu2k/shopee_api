# Shopee Clone

## Development

1. create venv with python 3.12.0
```cmd
python -m venv venv
```
2. set permission for window with powershell run administrator
```powershell
Set-ExecutionPolicy RemoteSigned
```
3. installing requirements.txt
```cmd
pip install -r requirements.txt
```

4. running app
```cmd
python manage.py runserver
```


## Tricks Tips

### Fix generic migrations in uuid is primary key
    * not call function uuid4()
    * use uuid4 with primary key, it's autocrement key
### Get params with django framework
    * in path call params (arg function)
    * form post call body or form data (request.data)
    * after ? call query (request.GET)
