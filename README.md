# ijra kanban board
IJRA - py/flask, vuejs/vuex draggable kanban board (like jira/gitlab issues)

demo:
![demo](./demo.gif)
(You can click on garbage can and it will delete action, just forgot to click it while recording)

Python:
1. ```Clone```
2. ```py -m venv venv```
3. ```pip install requirements.txt```
4. ```py run.py```

JS:

1. Install npm https://docs.npmjs.com/downloading-and-installing-node-js-and-npm#using-a-node-installer-to-install-nodejs-and-npm
2. Install vue-cli https://cli.vuejs.org/guide/installation.html
3. ```cd frontend```
4. ```npm run serve```
5. ```open localhost:8080 from cli```

Expected scenario:
1. Register user on frontend or by postman
2. Login with frontend
3. Add action with button
4. After all actions are added press ```commit actions``` 

#TODO commit actions dynamically
5. Enjoy

Features:
- Backend:
    - REST API
    - jwt token auth
    - CRUD operations through API and frontend
    - serializable models
- Frontend:
    - axios ajax requests to grab data from API
    - storing parsed data, user credentials from API in vuex storage
    - persisted state (store doesn't dissapear after page reload (even after hard refresh))
    - draggable menu of users actions (in hardcoded categories for now)
    - checking jwt token on each frontend route change
    - etc.

Problems:
- Animations are giga clunky (I hate css)
- Categories aren't dynamic (idk how to use ```vue-draggable``` dynamically yet)
- Commiting created actions by user in frontend isn't dynamic ^ 
- vuex storage is shared with all users at the same client(browser)

TODO: 
- fix clunky drag animation (css)
- add permissions on backend
- refactor frontend with dynamic category usage & dynamically save users actions
- implement verifications on user actions on current page (verify token more often than just router-view change)
- process date properly (open calendar component)
