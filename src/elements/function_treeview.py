from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QWidget,\
    QLabel, QSpacerItem, QSizePolicy, QHBoxLayout


class ItemWidget(QWidget):
    """自定义的item"""

    def __init__(self, text, badge, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QLabel(text, self, styleSheet='color: white;'))
        layout.addSpacerItem(QSpacerItem(
            60, 1, QSizePolicy.Maximum, QSizePolicy.Minimum))
        if badge and len(badge) == 2:  # 后面带颜色的标签
            layout.addWidget(QLabel(
                badge[0], self, alignment=Qt.AlignCenter,
                styleSheet="""min-width: 50px; 
                    max-width: 80px; 
                    min-height: 38px; 
                    max-height: 38px;
                    color: white; 
                    border:none; 
                    border-radius: 4px; 
                    background: %s""" % badge[1]
            ))


class FunctionTreeWidget(QTreeWidget):

    def __init__(self, *args, **kwargs):
        super(FunctionTreeWidget, self).__init__(*args, **kwargs)
        self.setEditTriggers(self.NoEditTriggers)
        self.header().setVisible(False)
        # 帮点单击事件
        self.itemClicked.connect(self.onItemClicked)

    def onItemClicked(self, item):
        """item单击事件"""
        pass
