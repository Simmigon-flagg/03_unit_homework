# Administrator accounts list
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]


# Build your login functions below
def getCreds():
    userInfo = []
    temp = {}
    username = input("Please Enter you Username: ");
    password = input("Please Enter you Password: ");
    temp["username"] = username
    temp["password"] = password
    userInfo.append(temp)
    return userInfo


def checkLogin(userInfo,adminList):
    loggedIn = None
    message = ""
    username = userInfo[0]['username']
    password = userInfo[0]['password']

    for index in range(0,len(adminList)):
        if username == adminList[index]['username'] and  password == adminList[index]['password']:
            loggedIn = True
            message = "YOU HAVE LOGGED IN!"
            print(message)
            return loggedIn
     
        else:
            loggedIn = False
            message = "Please Try again!"
    return loggedIn

        
  
userInfo = getCreds()
# checkLogin(userInfo,adminList)
loggedIn = checkLogin(userInfo,adminList)
# print(loggedIn)
while loggedIn == False:
    print("---------")
    userInfo = getCreds()
    loggedIn = checkLogin(userInfo,adminList)


# print("YOU HAVE LOGGED IN!")