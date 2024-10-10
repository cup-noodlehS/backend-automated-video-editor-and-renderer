import os
import requests


class FontInstallationError(Exception):
    pass

def install_font(url):
    """
    Sends a request to the Nexrender API to install a font.
    
    Args:
        url (str): The URL of the font to install
        
    Returns:
        dict: The response from the API
        
    Raises:
        FontInstallationError: If the font installation fails
    """
    nexrender_api_url = os.getenv('NEXRENDER_API_URL')
    if not nexrender_api_url:
        raise FontInstallationError("NEXRENDER_API_URL is not set in environment variables")
    
    install_endpoint = f"{nexrender_api_url.rstrip('/')}/install-font"
    
    try:
        response = requests.post(
            install_endpoint,
            json={'font_url': url},
            timeout=60
        )
        
        if response.status_code != 200:
            raise FontInstallationError(f"Font installation failed with status code {response.status_code}: {response.text}")
        
        return response.json()
        
    except requests.RequestException as e:
        raise FontInstallationError(f"Failed to connect to Nexrender API: {str(e)}")