from ._anvil_designer import MovieDisplayTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..MovieEdit import MovieEdit

class MovieDisplay(MovieDisplayTemplate):
  def __init__(self, **properties):
    # Set static data and bind screen elements to it.
    #self.item = {
    #  'movie_name': 'Back to the Future',
    #  'year': 1985,
    #  'director': 'Robert Zemeckis',
    #  'summary': 'Doc Brown invents a nuclear powered time machine, which Marty McFly '
    #              'then uses to nearly erase himself from existence.'
    #}

    # Client reading the table directly
    # self.item = app_tables.movies.search()[0]

    # Server code reading the data from db and passing it to client
    self.item = anvil.server.call('get_data')
    
    self.init_components(**properties)
  
  def edit_btn_click(self, **event_args):
    item = dict(self.item)
    edit_form = MovieEdit(item=item)
    alert(edit_form, large=True)
    anvil.server.call('update_movie', item)
    self.item = anvil.server.call('get_data')
    self.refresh_data_bindings()

  # you are converting items to dictonary as edit screen has write back enabled. So, if this is not set, it will try
  # to write back to databse from client ... that results in an error
  # With this, write back is into dictonary object. Then we can pass this dictonary to update server call.
  # Once update is completed, we need to read it back from database self.item as that is what is mapped to edit field
  # and refresh data.