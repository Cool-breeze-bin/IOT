from PyQt5 import QtCore, QtWidgets
from PyQt5.QtChart import QChartView,QChart, QLineSeries,QValueAxis
from PyQt5.QtGui import QBrush,QColor,QStandardItemModel,QStandardItem
from PyQt5.QtCore import Qt
import pymysql
import read_sql

def sql_data():
    con = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='py_t_h',
    charset='utf8'
    )
    cur = con.cursor()
    data = read_sql.read(cur)
    return data

class Ui_Dialog(object):
    def setupUi(self, Dialog,data):
        Dialog.setObjectName("Dialog")
        Dialog.resize(835, 621)
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 80, 161, 111))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display(data[1][-1])
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(240, 80, 161, 111))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.display(data[2][len(data[2])-1])
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(40, 250, 391, 311))
        self.tableView.setObjectName("tableView")
        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderLabels(['时间','温度', '湿度'])
        self.tableView.setModel(self.model)
        
        self.graphicsView = QChartView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(490, 90, 311, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QChartView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(490, 350, 311, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 50, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 50, 72, 15))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 210, 111, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(551, 50, 121, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(551, 320, 121, 20))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.setdate(data=sql_data())
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "张恒41905427"))
        self.label.setText(_translate("Dialog", "当前温度："))
        self.label_2.setText(_translate("Dialog", "当前温度："))
        self.label_3.setText(_translate("Dialog", "历史数据"))
        self.label_4.setText(_translate("Dialog", "温度变化曲线"))
        self.label_5.setText(_translate("Dialog", "湿度变化曲线"))
    def setdate(self,data):
        self.chart = QChart()
        self.chart.setBackgroundBrush(QBrush(QColor(255,255,255,100)))  # 设置背景颜色
        self.graphicsView.setChart(self.chart) # 将图表添加到QChartView中
        self.chart1 = QChart()
        self.chart1.setBackgroundBrush(QBrush(QColor(255,255,255,100)))  # 设置背景颜色
        self.graphicsView_2.setChart(self.chart1) # 将图表添加到QChartView中
        # 设置横坐标轴
        self.ax = QValueAxis()
        
        self.ax.setRange(0,30)
        # 设置温度纵坐标轴
        self.ay = QValueAxis()
        self.ay.setRange(min(data[1][-30:]), max(data[1][-30:])) 
        self.ay.setTitleText("温度")
        # 设置湿度纵坐标轴
        self.ay1 = QValueAxis()
        self.ay1.setRange(min(data[2][-30:]), max(data[2][-30:])) # 设置湿度范围
        self.ay1.setTitleText("湿度")
        
        self.chart.addAxis(self.ay, Qt.AlignLeft) # 添加温度纵坐标轴
        self.chart1.addAxis(self.ay1, Qt.AlignLeft) # 添加湿度纵坐标轴
        # 温度曲线
        self.seri = QLineSeries(self.chart)
        self.seri.setName("温度")
        self.chart.addSeries(self.seri)
        j = [i for i in range(30)]
        for i,j in zip(range(len(data[0])-30,len(data[0])),j):
            self.seri.append(j,data[1][i])
        # 湿度曲线
        self.seri1 = QLineSeries(self.chart)
        self.seri1.setName("湿度")
        self.chart1.addSeries(self.seri1)
        k = [i for i in range(30)]
        for i,j in zip(range(len(data[0])-30,len(data[0])),k):
            self.seri1.append(j,data[2][i])
        self.seri.attachAxis(self.ax) # 温度曲线和x轴绑定
        self.seri.attachAxis(self.ay) # 温度曲线和y轴绑定
        self.seri1.attachAxis(self.ax) # 湿度曲线和x轴绑定
        self.seri1.attachAxis(self.ay1) # 湿度曲线和y轴绑定
        self.seri.setPointsVisible(True)
        self.seri1.setPointsVisible(True)
        self.chart.addSeries(self.seri) # chart中添加温度曲线
        self.chart1.addSeries(self.seri1) # chart中添加湿度曲线
        
        # 表格历史数据
        for i in range(len(data[0])):
            self.model.appendRow([
                QStandardItem('%s' % str(data[3][i])),
                QStandardItem('%s' % str(data[1][i])),
                QStandardItem('%s' % str(data[2][i]))
            ])
            
            

from PyQt5.QtChart import QChartView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    
    ui = Ui_Dialog()
    ui.setupUi(Dialog,data=sql_data())
    Dialog.show()
    sys.exit(app.exec_())