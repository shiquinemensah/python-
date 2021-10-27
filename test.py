#factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))


#hello world
print('hello world');


#loop
for i in range(5):
    print('A number:', i)

#server

from flask import Flask
app = Flask ('app')

@app.route ('/'):
    def hello_world=();
        return 'hello world';


