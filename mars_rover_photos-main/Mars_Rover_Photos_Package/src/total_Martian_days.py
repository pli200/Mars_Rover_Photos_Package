{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
}

from datetime import datetime

def calculate_total_sols(landing_date, launch_date):
    """
    Calculate the total number of Martian days (sols) between the landing date and launch date.

    Parameters:
    - landing_date: Mars Rover landing date in the format 'YYYY-MM-DD'
    - launch_date: Mars Rover launch date in the format 'YYYY-MM-DD'

    Returns:
    - Total number of sols (int) or None if there's an error
    """

    try:
        # Convert landing_date and launch_date strings to datetime objects
        landing_datetime = datetime.strptime(landing_date, '%Y-%m-%d')
        launch_datetime = datetime.strptime(launch_date, '%Y-%m-%d')

        # Calculate the difference in days
        sols_difference = (landing_datetime - launch_datetime).days

        # Return the total number of sols
        return sols_difference

    except ValueError as e:
        # Handle any date parsing errors
        print(f"Date parsing error: {str(e)}")
        return None

