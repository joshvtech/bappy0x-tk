# my-website

[![Website](https://img.shields.io/website?down_color=yellow&down_message=Offline&style=for-the-badge&up_color=green&up_message=Online&url=https%3A%2F%2Fbappy0x.tk)](https://bappy0x.tk)
[![Discord](https://img.shields.io/discord/708323454881103882?logo=discord&style=for-the-badge)](https://discord.gg/Cvc6pVK)

> This is my personal website, *My Diary of Software and Web Development*.

I also host the bulk of the News-Notifier project here too.

![Made With Python](https://forthebadge.com/images/badges/made-with-python.svg)
![Uses HTML](https://forthebadge.com/images/badges/uses-html.svg)
![Uses CSS](https://forthebadge.com/images/badges/uses-css.svg)

Made with Flask (SQLAlchemy, Dance, Login), Psycopg2.

Also uses HTML, CSS, Bootstrap and jQuery.

## Licensing

[![License](https://img.shields.io/github/license/Bappy0X/my-website?style=for-the-badge)](https://github.com/Bappy0X/my-website/blob/master/LICENSE)

Licensed under GPL-3.0

Please try to read and understand the [LICENSE](https://github.com/Bappy0X/my-website/blob/master/LICENSE) document before making any form of edit to this repo.

## Running from Source

If you wish to run this yourself, consider checking the [Procfile](https://github.com/Bappy0X/my-website/blob/master/Procfile).

Clone and install required packages:
```
git clone https://github.com/bappy0x/my-website
cd my-website
pip install -r requirements.txt
```

If you wish to run this on your web server, use terminal and:
```
gunicorn "web:create_app()"
```

If you wish to run this in a development environment, you can simply:
```
python3 web.py
```

If you have any questions, feel free to join the [Discord](https://discord.gg/Cvc6pVK) and ping me with your question.
