import sys
import requests
import webbrowser
import urllib.request
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QMessageBox,QLineEdit,QLabel,QDialog
from PyQt5.QtGui import QIcon,QFont


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.draw()

    def lyric(self):

        url = "https://genius.p.rapidapi.com/search"
        querystring = {"q": self.line.text()}
        headers = {
            'x-rapidapi-host': "genius.p.rapidapi.com",
            'x-rapidapi-key': "299b6e1362msh82f721abaa64c3fp158cb4jsnc2b6a4dee3cb"
        }

        def connect(host='http://google.com'):
            try:
                urllib.request.urlopen(host)  # Python 3.x
                return True
            except:
                return False
        internet=connect()
        if not internet:
            self.window = ResultWin('No internet. Please connect to internet to use the app!',45)
            self.window.show()
        else:
            try:
                response = requests.get(url, headers=headers, params=querystring)
                js = response.json()
                a = 1
                ans=''
                for i in js['response']['hits']:
                    ans =ans + '{}. {} \n'.format(a, i['result']['full_title'])
                    a = a + 1

                self.window=ResultWin(ans,js)
                self.window.show()

            except:
            #self.btn.setText('error')
                self.window = ResultWin('',15)
                self.window.show()


    def draw(self):

        intro=QLabel(self)
        intro.setText("Welcome to the Genius lyrics app.\nThis app uses API hosted by the Genius Systems.\nYou can search songs of your favorite artist here.")
        intro.move(100,50)
        intro.setFont(QFont('Times' , 20))
        intro.adjustSize()

        self.lbl=QLabel(self)
        self.lbl.setText("Enter your search:")
        self.lbl.move(100,175)
        self.lbl.setFont(QFont('Times',14))

        self.line = QLineEdit(self)
        self.line.resize(250, 25)
        self.line.move(100, 210)
        self.line.returnPressed.connect(self.lyric)

        self.btn=QPushButton('Find lyrics',self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100,250)
        self.btn.clicked.connect(self.lyric)

        self.qui=QPushButton('Quit',self)
        self.qui.clicked.connect(QApplication.instance().quit)
        self.qui.resize(self.qui.sizeHint())
        self.qui.move(200,250)



        self.setWindowTitle('Lyrics')
        self.resize(900,500)
        self.setWindowIcon(QIcon('logo.png'))
        self.show()



    def closeEvent(self, event):
        reply=QMessageBox.question(self,'Quit','Are you sure you want to Quit?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# -------------     NEW WINDOW        -----------------
class ResultWin(QWidget):
    def __init__(self,text,json):
        super().__init__()
        self.js=json
        self.result(text,json)
    def openlink(self):

        if not self.line.text() == "":
            if int(self.line.text()) > 10:
                pass
            elif self.js['response']['hits'][int(self.line.text())-1]['result']['lyrics_state'] == 'complete':
                link = self.js['response']['hits'][int(self.line.text())-1]['result']['url']
                webbrowser.open_new_tab(link)
            else:
                nolyric=QDialog(self)
                nolyric.setWindowTitle('Sorry')
                lbl=QLabel(self)
                lbl.setText('Sorry lyrics of this song are not avalaible..')

    def closewin(self):
        self.window().close()
    def result(self,text,json):
        if text=='':
            res = QLabel(self)
            res.setText('No result found.')
            res.move(100, 100)
            res.adjustSize()
        else:
            intro=QLabel(self)
            intro.setText('Your search results-:')
            intro.move(100,50)
            intro.setFont(QFont("Arial",25))

            res=QLabel(self)
            res.setText(text)
            res.move(100,100)
            res.setFont(QFont('Times',15))
            res.adjustSize()

            reslbl=QLabel(self)
            reslbl.setText("Enter the song number:")
            reslbl.move(100,350)
            reslbl.setFont(QFont('Times',15))
            reslbl.adjustSize()

            self.line = QLineEdit(self)
            self.line.resize(250, 25)
            self.line.move(100, 375)
            self.line.returnPressed.connect(self.openlink)

            self.get=QPushButton('Search lyrics',self)
            self.get.resize(self.get.sizeHint())
            self.get.move(100,425)
            self.get.clicked.connect(self.openlink)

            self.back=QPushButton("Back",self)
            self.back.resize(self.back.sizeHint())
            self.back.move(185,425)
            self.back.clicked.connect(self.closewin)


        self.setWindowTitle('Result')
        self.resize(900, 500)
        self.setWindowIcon(QIcon('logo.png'))

        self.show()




def main():
    app=QApplication(sys.argv)
    win=MainWin()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
