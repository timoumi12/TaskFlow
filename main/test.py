#!/usr/bin/python3
from models.users import user
from models.tasks import task
from models.workspaces import workspace
import models

models.storage.reload()

# creation of a User
user1 = user(name="alx", email="alx@gmail.com", password="123")
user1.save()
user2 = user(name="anonymous", email="anonymous@gmail.com", password="123")
user2.save()

#workspace
workspace1 = workspace(id_admin=1)
workspace1.save()

user1.workspaces.append(workspace1)
user2.workspaces.append(workspace1)
print(user1.workspaces)
print(user2.workspaces)

#task
task1 = task(title="task", member_id=user1.id, priority="mid", description="/")
task1.save()
