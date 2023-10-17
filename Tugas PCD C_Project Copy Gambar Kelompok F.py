# Kelas : Pengolahan Citra Digital - C
# Judul : Program Copy Gambar dan Split Channel Piksel Gambar

# Nama Anggota Kelompok F:
# 1. I Kadek Rai Pramana                (2105551094)
# 2. Ni Putu Adnya Puspita Dewi         (2105551099)
# 3. Gusti Ngurah Satya Bagus Partama   (2105551100)
# 4. Dyah Putri Maheswari               (2105551102)

import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QErrorMessage
from PyQt6.QtGui import QImage, QPixmap
from PIL import Image
import io

class ImageWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScaledContents(True)

    def hasHeightForWidth(self):
        return self.pixmap() is not None

    def heightForWidth(self, w):
        if self.pixmap():
            try:
                return int(w * (self.pixmap().height() / self.pixmap().width()))
            except ZeroDivisionError:
                return 0

def resize_image(image_data, max_img_width, max_img_height):
    temp = image_data.copy()
    newSize = (max_img_width, max_img_height)
    temp.thumbnail(newSize)
    return temp

def pixmap_from_cv_image(cv_image):
    bytes_img = io.BytesIO()
    cv_image.save(bytes_img, format='JPEG')
    qimg = QImage()
    qimg.loadFromData(bytes_img.getvalue())
    return QPixmap.fromImage(qimg)

