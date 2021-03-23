Requires a validator.json from google,
as well as sharing the spreadsheet with "client_email"


Look at gspread documentation.

Looks like this
```
{
  "type": "service_account",
  "project_id": "{project_name}"
  "private_key_id": "{goes in here}",
  "private_key": "-----BEGIN PRIVATE KEY-----\{lol}\n-----END PRIVATE KEY-----\n",
  "client_email": "{lol}@.iam.gserviceaccount.com",
  "client_id": "105796253219979919387",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/{urlgoeshere}.iam.gserviceaccount.com"
}
```

Use `pip install -r requirements.txt` to get the requirements for this module.


Quick setup
===
1) Get the following files from xeal:
* authentication.json
2) Paste them in this folder.
3) Run `pip install -r requirements.txt`
4) Run `run.bat`

Quick setup (pipenv)
1) Get the following files from xeal:
* authentication.json
2) Paste them in this folder.
3) Run `pipenv install`
4) Run `run-pipenv.bat`