# Accepts 1 or 2 (1-access, 2-refresh) and returns the desired
def access(number: int):
    with open(r"access.txt", "r") as file:
        for count, line in enumerate(file):
            if count == number:
                return line
            
 

def auth():
    global token, headers
    account = requests.get(get_account, headers=headers) # Checks the need to change tokens (amoCRM has no methods for verification)
    
    if account.status_code == 401: 
        auth = requests.post(access_token, data=data).json()
    
    if 'id' not in account.json():
        access_token, refresh_token = auth['access_token'], auth['refresh_token']
        
        with open(r"access.txt", "w") as file: # Overwrite the file 
            file.write(a_token + '\n' + r_token)
        with open('tmp/restart.txt', 'tw', encoding='utf-8') as f: # Restart
            pass

        token = access(1) # .replace('\n', '') Must have
        headers = {'Authorization': 'Bearer {}'.format(token), 
           'Content-Type': 'application/json'
           }
