import tableauserverclient as TSC  
server = TSC.Server('https://10ax.online.tableau.com/')  ##cloud or your full on prem url

token_name="yourPATname"
token_value="yourPATvalue"
sitename = 'yourSitename' 

tableau_auth = TSC.PersonalAccessTokenAuth(token_name, token_value, sitename)
with server.auth.sign_in(tableau_auth):
    projects = [project for project in TSC.Pager(server.projects)]
    for x in projects:
        print(x)