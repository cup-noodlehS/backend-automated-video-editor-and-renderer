import requests
from django.conf import settings


nexrender_api_url = getattr(settings, 'NEXRENDER_API_URL', None)

class FontInstallationError(Exception):
    pass

class VideoRenderingError(Exception):
    pass

def install_font(url):
    """
    Install a font from a URL to the Nexrender server
    """
    print("Installing font")
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


def render_video(template_uri, composition_name, assets, priority=0):
    """
    Render a video using the Nexrender server. 
    **Returns** the **jobId** of the rendering job
    """
    print("Rendering video")
    if not nexrender_api_url:
        raise VideoRenderingError("NEXRENDER_API_URL is not set in environment variables")
    
    render_endpoint = f"{nexrender_api_url.rstrip('/')}/create-render"

    try:
        response = requests.post(
            render_endpoint,
            json={
                'template_uri': template_uri,
                'composition_name': composition_name,
                'assets': assets,
                'priority': priority
            },
            timeout=60
        )

        if response.status_code != 200:
            raise VideoRenderingError(f"Video rendering failed with status code {response.status_code}: {response.text}")
        
        return response.json().get('jobId')
    
    except requests.RequestException as e:
        raise VideoRenderingError(f"Failed to connect to Nexrender API: {str(e)}")

# def get_render_job_details(job_id)