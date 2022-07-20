#### Constructor workspace routes
```
# /constructor/c/<int:constructor_id>	- [c]onstructor
# /constructor/g/<int:group_id>		- l[g]roup

/			- GET	request	(list of groups with constructors)

/c			- GET	request	(list of constructors)
/c			- POST	request	(actions with constructors)

/c/{constructor_id}	- GET	request	(get saved work)
/c/{constructor_id}	- POST	request	(save changes)

/c/0			- GET	request	(empty page to work)
/c/0			- POST	request	(redirects to `/c/{constructor_id}`)

/g			- GET	request	(list of constructor groups)
/g			- POST	request	(actions with constructor groups)

/g/{group_id}			- GET	request (list of groups)
/g/{group_id}/{constructor_id}	- GET	request (redirects to `/c/{constructor_id}`)
```
