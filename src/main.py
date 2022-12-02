from taipy.gui import Gui
from pages import home
import os


gui = Gui(page=home.page).run(
    title="Demo Logistic Regression",
    port=os.environ.get("PORT", "8000"),
)
