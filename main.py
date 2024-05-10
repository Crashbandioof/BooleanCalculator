from logic import *
def main():
    Application = QApplication([])
    Window = logic()
    Window.show()
    Application.exec()
if __name__ == '__main__':
    main()