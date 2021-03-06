import requests

# we need to pass a link that downloads the image directly when accessed through the link, to allow the preprocessor to do it's work and extract the image from the url.
data = {
    "url": "https://drive.google.com/u/1/uc?id=1jrlCzVTSbpW86msq6OBvwOzU4ptpiHNm&export=download"
}

# replace the below url with "https://b19qq2whez.execute-api.<REGION>.amazonaws.com/<STAGE-NAME>/<ENDPOINT-NAME>" if you use Amazon API Gateway to expose lambda function as a web-service.
url = "http://localhost:8080/2015-03-31/functions/function/invocations"
results = requests.post(url, json=data).json()
print(results)


# "http://localhost:8080/2015-03-31/functions/function/invocations" url for localhost of the docker container that invoke the lambda function locally.


# Test with this links in the json
# "http://bit.ly/mlbookcamp-pants"

# https://drive.google.com/u/1/uc?id=1ZReTpKMByXsYNRnB2aYaQ3mU6AOtoBgv&export=download

# https://drive.google.com/u/1/uc?id=1jrlCzVTSbpW86msq6OBvwOzU4ptpiHNm&export=download

# https://bit.ly/3eaHwus

# to get more photos that download automatically, and work good with our web service.
# 1- put image on google drive
# 2- get link of sharing for everyone
# 3- use the link to open the photo on a web-browser
# 4- press on the download link in the webpage
# 5- capture the link of the download generated from the google drive, it will be in the shape of the above links from my google drive.
