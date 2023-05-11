import requests
import json

access_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IjBCUEhMX2VSMFZERjlqVnNmZHNLdFlpeWI4ZVVlR1dyR2pibkp3N3pESUUiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC81ZTFkNTQ0OC1jNDAwLTQwZmYtYmU4Mi03NDAyMzE0NDgxZWEvIiwiaWF0IjoxNjgzNzc0MTQwLCJuYmYiOjE2ODM3NzQxNDAsImV4cCI6MTY4Mzg2MDg0MCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhUQUFBQXBPQ0d6aEVYcmkwRVJhVHEzbXZZSnI5ZnJYOVM5VVkrbVdDaGhEL29ZZ1FZdnZFUnFmTks3UlNwK3ZXS0VNSFgiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMTQuNDQuMjAwLjYxIiwibmFtZSI6ImN0Y2hvdyIsIm9pZCI6ImQ4MzZmZTNiLWFkNDgtNGViNC1iODY2LTljYmQ4ZDgxODU2YSIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMTA1RDhBOUQ2IiwicmgiOiIwLkFYRUFTRlFkWGdERV8wQy1nblFDTVVTQjZnTUFBQUFBQUFBQXdBQUFBQUFBQUFCeEFNTS4iLCJzY3AiOiJvcGVuaWQgcHJvZmlsZSBVc2VyLlJlYWQgZW1haWwgTWFpbC5TZW5kIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoieGRJd01LVHJ5ZlFPR0JscXBkQXJJYXhSZmd3bHRVMGdpTzFFS1NkRlBHNCIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJBUyIsInRpZCI6IjVlMWQ1NDQ4LWM0MDAtNDBmZi1iZTgyLTc0MDIzMTQ0ODFlYSIsInVuaXF1ZV9uYW1lIjoiY3RjaG93QERPTkdIV0FUZWxlY29tLm9ubWljcm9zb2Z0LmNvbSIsInVwbiI6ImN0Y2hvd0BET05HSFdBVGVsZWNvbS5vbm1pY3Jvc29mdC5jb20iLCJ1dGkiOiJvZTVPM3dYM3RVdUoxMHVPYU5SRkFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiI4WGNvR0hJZFFfWW9xa3BMTzhvdFA4ZHBWc3A1WXNhSGZRMEdNM3VMNXg4In0sInhtc190Y2R0IjoxNjA4NTU3NjE3fQ.kcMtUnQMuch-u5L2jKxm1HAjbdso_efVxXqMcLQp4S5IpkJqmB6FkU6qGljGwkKW1V8Rk0yvi4hGV5azO3Iy4dYFc7KXMgpVAkL7-3kgmtUR73OxWRhZRvfA9ASL6b059Ogr1i-z7M0-RmnLzhBvAJCWvhAGDF7rDoBpeZNb_zKtcBT18raVSG-CQxYhCyawQlv31c_OkA87TsGtfeAZ0eRppFpDaJ2QA97T7hl-sECBJK7Ii18KfMLgRTpWaPACWfN-LoZ4ib1g0662oLMLzBjn7RGOaoFZvCwqUrQNwGNV9eDCtA8nEGlqsS8D3uFHylzfHhIV1hJUIMZsykyhrw"

url = "https://graph.microsoft.com/v1.0/me/sendMail"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
HTML="""
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

print('-' * 25 + ' HTML Content ' + '-' * 25)
print(HTML)
print('-' * 25 + ' HTML Content ' + '-' * 25)

payload = {
    "message": {
        "subject": "Meet for lunch?",
        "body": {
            "contentType": "HTML",
            "content": HTML
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "address": "ylc@cht.com.tw"
                }
            }
        ]
    }
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 202:
    print("Email sent successfully!")
else:
    print(f"Failed to send email. Status code: {response.status_code}")
    print(response.text)
