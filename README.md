<div align="center">
    <h1>📘 TODO</h1>
    <a href="https://github.com/jakuboskera/todo/actions"><img alt="jakuboskera" src="https://img.shields.io/github/workflow/status/jakuboskera/todo/tagged-release?logo=github"></a>
    <a href="https://github.com/jakuboskera/todo/releases"><img alt="jakuboskera" src="https://img.shields.io/github/v/release/jakuboskera/todo?logo=docker"></a>
    <a href="https://hub.docker.com/repository/docker/jakuboskera/todo"><img alt="jakuboskera" src="https://img.shields.io/docker/pulls/jakuboskera/todo?logo=docker"></a>
    <a href="https://opensource.org/licenses/Apache-2.0"><img alt="jakuboskera" src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"></a>
</div>

TODO is a simple web application which displays tasks that "should be done".
These tasks can be created/updated/deleted only via API `/api/v1` using
proper `API Key`. This API is documented with [Swagger](http://swagger.io)
documentation. Purpose of this application is mainly to leverage it as
a basic application which can be then mananaged with IaC/GitOps approach.

Last release is always automatically deployed as live demo in
[Heroku](http://heroku.com) 🚀:

<p align="center">
    <b>https://todo.jakuboskera.dev</b>
</p>

TODO's tasks in live demo are managed via
[TODO Terraform provider](https://registry.terraform.io/providers/jakuboskera/todo/latest)
and Terraform manifests are stored in repository
[jakuboskera/infra/todo](https://github.com/jakuboskera/infra/tree/main/todo).

As you can see, tasks which are defined in this
[Terraform manifest](https://github.com/jakuboskera/infra/blob/main/todo/main.tf)
are same as tasks in live demo.

See
[Manage TODO application via Terraform provider](#-manage-todo-application-via-terraform-provider).

## 📖 TOC

- [📖 TOC](#-toc)
- [🏁 Get started](#-get-started)
- [🎉 Run in docker using docker-compose](#-run-in-docker-using-docker-compose)
  - [⚠️ Prerequisites](#️-prerequisites)
  - [🚀 Install](#-install)
  - [🧹 Cleanup](#-cleanup)
- [😎 Manage TODO application via Terraform provider](#-manage-todo-application-via-terraform-provider)
- [Develop](#develop)

## 🏁 Get started

1. Clone this repo

    ```bash
    git clone git@github.com:jakuboskera/todo.git
    ```

1. Navigate to a folder `todo`

    ```bash
    cd todo
    ```

1. Issue `make` command to see available targets, which you can use

    ```bash
    make
    ```

## 🎉 Run in docker using docker-compose

### ⚠️ Prerequisites

- docker
- docker-compose

### 🚀 Install

```bash
make run
```

### 🧹 Cleanup

```bash
make clean
```

## 😎 Manage TODO application via Terraform provider

There was created a
[TODO Terraform provider](https://registry.terraform.io/providers/jakuboskera/todo/latest)
for this application, which can be used for managing a TODO instance.
So you can create/update/delete a TODO tasks using Terraform manifests.


1. Run TODO application localy using
   [docker-compose](#-run-in-docker-using-docker-compose)
1. Go to <http://localhost:5000> and check that there are no tasks created
1. Create this terraform manifest

    ```hcl
    # main.tf

    terraform {
      required_providers {
        todo = {
          source  = "jakuboskera/todo"
          version = "0.1.0"
        }
      }
    }

    provider "todo" {
      url     = "http://localhost:5000"
      api_key = "12345678"
    }

    resource "todo_task" "coding" {
      text = "Create the best application ever"
    }
    ```

1. Initialize this Terraform project

    ```bash
    terraform init
    ```

1. Create task in TODO application

    ```bash
    terraform apply -auto-approve
    ```

1. Go to <http://localhost:5000> and check if task "Create the best
   application ever" was created
1. Now you can change a text of this task, add another tasks, etc.
1. After that you can delete tasks by

    ```bash
    terraform destroy -auto-approve
    ```

## Develop

This will run application localy using
[SQLite](https://www.sqlite.org/index.html) as database.

```bash
export FLASK_APP=$PWD/main.py
export FLASK_DEBUG=True
export API_KEY=12345678 # used in X-API-KEY header when creating/updating/deleting tasks in API
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
flask run
```

If you will do a changes to DB schema don't forget to run

```bash
flask db migrate
```
