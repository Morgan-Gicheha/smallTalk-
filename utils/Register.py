import json

def process_registration(RequestDetails):
    UniqueID = ""; IMEI = ""; CodeBase = ""; MobileNumber = ""; NetworkCountry = ""; OTPType = ""; FullName = ""; PIN = ""; EMailID = ""; Interests = ""; InAppID = ""

    JSONData = RequestDetails

    UniqueID = JSONData["UniqueID"]
    IMEI = JSONData["IMEI"]
    CodeBase = JSONData["CodeBase"]
    MobileNumber = JSONData["MobileNumber"]
    NetworkCountry = JSONData["NetworkCountry"]
    OTPType = JSONData["Register"]["OTPType"]
    FullName = JSONData["Register"]["FullName"]
    PIN = JSONData["Register"]["PIN"]
    EMailID = JSONData["Register"]["EMailID"]
    Interests = JSONData["Register"]["Interests"]
    InAppID = JSONData["Register"]["InAppID"]

    ResponseData = {
        "RequestID": "REGISTER",
        "UniqueID": UniqueID
    }

    json_response = json.dumps(ResponseData)

    return ResponseData