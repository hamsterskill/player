import pygame
import random
import sys
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QBasicTimer
import player_design

pygame.init()
pygame.mixer.init()


class ExampleApp(QtWidgets.QMainWindow, player_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.directory = ''
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btnfolderopen.clicked.connect(self.browse_folder)
        self.btnshuffle.clicked.connect(self.shuffle)
        self.songs = []
        self.playing = 0
        self.row = 0
        self.tablefolder.doubleClicked.connect(self.play)
        self.btnplayandstop.clicked.connect(self.play_and_stop)
        self.btnprewious.clicked.connect(self.prewioussong)
        self.btnnew.clicked.connect(self.newsong)
        self.timer = QBasicTimer()
        self.step = 0
        #self.timeSlider.valueChanged.connect(print())

    def browse_folder(self):
        self.songs = []
        self.tablefolder.setRowCount(0)
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        row = 0
        if self.directory:
            for file_name in os.listdir(self.directory):  # для каждого файла в директории
                if file_name[-4:] == '.mp3':
                    self.tablefolder.insertRow(row)
                    self.tablefolder.setItem(row, 0, QTableWidgetItem(str(file_name)))
                    song = pygame.mixer.Sound(self.directory + '/' + str(file_name))
                    time = round(song.get_length(), 0)
                    minute = int(time // 60)
                    sec = str(int(time % 60))
                    if int(sec) // 10 == 0:
                        sec = '0' + sec
                    self.songs.append([str(file_name), str(minute) + ':' + sec])
                    self.tablefolder.setItem(row, 1, QTableWidgetItem(str(minute) + ':' + sec))
                    row += 1
        self.linefolder.setText(self.directory)

    def shuffle(self):
        random.shuffle(self.songs)
        row = 0
        for song in self.songs:
            self.tablefolder.setItem(row, 0, QTableWidgetItem(song[0]))
            self.tablefolder.setItem(row, 1, QTableWidgetItem(song[1]))
            row += 1

    def play(self, item):
        if self.directory != '':
            if type(item) != int:
                self.row = item.row()
            self.tabWidget.setCurrentIndex(1)
            pygame.quit()
            pygame.mixer.init()
            pygame.mixer.Sound(self.directory + '/' + self.songs[self.row][0]).play()
            self.playing = 1
            self.linenowplay.setText(self.songs[self.row][0])
            time = self.songs[self.row][1].split(':')
            self.timeSlider.setMaximum(int(time[0]) * 60 + int(time[1]))
            self.timer.start(1000, self)

    def timerEvent(self, e):
        if self.step >= self.timeSlider.maximum():
            self.timer.stop()
            self.newsong()
            return
        self.step = self.step + 1
        self.timeSlider.setValue(self.step)
        minute = str(self.step// 60)
        sec = str(self.step % 60)
        if int(sec) // 10 == 0:
            sec = '0' + sec
        self.linenowplay.setText(self.songs[self.row][0] + ' ' + minute + ':' + sec + '/' + self.songs[self.row][1])
    def play_and_stop(self):
        if self.directory != '':
            pygame.mixer.init()
            if self.playing == 0:
                self.timer.start(1000, self)
                pygame.mixer.unpause()
                self.playing = 1
            else:
                self.timer.stop()
                pygame.mixer.pause()
                self.playing = 0

    def prewioussong(self):
        if self.row == 0 and len(self.songs) != 0:
            self.row = len(self.songs) - 1
        else:
            self.row -= 1
        self.step = 0
        self.play(self.row)

    def newsong(self):
        if self.row == len(self.songs) - 1 and len(self.songs) != 0:
            self.row = 0
        else:
            self.row += 1
        self.step = 0
        self.play(self.row)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


# main()
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()


