import msal
import requests
import json


# Graph Python quick start
# 值: OBC8Q~Z3fnCoR4~q9Wm6zcdpVrWVO9QiF8e2abAl
# 秘密識別碼: 5fb9c3a3-3ad7-41e2-ab23-fe96346ec1da

client_id = "5830434e-26b0-4e69-abf5-9e790dd5c15e"
client_secret = "OBC8Q~Z3fnCoR4~q9Wm6zcdpVrWVO9QiF8e2abAl"


def acquire_token_by_username_password():
    authority_url = "https://login.microsoftonline.com/{0}".format(
        "DONGHWATelecom.onmicrosoft.com"
    )
    app = msal.PublicClientApplication(authority=authority_url, client_id=client_id)
    return app.acquire_token_by_username_password(
        username="DONGHWA17@DONGHWATelecom.onmicrosoft.com",
        password="Vam1874Vam1874",
        scopes=["https://graph.microsoft.com/.default"],
    )


access_token = acquire_token_by_username_password().get("access_token")


url = "https://graph.microsoft.com/v1.0/me/sendMail"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #333;
            margin: 0;
            padding: 0;
        }

        .container {
            background-color: #222;
            max-width: 600px;
            margin: 30px auto;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }

        h1 {
            font-size: 28px;
            color: #fff;
            text-align: center;
            margin-bottom: 30px;
        }

        p {
            font-size: 16px;
            color: #ccc;
            line-height: 1.5;
            text-align: center;
        }

        .btn {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>您被邀請參加午餐聚會！</h1>
        <p>親愛的朋友，我們很高興邀請您參加我們在新開的員工餐廳舉行的午餐聚會。</p>
        <p>這將是一個絕佳的機會，讓我們一起享受美味的食物，並在輕鬆的氛圍中互相交流。</p>
        <p>敬請期待您的光臨！</p>
        <p><a href="#" class="btn btn-primary">確認出席</a></p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"></script>
</body>
</html>
"""


payload = {
    "message": {
        "subject": "Meet for lunch?",
        "body": {"contentType": "HTML", "content": HTML},
        "toRecipients": [{"emailAddress": {"address": "cht_frank@cht.com.tw"}}],
    }
}

# change sender email address
# payload["message"]["from"] = {"emailAddress": {"address": "no-reply@DONGHWATelecom.onmicrosoft.com"}}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 202:
    print("Email sent successfully!")
else:
    print(f"Failed to send email. Status code: {response.status_code}")
    print(response.text)
