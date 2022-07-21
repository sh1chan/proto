# sh1chan - Shinigami Chan (proto projects)
Blueprint `constructor` is the main project, others will be created as a utils

#### Blueprints
- [ ] Root		- Root (static) Pages and Files
	- [ ] Main
	- [ ] About
- [ ] Auth		- Authentication Pages
	- [ ] Register
	- [ ] Confirm
	- [ ] Login
- [ ] Services		- Random services
	- [ ] Servers
	- [ ] Parsers
- [ ] Applications	- Random applications
	- [ ] Chats
	- [ ] Bookmarks
	- [ ] Accounts
- [ ] Workspaces	- Widgets
	- [ ] constructor

#### Dependencies
```bash
$ pip -V	# pip 22.1.1
$ python -V	# Python 3.10.4
```

#### Project structure
```
$ tree -d -I '__pycache__'
.
├── applications
│   └── app
│       ├── accounts
│       ├── bookmarks
│       └── chats
├── auth
├── root
├── services
│   └── service
│       ├── parsers
│       └── servers
└── workspaces
    └── workspace
        └── constructor
```

#### SQL Database Structure
```python3
class Model:
	id	= 0
	name	= 'model_0'

class Element_*:
	id		= 0
	name		= 'element_0'
	*options	= '\\'

class Model_Elements:
	id			= 0
	model_id		= 0
	model_element_id	= 0

# Element Example
class Element_FullName(db.Model):
	id		= 0
	name		= 'Full Name'
	first_name	= 'Tanya'
	middle_name	= 'von'
	last_name	= 'Degurechaff'
```

#### Project vocabulary
```
R{request}		- REST request (RGET, RPOST), no html render
```
