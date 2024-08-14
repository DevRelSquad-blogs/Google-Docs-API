# Google Docs API Automation

This project demonstrates how to use the Google Docs API to automate reading and writing data in Google Docs Documents using Python.

## Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/Google-Docs-API.git
```

### Navigate to the Project Directory

```bash
cd Google-Docs-API
```

### Install Required Libraries

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Set Environment Variable
Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of your service account key:

```bash
set GOOGLE_APPLICATION_CREDENTIALS=path\to\your\service-account-file.json
```

## Usage

### Read Data from Google Docs
Run the Python script read.py to read data from your Google Docs:

```bash
python read.py
```

### Create Google Docs
Run the script to create Docs:

```bash
python create_doc.py
```
