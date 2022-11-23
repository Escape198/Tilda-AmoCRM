# Tilda-AmoCRM
Example of Webhooks (Tilda) + amoCRM integration 🍪
***
# Configure Tilda
`Site Settings - Forms - Other - Webhooks`

Create Webhooks, where your url is inserted.
Other parameters are not required "Api Method" - off


Note: your view must return 200.
If you use redirects or other methods in your handler - then you won't need Webhooks in your settings, just replace action="your ulr" of Tilda form

# AmoCRM
You will need an access token and a refresh token.
Create app: `Settings - Integrations - Create Integration (External integration)`

Also only the url is specified, the rest is irrelevant

After creating the application you will receive an authorization code (which must be used to get a refresh token in 20 minutes)

>POST /oauth2/access_token

>data = {
  'client_id': client_id, 
  'client_secret': client_secret,
  'grant_type': 'authorization_code',
  'code': code
  }
  
  After that you will get 2 values that need to be stored (in a file or in a database), because they need to be updated once a day
  
