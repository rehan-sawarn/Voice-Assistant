import requests
key = "API_KEY"
api_address="http://newsapi.org/v2/top-headlines?country=in&apiKey="+key

json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(5):
        ar.append("Number "+str(i+1)+", "+ json_data['articles'][i]['title']+".")
        
    return ar

