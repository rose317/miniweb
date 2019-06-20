import time

def login():
    return "---login--- welcome to our website-------time: %s" % time.ctime()

def register():
    return "---register--- welcome to our website-------time: %s" % time.ctime()

def profile():
    return "---profile--- welcome to our website-------time: %s" % time.ctime()

def application(env,start_response):
    start_response = ("200 OK",[("content-type","text/html;charset=utf-8")])
    file_name = env["PATH_INFO"]
    if file_name == "/login.py":
        return login()
    elif file_name == "/register":
        return register()
    elif file_name == "/profile":
        return profile()
    else:
        return "not found your page"