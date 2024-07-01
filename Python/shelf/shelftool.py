#iman shirani shelf tool GUI with PySide6 for 3ds max  
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget, QVBoxLayout, QTabWidget, QDockWidget, QLineEdit, QPushButton, QHBoxLayout, QDialog, QLabel, QMenu
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt
import pymxs

# Create functions to add different primitives
def create_box():
    rt = pymxs.runtime
    box = rt.Box()
    rt.redrawViews()

def create_sphere():
    rt = pymxs.runtime
    sphere = rt.Sphere()
    rt.redrawViews()

def create_cylinder():
    rt = pymxs.runtime
    cylinder = rt.Cylinder()
    rt.redrawViews()

# Function to run native 3ds Max commands
def run_max_command(command):
    pymxs.runtime.execute(command)

# Check if a QApplication instance already exists
app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

class TabManagerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tab Manager")
        self.layout = QVBoxLayout(self)

        self.tab_name_input = QLineEdit(self)
        self.layout.addWidget(QLabel("Tab Name:", self))
        self.layout.addWidget(self.tab_name_input)

        self.add_tab_button = QPushButton("Add Tab", self)
        self.add_tab_button.clicked.connect(self.add_tab)
        self.layout.addWidget(self.add_tab_button)

        self.remove_tab_button = QPushButton("Remove Tab", self)
        self.remove_tab_button.clicked.connect(self.remove_tab)
        self.layout.addWidget(self.remove_tab_button)

        self.hide_tab_button = QPushButton("Hide Tab", self)
        self.hide_tab_button.clicked.connect(self.hide_tab)
        self.layout.addWidget(self.hide_tab_button)

        self.unhide_tab_button = QPushButton("Unhide Tab", self)
        self.unhide_tab_button.clicked.connect(self.unhide_tab)
        self.layout.addWidget(self.unhide_tab_button)

        self.shelf_tool = None

    def add_tab(self):
        tab_name = self.tab_name_input.text()
        if tab_name and self.shelf_tool:
            self.shelf_tool.add_tab(tab_name)

    def remove_tab(self):
        tab_name = self.tab_name_input.text()
        if tab_name and self.shelf_tool:
            self.shelf_tool.remove_tab(tab_name)

    def hide_tab(self):
        tab_name = self.tab_name_input.text()
        if tab_name and self.shelf_tool:
            self.shelf_tool.hide_tab(tab_name)

    def unhide_tab(self):
        tab_name = self.tab_name_input.text()
        if tab_name and self.shelf_tool:
            self.shelf_tool.unhide_tab(tab_name)

# Create the main window class
class ShelfTool(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('3ds Max Shelf Tool')

        # Create a layout
        self.layout = QVBoxLayout(self)
        
        # Create a tab widget
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # Create tabs
        self.create_tabs()

        # Tab management
        self.hidden_tabs = {}

        # Add tab manager button
        self.add_tab_manager_button()

    def create_tabs(self):
        # Create the first tab
        tab1 = QWidget()
        tab1_layout = QVBoxLayout(tab1)
        
        toolbar1 = QToolBar("Tab 1 Toolbar")
        tab1_layout.addWidget(toolbar1)
        
        box_action = QAction(QIcon('box_icon.png'), 'Add Box', self)
        box_action.triggered.connect(create_box)
        toolbar1.addAction(box_action)

        sphere_action = QAction(QIcon('sphere_icon.png'), 'Add Sphere', self)
        sphere_action.triggered.connect(create_sphere)
        toolbar1.addAction(sphere_action)

        self.tab_widget.addTab(tab1, "Primitives")

        # Create the second tab
        tab2 = QWidget()
        tab2_layout = QVBoxLayout(tab2)

        toolbar2 = QToolBar("Tab 2 Toolbar")
        tab2_layout.addWidget(toolbar2)
        
        cylinder_action = QAction(QIcon('cylinder_icon.png'), 'Add Cylinder', self)
        cylinder_action.triggered.connect(create_cylinder)
        toolbar2.addAction(cylinder_action)

        # Add native 3ds Max commands
        snap_toggle_action = QAction(QIcon('snap_icon.png'), 'Toggle Snap', self)
        snap_toggle_action.triggered.connect(lambda: run_max_command('actionMan.executeAction 0 "40013"'))
        toolbar2.addAction(snap_toggle_action)

        select_all_action = QAction(QIcon('select_all_icon.png'), 'Select All', self)
        select_all_action.triggered.connect(lambda: run_max_command('actionMan.executeAction 0 "40004"'))
        toolbar2.addAction(select_all_action)

        self.tab_widget.addTab(tab2, "Other Primitives & Commands")

    def add_tab(self, tab_name):
        new_tab = QWidget()
        new_tab_layout = QVBoxLayout(new_tab)
        
        toolbar = QToolBar(f"{tab_name} Toolbar")
        new_tab_layout.addWidget(toolbar)
        
        # Add a sample action
        sample_action = QAction(QIcon('sample_icon.png'), f'Action in {tab_name}', self)
        toolbar.addAction(sample_action)
        
        self.tab_widget.addTab(new_tab, tab_name)

    def remove_tab(self, tab_name):
        index = self.find_tab_index(tab_name)
        if index != -1:
            self.tab_widget.removeTab(index)

    def hide_tab(self, tab_name):
        index = self.find_tab_index(tab_name)
        if index != -1:
            self.hidden_tabs[tab_name] = self.tab_widget.widget(index)
            self.tab_widget.removeTab(index)

    def unhide_tab(self, tab_name):
        if tab_name in self.hidden_tabs:
            widget = self.hidden_tabs.pop(tab_name)
            self.tab_widget.addTab(widget, tab_name)

    def find_tab_index(self, tab_name):
        for i in range(self.tab_widget.count()):
            if self.tab_widget.tabText(i) == tab_name:
                return i
        return -1

    def add_tab_manager_button(self):
        toolbar = QToolBar("Tab Manager Toolbar")
        self.layout.addWidget(toolbar)
        
        tab_manager_action = QAction(QIcon('tab_manager_icon.png'), 'Tab Manager', self)
        tab_manager_action.triggered.connect(self.open_tab_manager)
        toolbar.addAction(tab_manager_action)

    def open_tab_manager(self):
        tab_manager_dialog = TabManagerDialog(self)
        tab_manager_dialog.shelf_tool = self
        tab_manager_dialog.exec()

# Create the dockable widget
class DockableShelf(QDockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('3ds Max Shelf Tool')
        self.shelf_tool = ShelfTool()
        self.setWidget(self.shelf_tool)

# Create and show the dockable window
dockable_window = DockableShelf()

# Find the main window from 3ds Max
for widget in QApplication.instance().topLevelWidgets():
    if isinstance(widget, QMainWindow):
        main_window = widget
        break

# Add the dockable window to the main window
main_window.addDockWidget(Qt.LeftDockWidgetArea, dockable_window)

# Show the dockable window
dockable_window.show()

# Start the event loop if not already running
if not QApplication.instance().exec():
    sys.exit(app.exec())