def pesan_error():
    error_dialog = QErrorMessage()
    error_dialog.showMessage('Tidak Ada Gambar')
    error_dialog.exec()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Program Pengolahan Citra Digital Konversi RGB CMY")

        main_layout = QVBoxLayout()
        top_bar_layout = QHBoxLayout()
        image_bar_layout = QHBoxLayout()
        self.source_filename = None
        self.source_image_data = None
        self.result_image_data = None
        self.max_img_height = 500
        self.max_img_width = 800

        select_image_button = QPushButton('Pilih Gambar')
        r_button = QPushButton('Proses R')
        g_button = QPushButton('Proses G')
        b_button = QPushButton('Proses B')
        c_button = QPushButton('Proses C')
        m_button = QPushButton('Proses M')
        y_button = QPushButton('Proses Y')
        copy_button = QPushButton('Copy')

        select_image_button.clicked.connect(self.choose_source_image)
        r_button.clicked.connect(self.process_image_r)
        g_button.clicked.connect(self.process_image_g)
        b_button.clicked.connect(self.process_image_b)
        c_button.clicked.connect(self.process_image_c)
        m_button.clicked.connect(self.process_image_m)
        y_button.clicked.connect(self.process_image_y)
        copy_button.clicked.connect(self.process_image_copy)
        for btn in [select_image_button, r_button, g_button, b_button, c_button, m_button, y_button, copy_button]:
            btn.setFixedHeight(30)
            btn.setFixedWidth(100)

        top_bar_layout.addWidget(select_image_button)
        top_bar_layout.addWidget(r_button)
        top_bar_layout.addWidget(g_button)
        top_bar_layout.addWidget(b_button)
        top_bar_layout.addWidget(c_button)
        top_bar_layout.addWidget(m_button)
        top_bar_layout.addWidget(y_button)
        top_bar_layout.addWidget(copy_button)

        self.source_image = ImageWidget()
        self.result_image = ImageWidget()
        self.source_image.setMaximumSize(self.max_img_width, self.max_img_height)
        self.result_image.setMaximumSize(self.max_img_width, self.max_img_height)

        source_image_layout = QVBoxLayout()
        source_image_layout.addWidget(QLabel("Gambar Original:"))
        source_image_layout.addWidget(self.source_image)

        result_image_layout = QVBoxLayout()
        result_image_layout.addWidget(QLabel("Hasil Gambar:"))
        result_image_layout.addWidget(self.result_image)

        image_bar_layout.addLayout(source_image_layout)
        image_bar_layout.addLayout(result_image_layout)

        bottom_bar_layout = QHBoxLayout()
        self.save_button = QPushButton('Save Hasil Gambar')
        self.save_button.clicked.connect(self.save_as_file)        
        self.save_button.setFixedWidth(300)
        bottom_bar_layout.addWidget(self.save_button)

        main_layout.addLayout(top_bar_layout)
        main_layout.addLayout(image_bar_layout)
        main_layout.addLayout(bottom_bar_layout)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def choose_source_image(self):
        self.source_filename = QFileDialog.getOpenFileName()[0]
        self.source_image_data = Image.open(self.source_filename)
        source_image_resized = resize_image(self.source_image_data, self.max_img_width, self.max_img_height)
        self.data = self.source_image_data.getdata()
        self.source_image.setPixmap(pixmap_from_cv_image(source_image_resized))
        
    def process_image_r(self):
        if self.source_image_data is None:
            pesan_error()
        else:
            self.result_image_data = self.source_image_data.copy()
            self.r = [(d[0], 0, 0) for d in self.data]
            self.result_image_data.putdata(self.r)
            result_image_resized = resize_image(self.result_image_data, self.max_img_width, self.max_img_height)
            self.result_image.setPixmap(pixmap_from_cv_image(result_image_resized))

    def process_image_g(self):
        if self.source_image_data is None:
            pesan_error()
        else:
            self.result_image_data = self.source_image_data.copy()
            self.g = [(0, d[1], 0) for d in self.data]
            self.result_image_data.putdata(self.g)
            result_image_resized = resize_image(self.result_image_data, self.max_img_width, self.max_img_height)
            self.result_image.setPixmap(pixmap_from_cv_image(result_image_resized))
    
    def process_image_b(self):
        if self.source_image_data is None:
            pesan_error()
        else:
            self.result_image_data = self.source_image_data.copy()
            self.b = [(0, 0, d[2]) for d in self.data]
            self.result_image_data.putdata(self.b)
            result_image_resized = resize_image(self.result_image_data, self.max_img_width, self.max_img_height)
            self.result_image.setPixmap(pixmap_from_cv_image(result_image_resized))

    def process_image_c(self):
        if self.source_image_data is None:
            pesan_error()
        else:
            self.result_image_data = self.source_image_data.copy()
            self.c = [(0, d[1], d[2]) for d in self.data]
            self.result_image_data.putdata(self.c)
            result_image_resized = resize_image(self.result_image_data, self.max_img_width, self.max_img_height)
            self.result_image.setPixmap(pixmap_from_cv_image(result_image_resized))
    
    def process_image_m(self):
        if self.source_image_data is None:
            pesan_error()
        else:
            self.result_image_data = self.source_image_data.copy()
            self.m = [(d[0], 0, d[2]) for d in self.data]
            self.result_image_data.putdata(self.m)
            result_image_resized = resize_image(self.result_image_data, self.max_img_width, self.max_img_height)
            self.result_image.setPixmap(pixmap_from_cv_image(result_image_resized))
    
    def process_image_y(self):
        if self.source_image_data is None:
            pesan_error()
        else:
            self.result_image_data = self.source_image_data.copy()
            self.y = [(d[0], d[1], 0) for d in self.data]
            self.result_image_data.putdata(self.y)
            result_image_resized = resize_image(self.result_image_data, self.max_img_width, self.max_img_height)
            self.result_image.setPixmap(pixmap_from_cv_image(result_image_resized))
    
    def process_image_copy(self):
        if self.source_image_data is None:
            pesan_error()
        else:
            self.result_image_data = self.source_image_data.copy()
            self.copy = [(d[0], d[1], d[2]) for d in self.data]
            self.result_image_data.putdata(self.copy)
            result_image_resized = resize_image(self.result_image_data, self.max_img_width, self.max_img_height)
            self.result_image.setPixmap(pixmap_from_cv_image(result_image_resized))

    def save_as_file(self):
        if self.result_image_data is None:
            pesan_error()
        else:
            filename = QFileDialog.getSaveFileName(self, str('Save File'), '', str('Images (*.jpg *.png *.jpeg)'))[0]
            if len(filename) > 0:
                self.result_image_data.save(filename)
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()