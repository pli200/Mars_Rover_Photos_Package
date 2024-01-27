{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
}


import requests


    """
the function is used to request the api from NASA with parameter sol=1000

    """


api_key = 'DEMO_KEY'
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

params = {
    'sol': 1000,  # Martian Solar Day
    'api_key': api_key,
}

# Make the GET request
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    
    
    print(data)
else:
    
    print(f"Error: {response.status_code} - {response.text}")
