import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Система доставки еды")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        title_label = QLabel("Еда, еда:)")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)

        button_layout = QHBoxLayout()

        self.new_order_button = QPushButton("Создать новый заказ")
        self.new_order_button.clicked.connect(self.create_new_order)
        button_layout.addWidget(self.new_order_button)

        self.view_orders_button = QPushButton("Просмотр заказов")
        self.view_orders_button.clicked.connect(self.view_orders)
        button_layout.addWidget(self.view_orders_button)

        self.sales_report_button = QPushButton("Отчет по продажам")
        self.sales_report_button.clicked.connect(self.show_sales_report)
        button_layout.addWidget(self.sales_report_button)

        self.support_button = QPushButton("Поддержка")
        self.support_button.clicked.connect(self.show_support)
        button_layout.addWidget(self.support_button)

        layout.addLayout(button_layout)

        self.orders_table = QTableWidget()
        self.orders_table.setColumnCount(3)
        self.orders_table.setHorizontalHeaderLabels(["Номер заказа", "Имя клиента", "Статус заказа"])
        layout.addWidget(self.orders_table)

        main_widget.setLayout(layout)

    def create_new_order(self):
        print("Создание нового заказа")

    def view_orders(self):
        print("Просмотр заказов")

    def show_sales_report(self):
        print("Отчет по продажам")

    def show_support(self):
        print("Поддержка")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
