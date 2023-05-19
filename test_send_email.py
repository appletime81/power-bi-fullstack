import adal
import msal
import requests
import json
from msal import ConfidentialClientApplication

client_id = "4169274b-92fc-4d11-8e35-8114f16d287d"
client_secret = "MBJ8Q~vUCPUdaTDGlTqAs.ency4FtKUG.8pnza2R"
# 值: MBJ8Q~vUCPUdaTDGlTqAs.ency4FtKUG.8pnza2R
# 秘密識別碼: 6551cc7f-243b-41e8-8919-0b0e4331be85
SCOPES = ["Mail.Send"]

def acquire_token_func():
    authority_url = "https://login.microsoftonline.com/DONGHWATelecom.onmicrosoft.com"
    auth_ctx = adal.AuthenticationContext(authority_url)
    token = auth_ctx.acquire_token_with_client_credentials(
        "https://graph.microsoft.com",
        client_id,
        client_secret,
    )
    return token


print(acquire_token_func())



access_token = acquire_token_func()['accessToken']



url = "https://graph.microsoft.com/v1.0/users/sendMail"
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

# print("-" * 25 + " HTML Content " + "-" * 25)
# print(HTML)
# print("-" * 25 + " HTML Content " + "-" * 25)

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
