# Social Media API

#### Video Link: https://www.youtube.com/watch?v=0sOvCWFmrtA

### Main Notes

#### Python Setup
- check if both the termainal intrepretor(source venv/bin/activate) and vscode intrepretor(view/console/select interpretor) are using the venv python
- it is good to name the venv as the same name for all the project as it is unique to the project


#### Fast API seutp
- Link: https://fastapi.tiangolo.com/tutorial/
- pip: `pip3 install "fastapi[all]"` (this instance all the fastapi alond with dependencies)
- We have http request method @app.get() and the route path inside
- Name of the function doesn't matter. Make it readable and managable that's enough
- Each time we save the file, uvicorn will reload the file (use --reload extension)

#### Postman
Instead of checking the results each time on the browser, We can install postman and check each time. 
![Postman Example](<img/postman_example.png>)
- Even in the course after a while he tested all the endpoints on postman directly. Not using the browser anymore

#### 