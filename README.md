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
+----+-----------+---------+------+
| id |    name   | op_view | op_* |
+----+-----------+---------+------+
|  1 | Full Name |   div   |  ~!  |
+----+-----------+---------+------+

@Model_Elements.table
+----+-----------------+---------------------------+
| id | relation(Model) |    relation(Element_*)    |
+----+-----------------+---------------------------+
|  1 |   Model.id(1)   | Element_First_Name.id(1)  |
+----+-----------------+---------------------------+
|  2 |   Model.id(1)   | Element_Middle_Name.id(1) |
+----+-----------------+---------------------------+
|  3 |   Model.id(1)   |  Element_Last_Name.id(1)  |
+----+-----------------+---------------------------+

@Element_First_Name.table
+----+------------+---------+------+
| id |   Value    | op_view | op_* |
+----+------------+---------+------+
|  1 |   Tanya    |  input  |  ~!  |
+----+------------+---------+------+
```

#### Project vocabulary
```
R{request}		- REST request (RGET, RPOST), no html render
```
