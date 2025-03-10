from ._anvil_designer import StaffAdminTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StaffAdmin(StaffAdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("HomeAdmin")

  def bookings_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("BookingsAdmin")

  def staff_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("StaffAdmin")

  def Invoices_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("InvoicesAdmin")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('StaffAdmin_copy')
