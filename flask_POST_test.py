
"""
# list mac processes using a port
lsof -i -P | grep -i "listen" 

# list mac processes using port 5000
lsof -i -P | grep -i "listen" | grep -i 5000


"""


from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"



@app.route('/users', methods = ['GET', 'POST']) 
def show_input_data():

	# extract json, print it and return it
	user_data = request.get_json() 

	user_key = user_data['key']
	if user_key == 'a random key TO CHANGE':

		print(f'user_data: {user_data}')
		res = {'output': f'user password is {user_data["key"]} and you may continue'}
		return jsonify(res)

	else:
		res = {'output': 'Key failure. Sorry, you are not one of us'}
		return jsonify(res)


if __name__ == '__main__':
	app.run(debug = True)



"""
## Test queries. First one should fail password check, and second one should pass

curl --header "Content-Type: application/json"  --request POST  --data '{"username":"tutorials","key":"secret"}'  http://127.0.0.1:5000/users

curl -X POST -H "Content-Type: application/json" \
	-d '{"name": "linuxize", "key": "a random key TO CHANGE"}' \
	http://127.0.0.1:5000/users


"""
