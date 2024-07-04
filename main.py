from instapy_cli import client

username = "USERNAME"
password = "PASSWORD"
video = "PATH"
caption = "CAPTION"

with client(username, password) as cli:
    cli.upload(video, caption)

