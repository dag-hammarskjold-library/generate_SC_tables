To run this after downloading it, you will have to take the following steps:

>> Install your virtual environment, e.g.: virtualenv venv
>> Activate your virtual environment. 
    On Windows: .\venv\Scripts\activate
>> Install your dependencies from the included requirements file: 
    pip install -r requirements.txt
>> Copy config_sample.py to config.py and edit it to include your database connection details.
>> Set your local FLASK_APP environment variable. On Windows:
    set:FLASK_APP="generate_SC_table.py"
>> Run the application: flask run