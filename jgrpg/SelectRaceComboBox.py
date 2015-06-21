from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

from jgrpg.model import GlobalData

class SelectRaceComboBox(QComboBox):

    def __init__(self, parent=None):
        super(SelectRaceComboBox, self).__init__(parent)

        self.setModel(QStandardItemModel())

        self.init()

        GlobalData.race_added.connect(self.init)
        GlobalData.race_removed.connect(self.init)
        GlobalData.races_reset.connect(self.init)

    def init(self):
        print("SelectRaceComboBox.init")
        model = self.model()
        model.clear()

        root_item = model.invisibleRootItem()
        for race in GlobalData.races:
            item = QStandardItem(race.name)
            item.setData(race, Qt.UserRole)
            root_item.appendRow(item)
            
    def setRace(self, race):
        count = self.count()        
        for i in range(count):
            if self.itemData(i, Qt.UserRole) is race:
                self.setCurrentIndex(i)
                break
        else:
            print("Couldn't find that race...")

    def race(self):
        """Returns the currently selected race."""
        return self.currentData(Qt.UserRole)
