#################################
!pip install py-topping
!pip install git+https://github.com/vgrem/Office365-REST-Python-Client.git


#################################
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.file import File

app_settings = {
    'url': 'site of your sharepoint',
    'client_id': 'secret id',
    'client_secret': 'secret code',
}

ctx_auth = AuthenticationContext(url=app_settings['url'])
ctx_auth.acquire_token_for_app(
    client_id=app_settings['client_id'], client_secret=app_settings['client_secret'])

ctx = ClientContext(app_settings['url'], ctx_auth)

download_path = r'file location with name'
file_url = "site file location with name"
with open(download_path, "wb") as local_file:
    file = ctx.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
