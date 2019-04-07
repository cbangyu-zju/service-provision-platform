import sys
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""QTreeView {
        outline: 0px;
        background: rgb(47, 64, 78);
    }
    QTreeView::item {
        min-height: 50px;
    }
    QTreeView::item:hover {
        background: rgb(41, 56, 71);
    }
    QTreeView::item:selected {
        background: rgb(41, 56, 71);
    }
    QTreeView::item:selected:active{
        background: rgb(41, 56, 71);
    }
    QTreeView::item:selected:!active{
        background: rgb(41, 56, 71);
    }
    QTreeView::branch:open:has-children {
        background: rgb(41, 56, 71);
    }
    QTreeView::branch:has-siblings:!adjoins-item {
        background: green;
    }
    QTreeView::branch:closed:has-children:has-siblings {
        background: rgb(47, 64, 78);
    }
    QTreeView::branch:has-children:!has-siblings:closed {
        background: rgb(47, 64, 78);
    }
    QTreeView::branch:open:has-children:has-siblings {
        background: rgb(41, 56, 71);
    }
    QTreeView::branch:open:has-children:!has-siblings {
        background: rgb(41, 56, 71);
    }
    QTreeView:branch:hover {
        background: rgb(41, 56, 71);
    }
    QTreeView:branch:selected {
        background: rgb(41, 56, 71);
    }
        """)
    MainWindow = QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
