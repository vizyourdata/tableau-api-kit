import tableauserverclient as TSC  
server = TSC.Server('https://10ax.online.tableau.com/')  ##cloud or your full on prem url

token_name="yourPATname"
token_value="yourPATvalue"
sitename = 'yourSitename' 

tableau_auth = TSC.PersonalAccessTokenAuth(token_name, token_value, sitename)
with server.auth.sign_in(tableau_auth):
    all_project_items, pagination_item = server.projects.get()
    project_item = all_project_items[0]
    server.projects.populate_permissions(project_item)
    for x in all_project_items:
        print(x)