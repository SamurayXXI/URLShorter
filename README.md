# URLShorter
Enter your long link to the form. You'll get a short link like *domain.com/UrL*

## Enviroment variable
Set enviroment variable DB_CONNECTION for connection to your database.  
For example:
```
export DB_CONNECTION=sqlite:////tmp/flask.db
```

## Configuration
Application configurations you can set in *shorter/config.py*
| Name | Description | Default |
| --- | --- | --- |
| MIN_LINK_SIZE | Number of the minimum lenght of shorted url. | 3 |
| MAX_GENERATING_ATTEMPTS | Number of tries to generate short url with current length, after that current length will be incremented | 10 |
| DOMAIN_NAME | Set domain for short url to complete link. i.e.: Url "Qwe" with DOMAIN_NAME = mydomain.com will be transformed to "http://mydomain.com/Qwe" | localhost:5000 |

## Launch application
```
python run.py
```

## Start tests
```
pytest
```
