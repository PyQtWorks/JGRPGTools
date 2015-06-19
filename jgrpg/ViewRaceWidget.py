from PyQt5.uic import loadUiType

ui_ViewRaceWidget, ViewRaceWidgetBaseClass = loadUiType('ui/ViewRaceWidget.ui')

import __main__

class ViewRaceWidget(
        ViewRaceWidgetBaseClass,
        ui_ViewRaceWidget
):

    def __init__(self, race):
        super(ViewRaceWidget, self).__init__()

        self.race = race

        self.setupUi(self)

        print("Setting window title")
        self.setWindowTitle(race.name+" (Race)")

        print("Setting name text")
        self.nameValueLabel.setText(race.name)
        
        race.removed.connect(self.close)

    def createCharacter(self):
        print("Create character")
        mw = __main__.main_window
        dialog = mw.createCharacter()
        dialog.selectRaceComboBox.setRace(self.race)
        
    def copyRace(self):
        print("Copy race")
        
    def editRace(self):
        print("edit race")