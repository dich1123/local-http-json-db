# Local JSON DB

Simple variant of DB based on one JSON file over HTTP protocol.

## Description

You can get JSON data from file and replace JSON in that file.

## Getting Started

### Dependencies

* install python 3.7+ version (don't forget to click on 
  ADD TO PATH on the first install window)
  

### Installing

* clone this repo to your local machine
```
git clone [this_repo_link]
```
* get into the folder of this repo via terminal
```
cd repo_folder_path
```
* install requirements from requirements.txt
```
pip3 install -r requirements.txt
```

### Executing program

* get into the folder of this repo via terminal
```
cd repo_folder_path
```
* run main.py
```
python main.py
```
ATTENTION! If you've done everything correct, you should see:
```
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5123/ (Press CTRL+C to quit)
```
WARNING! 
Don't forget to turn off server after your work

## Help

* You can see simple help if you go to [localhost:5123](http://127.0.0.1:5123/)
* To get full JSON record send GET request to [localhost:5123/db](http://127.0.0.1:5123/db)
* To replace full JSON in file send POST request to [localhost:5123/db](http://127.0.0.1:5123/db)
data must be in body

## Authors

DiCh [LinkedIn](https://www.linkedin.com/in/dima-cherenkov-016101193)



_FROM__DICH_WITH__LOVE_