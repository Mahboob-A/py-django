from flask import Flask

app = Flask(__name__)

# a minimal flask app to test the docker security vulnerability of  port mapping like: "-p 8080:80 " that maps the container port to the
# 0.0.0.0 to the host making the container accessible from all network interfaces.
# see more here: https://www.linkedin.com/posts/i-mahboob-alam_docker-networking-major-activity-7287140198365192192-ckjt?utm_source=share&utm_medium=member_desktop

@app.route("/app/get-info/", methods=["GET"])
def get_info():
    return "hello, this is working", 200


if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000)
    app.run(host="0.0.0.0", port=5000)
