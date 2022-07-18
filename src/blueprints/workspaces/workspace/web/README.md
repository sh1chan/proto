#### Web workspace routes
```
/		- GET	request	(list of works)

/{web_id}	- GET	request	(get saved work)
/{web_id}	- POST	request	(save changes)

/0		- GET	request	(empty page to work)
/0		- POST	request	(redirects to `/{web_id}`)
```
