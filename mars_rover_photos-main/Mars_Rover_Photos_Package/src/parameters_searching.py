{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
}



import requests

def get_mars_rover_photos(sol, api_key='DEMO_KEY'):
    """
    Retrieve Mars Rover photos based on the provided parameters.

    Parameters:
    - sol: Martian Solar Day
    - api_key: NASA API key (default is 'DEMO_KEY')

    Returns:
    - List of photo data (dict) or None if there's an error
    """

   
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

    params = {
        'sol': sol,
        'api_key': api_key,
    }

    try:
        response = requests.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            
            data = response.json()

            return data.get('photos', [])
        else:
           
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {str(e)}")
        return None







    
