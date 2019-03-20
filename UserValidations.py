import bcrypt
import userCredentialsDb

class Credentials:
    def __init__(self,userName,password):
        self.userName=userName
        self._password=password

    def verifyUser(self):

        # TODO : verify if email exists in backend if yes compare password with input data
        pwdGenHash = HashFunctions.generateHash(self._password)
        pwdHash=userCredentialsDb.getUserPassword()

        if pwdHash and pwdHash==pwdGenHash:
            return True

        return False

    def registerUser(self):
        # TODO : insert input data to table
        #   first check if usermail exists then insert
        pass
    def resetPassowrd(self):
        # TODO : Check what to do? how to do?
        pass










class HashFunctions:
    def matchHash(inputstring,actualHash):
        byteString = bytes(inputstring, 'utf-8')
        return bcrypt.checkpw(byteString, actualHash)

    def generateHash(inputstring):
        byteString = bytes(inputstring,'utf-8')
        hashedPwd = bcrypt.hashpw(byteString, bcrypt.gensalt())
        return hashedPwd