
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:38:15 2016

@author: rabab
"""

import sys
import numpy as np
from scipy import interpolate
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Compositions import isotopes

class MainWindow( QMainWindow ):
    def __init__(self, parent=None) :
        super(MainWindow, self).__init__(parent)
        
        self.setWindowIcon(QIcon('1.png'))
        self.menu= self.menuBar().addMenu("File")
        self.saveas=QAction("Save As",self)
        self.saveas.setShortcut("Ctrl+S")
        self.menu.addActions([self.saveas])
        self.saveas.triggered.connect(self.saveass)
        self.menu2= self.menuBar().addMenu("Help")

        self.help=QAction("About",self)
        self.menu2.addActions([self.help])

        self.help.triggered.connect(self.Help)


        self.widget=Form()
        self.setCentralWidget(self.widget)
        self.setGeometry(350,350,350,550)
        self.setWindowTitle("Triga  Reactor Fuel Elements Compositions")
        
        
    def saveass(self):
        fname=(QFileDialog.getSaveFileName(self,"Save As"))
        f = open(fname[0],'a')
        
        compositions=""

        for i in range(36): 
            compositions=compositions+self.widget.Composition.item(i,0).text()+"   " +self.widget.Composition.item(i,1).text()+"\n"
        
        f.write(compositions)
        f.close()
        
        
    def Help(self):
        reply=QMessageBox.about(self, "About", """This tool generates the istopic compositions of the triga fuel element 
                               for irradiation time up to 42 years and decay times up to 40 years""")
            
class Form(QLabel) :

    def __init__(self,parent=None) :
        super(Form, self).__init__(parent)
        font=QFont('Times',10)
        
        self.Irradiation_Time = QLineEdit(" ")
        
        self.Decay_Time = QLineEdit(" ")
        
        self.Composition = QTableWidget(36,2)
        self.header=QHeaderView(Qt.Horizontal)
        self.header.setFont(font)
        self.Composition.setHorizontalHeaderLabels(["  Isotope" , "   Composition"])
        self.Composition.setHorizontalHeader(self.header)
        

        self.Irradiation=QLabel("Irradiation Time")
        self.Irradiation.setFont(font)
        
        self.Decay=QLabel("     Decay Time ")
        self.Decay.setFont(font)

        self.Isotopic_Density=QLabel("                         Isotopic  Compositions in Atomic/ barn.cm")
        
        self.b=QPushButton("Generate Isotopic Compositions")
        self.b.clicked.connect(self.updateUI)
        
        self.c=QPushButton("Rest")
        self.c.clicked.connect(self.Clear)

        self.Irrad_days =QCheckBox('Days', self)
        self.Irrad_years=QCheckBox('Years', self)
        self.Decay_days= QCheckBox('Days', self)
        self.Decay_years =QCheckBox('Years', self)



        layout1=QHBoxLayout()
        layout1.addWidget(self.Irradiation)
        layout1.addWidget(self.Decay)
        layout2=QHBoxLayout()
        layout2.addWidget(self.Irradiation_Time)
        layout2.addWidget(self.Decay_Time)
        layout3=QHBoxLayout()
        layout3.addWidget(self.Irrad_days)
        layout3.addWidget(self.Irrad_years)
        layout3.addWidget(self.Decay_days)
        layout3.addWidget(self.Decay_years)
        
        layout=QVBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addWidget(self.b)
        layout.addWidget(self.c)
        layout.addWidget(self.Isotopic_Density)
        layout.addWidget(self.Composition)
        self.setLayout(layout)
        
       
    def updateUI(self):
        try:
            r=eval(self.Irradiation_Time.text())
            d=eval(self.Decay_Time.text())
        except Exception:
                    reply = QMessageBox.warning(self, 'Message',
                    "Invalid Entry", QMessageBox.Ok)
                    
        if  self.Irrad_days.isChecked()==True and self.Decay_days.isChecked()==True:
            if r > 1.53300E+04  or d >  14600 :
                reply=QMessageBox.warning(self,'Message',"Irradiation or Decay time exceeds the allowed values ", QMessageBox.Ok)
                
              
                if reply == QMessageBox.Ok:
                    event.accept()
                else:
                    event.ignore() 
            elif r ==0  and d >  0 :
                reply = QMessageBox.warning(self, 'Message',
                "Invalid Entry", QMessageBox.Ok)
    
                if reply == QMessageBox.Ok:
                    event.accept()
                else:
                    event.ignore() 
            else:
                self.compos=isotopes()
                res=self.compos.Gen_compositions(r,d)
                for i in range(36): 
                    self.Composition.setItem(i,0,QTableWidgetItem (str(self.compos.names[i])))
                    self.Composition.setItem(i,1,QTableWidgetItem(str(res[i])))
                    
        elif  self.Irrad_years.isChecked()==True  and self.Decay_years.isChecked()==True:
            if r > 42  or d >  40 :
                reply = QMessageBox.warning(self, 'Message',
                "Irradiation or Decay time exceeds the allowed values ", QMessageBox.Ok)
    
                if reply == QMessageBox.Ok:
                    event.accept()
                else:
                    event.ignore() 
                    
            elif r ==0  and d >  0 :
                reply = QMessageBox.warning(self, 'Message',
                "Invalid Entry", QMessageBox.Ok)
    
                if reply == QMessageBox.Ok:
                    event.accept()
                else:
                    event.ignore() 
            else:
                self.compos=isotopes()
                res=self.compos.Gen_compositions_years(r,d)
                for i in range(36): 
                    self.Composition.setItem(i,0,QTableWidgetItem (str(self.compos.names[i])))
                    self.Composition.setItem(i,1,QTableWidgetItem(str(res[i])))  
                    
        elif self.Irrad_years.isChecked()==True  and self.Decay_days.isChecked()==True:
            if r > 42  or d >  14600 :
                reply = QMessageBox.warning(self, 'Message',
                "Irradiation or Decay time exceeds the allowed values ", QMessageBox.Ok)
    
                if reply == QMessageBox.Ok:
                    event.accept()
                else:
                    event.ignore() 
            if r ==0  and d >  0 :
                reply = QMessageBox.warning(self, 'Message',
                "Invalid Entry", QMessageBox.Ok)
    
                if reply == QMessageBox.Ok:
                    event.accept()
                else:
                    event.ignore() 
            else:
                self.compos=isotopes()
                res=self.compos.Gen_compositions_years_days(r,d)
                for i in range(36): 
                    self.Composition.setItem(i,0,QTableWidgetItem (str(self.compos.names[i])))
                    self.Composition.setItem(i,1,QTableWidgetItem(str(res[i])))
                    
        elif self.Irrad_days.isChecked()==True  and self.Decay_years.isChecked()==True:
            if r >  1.53300E+04  or d >  40 :
                reply = QMessageBox.warning(self, 'Message',
                "Irradiation or Decay time exceeds the allowed values ", QMessageBox.Ok)
    
                if reply == QMessageBox.Ok:
                    event.accept()
                else:
                    event.ignore() 
            if r ==0  and d >  0 :
                reply = QMessageBox.warning(self, 'Message',
                "Invalid Entry", QMessageBox.Ok)
    
                if reply == QMessageBox.Ok:
                    event.accept()
                else:
                    event.ignore()
                    
            else:
                self.compos=isotopes()
                res=self.compos.Gen_compositions_days_years(r,d)
                for i in range(36): 
                    self.Composition.setItem(i,0,QTableWidgetItem (str(self.compos.names[i])))
                    self.Composition.setItem(i,1,QTableWidgetItem(str(res[i])))
 
        
    def Clear(self):
        self.Composition.clearContents()  
        self.Irradiation_Time.clear()
        self.Decay_Time.clear()
        self.Irrad_days.setChecked(False)
        self.Irrad_years.setChecked(False)
        self.Decay_days.setChecked(False)
        self.Decay_years.setChecked(False)
        
   
            


app = QApplication(sys.argv)
mainwindow= MainWindow()
mainwindow.show()
app.exec_()
