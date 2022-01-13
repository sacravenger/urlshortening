
# Flask_Url_Shortening

The basic shortening the url applicion. The applicion can generate the shortening url by post the orignal url and redirect the shorted url to orignal.

## Authors

- [@Wayne](https://github.com/sacravenger)


## Installation

Install and update using pip:


```bash
  $ pip install -r requirements.txt
```

Create a sqLite local database.

```bash
   $ python db_init.py
```
Start the flask applicaion 
```bash
   $ flask run
```
## Instructions
After start the applicaion, you can use the endpoint 
/shortenurl to POST the urls request. 

Method
POST

Bequest body example
{"url":"https://flask.palletsprojects.com/en/2.0.x/quickstart/"}

Request body example
{"shorted url": "http://127.0.0.1:5000/12M9"}

If user click the shorted url, the flask applicaion will redirect the browser to the orignal url
