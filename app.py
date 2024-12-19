from flask import Flask, render_template

app = Flask(__name__)

github_repos = {
    'DEEF-Lite-Image-Viewer': {
        'description': 'Сross-platform image viewer.',
        'icon_link': 'static/dliv.ico',
        'version': '2.1',
        'download_link': 'https://github.com/deeffest/DEEF-Lite-Image-Viewer/releases/latest/',
        'github_link': 'https://github.com/deeffest/DEEF-Lite-Image-Viewer/'
    },
    'DEEF-Lite-Media-Player': {
        'description': 'Сross-platform media player.',
        'icon_link': 'static/dlmp.ico',
        'version': '1.2',
        'download_link': 'https://github.com/deeffest/DEEF-Lite-Media-Player/releases/latest/',
        'github_link': 'https://github.com/deeffest/DEEF-Lite-Media-Player/'
    },
    'Youtube-Music-Desktop-Player': {
        'description': 'Turns the YT Music site into a desktop application. ',
        'icon_link': 'static/ytmdp.ico',
        'version': 'v1.14.1',
        'download_link': 'https://github.com/deeffest/Youtube-Music-Desktop-Player/releases/latest/',
        'github_link': 'https://github.com/deeffest/Youtube-Music-Desktop-Player/',
        'sourceforge_link': 'https://sourceforge.net/projects/youtube-music-desktop-player/'
    },
    'Qt-Multimedia-Player': {
        'description': "Turns Qt's Media Player Example into a complete application.",
        'icon_link': 'static/qmp.ico',
        'version': 'v1.0.0',
        'download_link': 'https://github.com/deeffest/Qt-Multimedia-Player/releases/latest/',
        'github_link': 'https://github.com/deeffest/Qt-Multimedia-Player/'
    },
}

news_list = [
    {'title': 'Youtube-Music-Desktop-Player v1.14.1 is Here!', 'date': '17.12.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player v1.14.0 is Here!', 'date': '15.12.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player v1.13.1 is Here!', 'date': '11.12.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'DEEFFEST-SITE v1.0.0 is Here!', 'date': '30.11.2024', 'icon_link': 'static/icon.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.13 update!', 'date': '25.11.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.13-rc1 update!', 'date': '24.11.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Qt-Multimedia-Player is released!', 'date': '09.11.2024', 'icon_link': 'static/qmp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.12.1 update!', 'date': '09.11.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.12 update!', 'date': '27.10.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.11.4 update!', 'date': '16.10.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.11.3 update!', 'date': '09.10.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.11.2 update!', 'date': '04.10.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.11.1 update!', 'date': '28.09.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.11 update!', 'date': '24.09.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'DEEF-Lite-Image-Viewer 3.0-beta update!', 'date': '29.08.2024', 'icon_link': 'static/dliv.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.10.3 update!', 'date': '28.08.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.10.2 update!', 'date': '26.08.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.10.1 update!', 'date': '21.08.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'DEEF-Lite-Media-Player 2.1.1-beta update!', 'date': '16.08.2024', 'icon_link': 'static/dlmp.ico'},
    {'title': 'DEEF-Lite-Media-Player 2.1-beta update!', 'date': '14.08.2024', 'icon_link': 'static/dlmp.ico'},
    {'title': 'DEEF-Lite-Media-Player 2.0-beta update!', 'date': '13.08.2024', 'icon_link': 'static/dlmp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.10 update!', 'date': '10.08.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.9 update!', 'date': '09.08.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.8 update!', 'date': '09.08.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.7.1 update!', 'date': '10.07.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.7 update!', 'date': '23.06.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.6.1 update!', 'date': '16.06.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.6 update!', 'date': '16.06.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.5.2 update!', 'date': '09.06.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.5.1 update!', 'date': '08.06.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.5 update!', 'date': '07.06.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.4.1 update!', 'date': '26.05.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.4 update!', 'date': '23.05.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'DEEF-Lite-Image-Viewer 2.1 update!', 'date': '14.05.2024', 'icon_link': 'static/dliv.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.3 update!', 'date': '12.05.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.2.1 update!', 'date': '08.05.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.2 update!', 'date': '29.04.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'DEEF-Lite-Image-Viewer 2.0.2 update!', 'date': '11.04.2024', 'icon_link': 'static/dliv.ico'},
    {'title': 'DEEF-Lite-Media-Player 1.2 update!', 'date': '10.04.2024', 'icon_link': 'static/dlmp.ico'},
    {'title': 'DEEF-Lite-Image-Viewer 2.0.1 update!', 'date': '03.04.2024', 'icon_link': 'static/dliv.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.1.4 update!', 'date': '02.04.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'DEEF-Lite-Image-Viewer 2.0 update!', 'date': '24.03.2024', 'icon_link': 'static/dliv.ico'},
    {'title': 'DEEF-Lite-Media-Player 1.1 update!', 'date': '17.03.2024', 'icon_link': 'static/dlmp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.1.3 update!', 'date': '03.03.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.1.2 update!', 'date': '01.03.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.1.1 update!', 'date': '26.02.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player 1.1 update!', 'date': '25.02.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'Youtube-Music-Desktop-Player is released!', 'date': '25.01.2024', 'icon_link': 'static/ytmdp.ico'},
    {'title': 'DEEF-Lite-Media-Player is released!', 'date': '17.01.2024', 'icon_link': 'static/dlmp.ico'},
    {'title': 'DEEF-Lite-Image-Viewer 1.3 update!', 'date': '15.01.2024', 'icon_link': 'static/dliv.ico'},
    {'title': 'DEEF-Lite-Image-Viewer 1.2 update!', 'date': '09.01.2024', 'icon_link': 'static/dliv.ico'},
    {'title': 'DEEF-Lite-Image-Viewer 1.1 update!', 'date': '29.12.2023', 'icon_link': 'static/dliv.ico'},
    {'title': 'DEEF-Lite-Image-Viewer is released!', 'date': '09.11.2023', 'icon_link': 'static/dliv.ico'},
    {'title': 'A complete redesign of the site.', 'date': '23.10.2023', 'icon_link': 'static/icon.ico'}
]

skills_list = [
    {'title': 'Python', 'icon_link': 'static/python.png'},
    {'title': 'JavaScript', 'icon_link': 'static/js.png'},
    {'title': 'HTML', 'icon_link': 'static/html.png'},
    {'title': 'CSS', 'icon_link': 'static/css.png'},
    {'title': 'Qt', 'icon_link': 'static/qt.png'},
    {'title': 'QML', 'icon_link': 'static/qml.png'},
    {'title': 'Flask', 'icon_link': 'static/flask.png'}
]

@app.route('/')
def home():
    template = 'home.html'
    projects = [
        {**info, 'title': title}
        for title, info in github_repos.items()
    ]
    return render_template(
        template,
        projects=projects, 
        news_list=news_list, 
        skills_list=skills_list
    )

if __name__ == '__main__':
    app.run(debug=False, port=8088)