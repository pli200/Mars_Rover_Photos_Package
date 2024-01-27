{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
}

import requests

def search_photo_by_id(photo_id, api_key='DEMO_KEY'):
    """
    Search for a Mars Rover photo by its ID.

    Parameters:
    - photo_id: ID of the photo to search for
    - api_key: NASA API key (default is 'DEMO_KEY')

    Returns:
    - Photo data (dict) or None if the photo is not found or an error occurs
    """

    url = f'https://api.nasa.gov/mars-photos/api/v1/photos/{photo_id}'

 
    params = {
        'api_key': api_key,
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
         
            data = response.json()

            
            if 'photo' in data:
                return data['photo']
            else:
                print(f"Photo with ID {photo_id} not found.")
                return None
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
