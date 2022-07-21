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
```
@Model.table
+----+-----------+
| id |    name   |
+----+-----------+
|  1 | Full Name |
+----+-----------+

@ModelElements.table
+----+-----------+------------------------------+
| id |  model_id | model_elementoption_value_id |
+----+-----------+------------------------------+
|  1 |     1     |                1             |
+----+-----------+------------------------------+
|  2 |     1     |                2             |
+----+-----------+------------------------------+
|  3 |     1     |                3             |
+----+-----------+------------------------------+

@ElementOption_Value.table
+----+-------------+---------------+
| id |  element_id | element_value |
+----+-------------+---------------+
|  1 |     1       |     Tanya     |
+----+-------------+---------------+
|  2 |     2       |      von      |
+----+-------------+---------------+
|  3 |     3       |  Degurechaff  |
+----+-------------+---------------+

@Element_Firstname.table
+----+------------+---------+------+
| id |    name    | op_view | op_* |
+----+------------+---------+------+
|  1 | First Name |  input  |  ~!  |
+----+------------+---------+------+
```

#### Project vocabulary
```
R{request}		- REST request (RGET, RPOST), no html render
```
