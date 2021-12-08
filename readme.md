# Swatch server using Django framework

---

## Pre-requisites
* Python 3.6.1
* pip 20.3.4
* Docker 19.03.8 `(Optional)`

## How to run

### Using Django

* `pip3 install -r requirements.txt`
* `python3 manage.py runserver 0.0.0.0:8080`

### Using Docker

* `docker build -t swatch/server_django:0.0.1 .`
* `docker run -p 8080:8080 -d swatch/server_django:0.0.1 >> server.pid`

## How to test

* Run following `curl` request in the terminal

`curl -v http://localhost:8080/swatch`

* Expected output

```json
[

    {
        "type":"HSL",
        "syntax":"hsl(164, 75%, 93%)",
        "is_css_compatible":true
    },
    {
        "type":"HSL",
        "syntax":"hsl(29, 88%, 33%)",
        "is_css_compatible":true
    },
    {
        "type":"HSL",
        "syntax":"hsl(121, 72%, 69%)",
        "is_css_compatible":true
    },
    {
        "type":"RGB",
        "syntax":"rgb(161, 25, 95)",
        "is_css_compatible":true
    },
    {
        "type":"RGB",
        "syntax":"rgb(65, 116, 179)",
        "is_css_compatible":true
    }

]
```