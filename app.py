import json
from flask import Flask, redirect, url_for, request
import csv
from datetime import datetime


app = Flask(__name__)


@app.route("/monitor", methods=["POST"])
def monitor():
    if "platformType" not in request.json:
        return {"success": False, "error": "invalid platformType"}

    if "processorType" not in request.json:
        return {"success": False, "error": "invalid processorType"}

    if "numberOfPhysicalCores" not in request.json:
        return {"success": False, "error": "invalid numberOfPhysicalCores"}

    if "operatingSystemRelease" not in request.json:
        return {"success": False, "error": "invalid operatingSystemRelease"}

    if "operatingSystem" not in request.json:
        return {"success": False, "error": "invalid operatingSystem"}

    if "operatingSystemVersion" not in request.json:
        return {"success": False, "error": "invalid operatingSystemVersion"}

    if "currentCpuFrequency" not in request.json:
        return {"success": False, "error": "invalid currentCpuFrequency"}

    if "numberOfLogicalCores" not in request.json:
        return {"success": False, "error": "invalid numberOfLogicalCores"}

    if "numberOfUsers" not in request.json:
        return {"success": False, "error": "invalid numberOfUsers"}

    if "numberOfProcess" not in request.json:
        return {"success": False, "error": "invalid numberOfProcess"}

    if "hostname" not in request.json:
        return {"success": False, "error": "invalid hostname"}

    if "hostip" not in request.json:
        return {"success": False, "error": "invalid hostip"}

    file_object = open(
        request.json["hostip"] + "-" + datetime.now().strftime("%Y%m%d") + ".csv", "a"
    )

    file_object.write(
        "processorType;platformType;numberOfPhysicalCores;operatingSystemRelease;operatingSystem;operatingSystemVersion;currentCpuFrequency;numberOfLogicalCores;numberOfUsers;numberOfProcess;hostname;hostip;\n"
        + request.json["processorType"]
        + ";"
        + request.json["platformType"]
        + ";"
        + request.json["numberOfPhysicalCores"]
        + ";"
        + request.json["operatingSystemRelease"]
        + ";"
        + request.json["operatingSystem"]
        + ";"
        + request.json["operatingSystemVersion"]
        + ";"
        + request.json["currentCpuFrequency"]
        + ";"
        + request.json["numberOfLogicalCores"]
        + ";"
        + request.json["numberOfUsers"]
        + ";"
        + request.json["numberOfProcess"]
        + ";"
        + request.json["hostname"]
        + ";"
        + request.json["hostip"]
        + "\n"
    )
    file_object.write(";")
    # Close the file
    file_object.close()

    return {"success": True, "data": request.json}


if __name__ == "__main__":
    app.run(port=4333, debug=True)
