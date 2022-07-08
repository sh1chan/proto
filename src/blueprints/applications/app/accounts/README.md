The idea is about to collect all accounts in one place (page)

Yep, You can collect your own or others accounts

#### Application routes
```
/	- GET	request (all created profiles)

/profile/{profile_id}	- GET	request (created profile by id), 0 is to create a new one
/profile/{profile_id}	- POST	request (profile_id=0, create a new profile)

/account_options/{account_id}	- RGET	request (account options by account_id)

# WIDGETS (TODO)

/account/{account_id}				- RGET	request (account with options)
/profile_account/{profile_id}/{account_id}	- RGET	request (profile account with options)
```
