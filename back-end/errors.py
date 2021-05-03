#-------------------- USERS ---------------------------


class NullParameter(Exception):
    def __str__(self):
        return "Null parameterer given"

class EmailAlreadyExists(Exception):
    def __str__(self):
        return "There is already a user with that email"

class NoAdminChargingSessions(Exception):
    def __str__(self):
        return "No admin charging sessions"

class NotAuthorized(Exception):
    def __str__(self):
        return "Not authorized"

class EmptyUsers(Exception):
    def __str__(self):
        return "Users not found"

class NoPointsForAdminFound(Exception):
    def __str__(self):
        return "No Points found for this admin"

class LogSessionError(Exception):
    def __str__(self):
        return "Problem with new charging session"

class CalculationFailed(Exception):
    def __str__(self):
        return "Calculation Failed"
        
class InvalidUserId(Exception):
    def __str__(self):
        return "Invalid User ID"
class NotValidUser(Exception):
    def __str__(self):
        return "Either you misspelled username or this user is not customer of your company"
class NoStations(Exception):
    def __str__(self):
        return "No Stations Available"

class NoPoints(Exception):
    def __str__(self):
        return "No Points Available"

class NoAvailableContracts(Exception):
    def __str__(self):
        return "No Contracts Available"

class NoCarsFound(Exception):
    def __str__(self):
        return "No Cars Available"

class InvalidContractInput(Exception):
    def __str__(self):
        return "Cannot create new contract, either user id or distributor id not valid"

class InvalidCarInput(Exception):
    def __str__(self):
        return "Not valid input for data of new car"

class InvalidStationInfo(Exception):
    def __str__(self):
        return "Invalid Station Info"

class NotValidInput(Exception):
    def __str__(self):
        return "Not Valid Input"

class BillIssueFailed(Exception):
    def __str__(self):
        return "Bill Issue Failed"

class BillPaymentFailed(Exception):
    def __str__(self):
        return "Bill Payment Failed"

class DeleteContractFailed(Exception):
    def __str__(self):
        return "Delete Contract Failed"
        
class InvalidEmail(Exception):
    def __str__(self):
        return "There is no user with that email"

class WrongCred(Exception):
    def __str__(self):
        return "Wrong Email or Password"

class UserCarNotExist(Exception):
    def __str__(self):
        return "That car does not exists in user's collection"

class UserCarAlreadyExists(Exception):
    def __str__(self):
        return "That car already exists in user's collection"

class NoStationChargingSessions(Exception):
    def __str__(self):
        return "No charging sessions found for this station"

class UserCreationFailed(Exception):
    def __str__(self):
        return "User creation failed"

class UserInfoError(Exception):
    def __str__(self):
        return "User Not Found"

class NotValidPassName(Exception):
    def __str__(self):
        return "Not valid user credentials"

class IncorrectOldPassword(Exception):
    def __str__(self):
        return "Not valid old password"

class IncorrectPassword(Exception):
    def __str__(self):
        return "Not valid password"

class NoChargingSessions(Exception):
    def __str__(self):
        return "No charging sessions"  

class EmptyResponse(Exception):
    def __str__(self):
        return "Empty response from database"

class NoContractsFound(Exception):
    def __str__(self):
        return "No contracts found"  

class FileNotFound(Exception):
    def __str__(self):
        return "File Not Found"

class InvalidCredentials(Exception):
    def __str__(self):
        return "Invalid credentials"

class AdminNotFound(Exception):
    def __str__(self):
        return "Admin Not Found"

class AdminNotValid(Exception):
    def __str__(self):
        return "This administrator does not work for you! Leave him alone you prick!"

class NoAdminsFound(Exception):
    def __str__(self):
        return "No Admins Found"

