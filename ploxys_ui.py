# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ploxys.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image,ImageDraw,ImageFont
from random import randint
import time
import os
import traceback
class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1002, 1084)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.ploxys_image = QtWidgets.QLabel(self.centralwidget)
        self.ploxys_image.setGeometry(QtCore.QRect(30, 140, 900, 900))
        self.ploxys_image.setObjectName("ploxys_image")
        self.numploxyslabel = QtWidgets.QLabel(self.centralwidget)
        self.numploxyslabel.setGeometry(QtCore.QRect(10, 0, 121, 41))
        self.numploxyslabel.setObjectName("numploxyslabel")
        self.numploxys = QtWidgets.QSpinBox(self.centralwidget)
        self.numploxys.setGeometry(QtCore.QRect(150, 10, 71, 22))
        self.numploxys.setMaximum(10000)
        self.numploxys.setObjectName("numploxys")
        self.numfoodlabel = QtWidgets.QLabel(self.centralwidget)
        self.numfoodlabel.setGeometry(QtCore.QRect(260, 0, 121, 41))
        self.numfoodlabel.setObjectName("numfoodlabel")
        self.numfood = QtWidgets.QSpinBox(self.centralwidget)
        self.numfood.setGeometry(QtCore.QRect(400, 10, 71, 22))
        self.numfood.setMaximum(10000)
        self.numfood.setObjectName("numfood")
        self.minlifespanlabel = QtWidgets.QLabel(self.centralwidget)
        self.minlifespanlabel.setGeometry(QtCore.QRect(510, 0, 121, 41))
        self.minlifespanlabel.setObjectName("minlifespanlabel")
        self.minlifespan = QtWidgets.QSpinBox(self.centralwidget)
        self.minlifespan.setGeometry(QtCore.QRect(650, 10, 71, 22))
        self.minlifespan.setMaximum(10000)
        self.minlifespan.setObjectName("minlifespan")
        self.maxlifespanlabel = QtWidgets.QLabel(self.centralwidget)
        self.maxlifespanlabel.setGeometry(QtCore.QRect(10, 50, 121, 41))
        self.maxlifespanlabel.setObjectName("maxlifespanlabel")
        self.maxlifespan = QtWidgets.QSpinBox(self.centralwidget)
        self.maxlifespan.setGeometry(QtCore.QRect(150, 60, 71, 22))
        self.maxlifespan.setMaximum(10000)
        self.maxlifespan.setObjectName("maxlifespan")
        self.numroundslabel = QtWidgets.QLabel(self.centralwidget)
        self.numroundslabel.setGeometry(QtCore.QRect(260, 50, 121, 41))
        self.numroundslabel.setObjectName("numroundslabel")
        self.numrounds = QtWidgets.QSpinBox(self.centralwidget)
        self.numrounds.setGeometry(QtCore.QRect(400, 60, 71, 22))
        self.numrounds.setMaximum(100000)
        self.numrounds.setObjectName("numrounds")
        self.aliveploxyslabel = QtWidgets.QLabel(self.centralwidget)
        self.aliveploxyslabel.setGeometry(QtCore.QRect(790, 0, 111, 41))
        self.aliveploxyslabel.setObjectName("aliveploxyslabel")
        self.roundnumberlabel = QtWidgets.QLabel(self.centralwidget)
        self.roundnumberlabel.setGeometry(QtCore.QRect(820, 40, 71, 41))
        self.roundnumberlabel.setObjectName("roundnumberlabel")
        self.aliveploxys = QtWidgets.QLCDNumber(self.centralwidget)
        self.aliveploxys.setGeometry(QtCore.QRect(920, 10, 64, 21))
        self.aliveploxys.setSmallDecimalPoint(True)
        self.aliveploxys.setObjectName("aliveploxys")
        self.roundnumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.roundnumber.setGeometry(QtCore.QRect(920, 50, 64, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.roundnumber.setFont(font)
        self.roundnumber.setSmallDecimalPoint(True)
        self.roundnumber.setObjectName("roundnumber")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(510, 42, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.directory = QtWidgets.QLineEdit(self.centralwidget)
        self.directory.setGeometry(QtCore.QRect(170, 100, 161, 20))
        self.directory.setText("")
        self.directory.setObjectName("directory")
        self.directorylabel = QtWidgets.QLabel(self.centralwidget)
        self.directorylabel.setGeometry(QtCore.QRect(10, 100, 161, 21))
        self.directorylabel.setObjectName("directorylabel")
        self.frameratelabel = QtWidgets.QLabel(self.centralwidget)
        self.frameratelabel.setGeometry(QtCore.QRect(820, 80, 81, 41))
        self.frameratelabel.setObjectName("frameratelabel")
        self.framerate = QtWidgets.QLCDNumber(self.centralwidget)
        self.framerate.setGeometry(QtCore.QRect(920, 90, 64, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.framerate.setFont(font)
        self.framerate.setSmallDecimalPoint(True)
        self.framerate.setObjectName("framerate")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1002, 21))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)
        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)
        self.start.clicked.connect(self.ploxys)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Ploxys"))
        self.ploxys_image.setText(_translate("main", "TextLabel"))
        self.numploxyslabel.setText(_translate("main", "Initial number of ploxys:"))
        self.numfoodlabel.setText(_translate("main", "Initial number of food:"))
        self.minlifespanlabel.setText(_translate("main", "Initial minimal lifespan:"))
        self.maxlifespanlabel.setText(_translate("main", "Initial maximall lifespan:"))
        self.numroundslabel.setText(_translate("main", "Number of rounds"))
        self.aliveploxyslabel.setText(_translate("main", "Number of ploxys alive:"))
        self.roundnumberlabel.setText(_translate("main", "Round number:"))
        self.start.setText(_translate("main", "Start"))
        self.directorylabel.setText(_translate("main", "Type the data directory\'s name:"))
        self.frameratelabel.setText(_translate("main", "Framerate (fps):"))
        pixmap = QtGui.QPixmap("image.jpg")
        self.ploxys_image.setPixmap(pixmap)
    def ploxys(self):
        try:
            num_ploxys = self.numploxys.value()
            num_foods = self.numfood.value()
            min_lifespan = self.minlifespan.value()
            max_lifespan = self.maxlifespan.value()
            num_rounds = self.numrounds.value()
            def nozero(inteiro):
                if inteiro > 0:
                    return inteiro
                else:
                    return 0
            def sanitize(num):
                cadeia = str(num)
                zeros = 9 - len(cadeia)
                adicao = "0" * zeros
                return adicao + cadeia
            #here the directory is created
            diretorio = self.directory.text()
            os.makedirs(diretorio)
            os.chdir(diretorio)
            data_initial_ploxys = open("data_intial_ploxys.txt","w")
            # here the base image is created
            font = ImageFont.truetype("arial.ttf", 15)
            lol = Image.new("RGB", (900, 900), "white")
            suamae = ImageDraw.Draw(lol)
            # Creating the scenario
            for x in range(1,901):
                for y in range(1,901):
                    if y % 2 == 0 and x % 2 == 0:
                        suamae.point((x,y),"grey")
            lol.save("plot.jpg","JPEG")

            # here the ploxys are creates, each ploxy is a list holding its x, its y , how many roudns it will live, his birthdate and his generation respectively
            ploxys = []
            for i in range(0,num_ploxys):
                tempo = time.time()
                lifespan = randint(min_lifespan,max_lifespan)
                newborn = [randint(1,900),randint(1,900),randint(min_lifespan,max_lifespan),randint(-1 * (lifespan),0),0,randint(1,4)]
                ploxys.append(newborn)
                data_initial_ploxys.write("\n" + str(newborn))
            data_initial_ploxys.close()
            #print (ploxys)

            # the calculation of the average initial ploxys lifespan
            soma = 0
            filhagem = 0
            for ploxy in ploxys:
                soma += ploxy[2]
                filhagem += ploxy[5]
            if num_ploxys > 0:
                media = soma / num_ploxys
                media_filhagem = filhagem / num_ploxys
            else:
                media = 0
                media_filhagem = 0
            # here the inital foods are create, each one is a list holding its position in x and y
            foods = [[randint(1,901),randint(1,901)] for i in range (0,num_foods)]

            # base numbers to calculate the average lifespan of the reproduced ploxys
            soma_reproduzidos = 0
            filhagem_reproduzidos = 0
            count = 0
            data_run_test = open("data_run_teste.txt","w")
            tabela = open("table.txt","w")
            conta = 0

            # the simulation starts
            tempoguit = time.time()
            for i in range (0,num_rounds):
                # the scenario is open and the draw is set
                lol = Image.open("plot.jpg")
                suamae = ImageDraw.Draw(lol)

                # each ploxy moves ramdomly from -5 to 5 pixels in each round, if the ploxy lifespan is over, the ploxy does not goes into the next round
                ploxys = [ [(ploxy[0] + randint(-5,5)) % 900 ,(ploxy[1] + randint(-5,5)) % 900,ploxy[2],ploxy[3], ploxy[4],ploxy[5]] for ploxy in ploxys if ploxy[2] + ploxy[3] > conta]

                #each ploxy is drawn
                for ploxy in ploxys:
                    suamae.text(ploxy,"\\",fill = "red",font = font)

                # it chekcs if any food has been eaten, if it has, the food will be deleted
                for food in foods:
                    eaten = False
                    for ploxy in ploxys:
                        if [ploxy[0],ploxy[1]] == food:
                            eaten = True
                            # the ploxy that ate the food, generates 3 children and a new food is generated
                            for i in range(0,ploxy[5]):
                                ploxys.append([ploxy[0],ploxy[1],ploxy[2] + randint(-5,5),conta,ploxy[4] + 1,nozero(ploxy[5] + randint(-1,1))])
                            foods.append([randint(0,900),randint(0,900)])
                            soma_reproduzidos += ploxy[2]
                            filhagem_reproduzidos += ploxy[5]
                            count += 1
                            data_run_test.write("This ploxy ate and reproduced : " + str(ploxy) + "\n")
                            #print ("Esse ploxy comeu e se reproduziu : " + str(ploxy))
                            break

                    # if the food is not eaten, it is drawn and the simulation goes on
                    if eaten == False:
                        suamae.rectangle([(food[0] - 1, food[1] - 1), (food[0] + 2, food[1] + 2)],"green")
                    else:
                        foods.remove(food)
                #print ("Round number %d, and with %d ploxys alive" % (i,len(ploxys)))
                data_run_test.write("Round number " + str(conta) + " and with " + str(len(ploxys)) + " alive\n")
                tabela.write(str(conta) + " " + str(len(ploxys)) + "\n")
                # saving the image for every round
                lol.save( "main.jpg","JPEG")
                pixmap = QtGui.QPixmap("main.jpg")
                temponow = time.time()
                dif = temponow - tempoguit
                if dif <= (1/30):
                    time.sleep((1/30) - dif)
                self.framerate.display("%.2f" %(1 /(time.time() - tempoguit)))
                tempoguit = time.time()
                self.ploxys_image.setPixmap(pixmap)
                self.aliveploxys.display(len(ploxys))
                self.roundnumber.display(conta)
                conta += 1
                if len(ploxys) == 0:
                    data_run_test.write("The population died")
                    #print ("The population died")
                    break
                QtCore.QCoreApplication.processEvents()
            if count > 0:
                media_reproduzidos = soma_reproduzidos / count
                media_filhagem_reproduzidos = filhagem_reproduzidos / count
            else:
                media_reproduzidos = 0
                media_filhagem_reproduzidos = 0
            data_run_test.close()
            tabela.close()
            data_final_ploxys = open("data_final_ploxys.txt","w")

            # it shows how many ploxys survived, e saves the final image
            soma_sobreviventes = 0
            soma_filhagem = 0
            for ploxy in ploxys:
                soma_sobreviventes += ploxy[2]
                soma_filhagem += ploxy[5]
            if len(ploxys) > 0:
                media_sobreviventes = soma_sobreviventes / len(ploxys)
                media_filhagem_finalistas = soma_filhagem / len(ploxys)
            else:
                media_sobreviventes = 0
                media_filhagem_finalistas = 0
            data_final_ploxys.write("\n".join([str(i) for i in ploxys]))
            data_final_ploxys.close()
            data_final = open("data_final.txt","w")
            data_final.write("The game started with %d ploxys, but ends with %d ploxys.\n" % (num_ploxys,len(ploxys)))
            data_final.write("The average lifespan of the initial ploxys was: %f rounds\n" % media)
            data_final.write("The average lifespan of the reproduced ploxys was: %f rounds\n" % media_reproduzidos)
            data_final.write("The average lifespan of the remaining ploxys is: %f rounds\n" % media_sobreviventes)
            data_final.write("The average number of children per birth of the initial ploxys was: %f children\n" % media_filhagem)
            data_final.write("The average number of children per birth of the reproduced ploxys was: %f children\n" % media_filhagem_reproduzidos)
            data_final.write("The average number of children per birth of the remaining ploxys is: %f children\n" % media_filhagem_finalistas)
            data_final.close()
            os.chdir("..")
        except:
            print("ERROR")
            traceback.print_exc()