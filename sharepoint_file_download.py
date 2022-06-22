#################################
!pip install py-topping
!pip install git+https://github.com/vgrem/Office365-REST-Python-Client.git


#################################
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.file import File

app_settings = {
    'url': 'https://levi.sharepoint.com/sites/LSAMPIM/',
    'client_id': 'd1a182a5-05db-41d1-8df2-091c0dbdd963',
    'client_secret': 'qEYU9S1T1ydArcCtdet7LXrTjtoGmw3qHSOcAI2OE7c=',
}

ctx_auth = AuthenticationContext(url=app_settings['url'])
ctx_auth.acquire_token_for_app(
    client_id=app_settings['client_id'], client_secret=app_settings['client_secret'])

ctx = ClientContext(app_settings['url'], ctx_auth)

download_path = r'\\Sfooa11\forecast\LSA P&A\Team LSA\Documentation\Prabhu - TEST\Dockers Reporting- Prabhu TEST.xlsx'
file_url = "/sites/LSAMPIM/LSA Reporting Team/TEST - Prabhu/Dockers Reporting- Prabhu TEST.xlsx"
with open(download_path, "wb") as local_file:
    file = ctx.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
