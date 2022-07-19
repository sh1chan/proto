#### Constructor workspace routes
```
/			- GET	request	(list of works)

/{constructor_id}	- GET	request	(get saved work)
/{constructor_id}	- POST	request	(save changes)

/0			- GET	request	(empty page to work)
/0			- POST	request	(redirects to `/{constructor}`)
```
