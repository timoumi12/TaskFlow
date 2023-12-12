-- create taskflow db
CREATE DATABASE IF NOT EXISTS taskflow;
-- create users table
USE taskflow;
CREATE TABLE users (
id INTEGER AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(128) NOT NULL,
email VARCHAR(128) NOT NULL,
password VARCHAR(128) NOT NULL);
-- create workspaces table
 CREATE TABLE workspaces (
id INTEGER AUTO_INCREMENT PRIMARY KEY,
id_admin INTEGER NOT NULL,
creation_date DATETIME NOT NULL,
code VARCHAR(128) NOT NULL,
FOREIGN KEY (id_admin) REFERENCES users(id));
-- create tasks table
CREATE TABLE tasks (
id INTEGER AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(128) NOT NULL,
member_id INTEGER NOT NULL,
workspace_id INTEGER NOT NULL,
start_date DATETIME NOT NULL,
due_date DATETIME NOT NULL,
priority VARCHAR(20),
description VARCHAR(500),
FOREIGN KEY (workspace_id) REFERENCES workspaces(id),
FOREIGN KEY (member_id) REFERENCES users(id));
-- create conn table 'members'
CREATE TABLE members (
    id_workspace INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    FOREIGN KEY (id_workspace) REFERENCES workspaces(id),
    FOREIGN KEY (id_user) REFERENCES users(id)
);
