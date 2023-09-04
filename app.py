import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '0.0.0.0:1234'

def reload_page():
    webview.reload()

app = QApplication(sys.argv)
window = QMainWindow()

webview = QWebEngineView()
webview.setUrl(QUrl("https://threejs.org/examples/webgl_animation_skinning_blending"))

# Enable JavaScript for the web view
web_settings = webview.settings()
web_settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)


# Create a refresh action in the application's menu
refresh_action = QAction("Refresh", window)
refresh_action.triggered.connect(reload_page)
window.menuBar().addAction(refresh_action)

window.setCentralWidget(webview)
window.show()

sys.exit(app.exec_())
