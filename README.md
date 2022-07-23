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

#### Project vocabulary
```
R{request}		- REST request (RGET, RPOST), no html render
```
