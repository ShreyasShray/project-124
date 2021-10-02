from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        "id":1,
        "Name":"Shreyas Shray",
        "Contact":9431268938,
        "done":False
    }
]

@app.route("/add-data", methods = ["POST"])
def add_task():
    if (not request.json):
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        })

        contact = {
            "id":tasks[-1]["id"] + 1,
            "Name":request.json["Name"],
            "Contact":request.json.get("contact", ""),
            "done":False
        }

        tasks.append(contact)
        return jasonify({status:"success", message:"Contact added successfuly"}, 400)

if(__name__ == "__main__"):
    app.run(debug = True)
