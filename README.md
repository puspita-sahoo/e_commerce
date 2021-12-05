

# e_commerce

- Developed an e-commerce Website where the user can add, increase and place the order of items.
- Implemented payment integration system. Implemented the user authentication system.

![Screenshot from 2021-10-02 21-48-09](https://user-images.githubusercontent.com/85501280/135724546-cd91f562-4514-42be-ab14-d5aba4d699fb.png)

## Run Locally


### Clone the project


```bash
  git clone https://github.com/puspita-sahoo/e_commerce.git
```

### Create Environment

```bash
  python3 -m venv env_name
```
### Activate Environment(env)

```bash
  $ souce env/bin/activate
```


## Install all Dependencies


```bash
 $ pip3 install -r requrements.txt
```

## Database Migrations


```bash
 $ python3 manage.py makemigrations

```

```bash
 $ python3 manage.py migrate
## Create Super User


```bash
 $ python3 manage.py createsuperuser
```

## Run Server

```bash
$ python3 manage.py runserver
```

