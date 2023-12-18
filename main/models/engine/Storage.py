import models
from models.users import user
from models.tasks import task
from models.workspaces import workspace
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base

classes = {"user": user, "task": task, "workspace": workspace}


class Storage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None
    def __init__(self):
        """ init method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format('root', 'password', 'localhost', 'taskflow'))

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    new_dict[obj.id] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def getUserByEmail(self, email):
        """
        Returns the object based on the class name and its USERNAME, or
        None if not found
        """
        all_users = models.storage.all(user)
        #print(all_users)
        for value in all_users.values():
            if (value.email == email):
                return value
        return None

    def getUserById(self, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        all_users = models.storage.all(user)
        #print(all_users)
        for value in all_users.values():
            if (value.id == id):
                return value
        return None

    def getUserWorkspaces(self, uid):
        """returns workspaces for a specific user"""
        user = self.getUserById(uid)
        target_name = user.name.upper() + '_W' + str(uid)
        private_wsp = self.__session.query(workspace).filter_by(name=target_name).one()
        owned_wspaces = self.__session.query(workspace).filter(and_(workspace.id_admin==uid, workspace.name!=target_name)).all()
        return {"memberOf": user.workspaces,
                "private": private_wsp,
                "owned": owned_wspaces}

    def getWorkspaceByCode(self, code):
        """returns the workspace speicified by a unique code"""
        return self.__session.query(workspace).filter_by(code=code).one()

    def getWorkspaceById(self, id):
        """returns the workspace speicified by it's id"""
        return self.__session.query(workspace).filter_by(id=id).one()

    def getWorkspaceTask(self, workspace_id):
        """returns the workspace's tasks"""
        return self.__session.query(task).filter_by(workspace_id=workspace_id).all()

    def addTask(self, **task_data):
        """adds a new task"""
        new_task = task(**task_data)
        new_task.save()
        return ''

    def getWorkspaceMembers(self, workspace_id):
        """retrieves the workspaces members"""
        target_workspace = self.getWorkspaceById(workspace_id)
        return target_workspace.members
    
    def getTaskById(self, task_id):
        """retrieves the task by id"""
        return self.__session.query(task).filter_by(id=task_id).one()
    
    def deleteWorkspace(self, code):
        """deletes workspace"""
        wsp = self.getWorkspaceByCode(code)
        print(wsp.code)
        self.__session.delete(wsp)
        self.__session.commit()

    def deleteTask(self, id):
        """deletes task"""
        task = self.getTaskById(id)
        print(task.title)
        self.__session.delete(task)
        self.__session.commit()

    def updateWorkspace(self, workspace_id, name):
        """updates workspace"""
        wsp = self.getWorkspaceById(workspace_id)
        wsp.name = name
        self.__session.commit()

    def editTask(self, id, edit_data):
        """updates task"""
        task = self.getTaskById(id)
        task.title = edit_data["title"]
        task.priority = edit_data["priority"]
        task.member_id = edit_data["member_id"]
        task.state = edit_data["state"]
        task.description = edit_data["description"]
        self.__session.commit()
