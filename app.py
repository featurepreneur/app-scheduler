from flask import Flask
from flask_apscheduler import APScheduler

app  = Flask(__name__)
scheduler = APScheduler()

PORT = 5000

@app.route("/") 

def scheduledTask():
    print("Sample Scheduled task")
    

if __name__ == "__main__":
    scheduler.add_job(id = 'Scheduled task' , func = scheduledTask, trigger = 'interval', seconds = 5)
    scheduler.start()
    app.run(debug = True,host="0.0.0.0" , port = PORT)
