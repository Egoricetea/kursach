import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QDialog, QDialogButtonBox, QLineEdit, QTextEdit
)
from PyQt5.QtCore import Qt

class SupportDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Поддержка")
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        support_label = QLabel("Для получения поддержки, свяжитесь с нами:")
        support_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(support_label)

        contact_label = QLabel("Телефон: +7 (123) 456-78-90\nEmail: support@example.com")
        contact_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(contact_label)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)

        self.setLayout(layout)

class NewOrderDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Создание нового заказа")
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        self.name_label = QLabel("Имя клиента:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.phone_label = QLabel("Телефон клиента:")
        self.phone_input = QLineEdit()
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)

        self.address_label = QLabel("Адрес доставки:")
        self.address_input = QTextEdit()
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)

        self.items_label = QLabel("Список блюд:")
        self.items_input = QTextEdit()
        layout.addWidget(self.items_label)
        layout.addWidget(self.items_input)

        self.notes_label = QLabel("Пожелания клиента:")
        self.notes_input = QTextEdit()
        layout.addWidget(self.notes_label)
        layout.addWidget(self.notes_input)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def get_order_details(self):
        return {
            "name": self.name_input.text(),
            "phone": self.phone_input.text(),
            "address": self.address_input.toPlainText(),
            "items": self.items_input.toPlainText(),
            "notes": self.notes_input.toPlainText(),
        }

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

        # Заголовок
        title_label = QLabel("Добро пожаловать в систему доставки еды")
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
        dialog = NewOrderDialog()
        if dialog.exec_() == QDialog.Accepted:
            order_details = dialog.get_order_details()
            print("Новый заказ:", order_details)

    def view_orders(self):
        print("Просмотр заказов")

    def show_sales_report(self):
        print("Отчет по продажам")

    def show_support(self):
        support_dialog = SupportDialog()
        support_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
