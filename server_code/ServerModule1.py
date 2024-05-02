import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def get_data():
  row = app_tables.movies.search()[0]
  return row

@anvil.server.callable
def update_movie(movie_data):
  if movie_data['director'] and movie_data['movie_name'] and movie_data['summary'] and movie_data['year']:
    row = app_tables.movies.search()[0]
    row['director'] = movie_data['director']
    row['movie_name'] = movie_data['movie_name']
    row['summary'] = movie_data['summary']
    row['year'] = movie_data['year']
  