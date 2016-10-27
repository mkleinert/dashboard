__author__ = 'mkleinert'
import pypyodbc
import logging as log

FORMAT = '%(asctime)s - %(message)s'
WARNINGFORMAT = 'WARNING:: %(asctime)s %(message)s'
log.basicConfig(level=log.INFO, format=FORMAT)
log.basicConfig(level=log.warning, format=WARNINGFORMAT)

class shqsql:

    def __init__(self, database=None, server=None, user=None, password=None):
        if not database: self.database = 'republicoftea'
        else: self.database = database

        # if not port: self.port = '5439'
        # else: self.port = port

        if not user: self.user = 'mkleinert'
        else: self.user = user

        if not password: self.password = ''
        else: self.password = password

        if not server: self.server = 'S871DBSP01VW'
        else: self.server = server

        log.info('Default host: %s' %self.database)

        return

    def _set_database_(self, database):
          """set the database property"""
          self.database = database
          return

    def _set_server_(self, server):
          """set the server property"""
          log.info('Setting a new server: %s'%server)
          self.server = server
          return

    def _set_user_(self, user):
          """set the server property"""
          self.user = user
          return

    def _set_password_(self, password):
          """set the server property"""
          self.password = password
          return

    def set_cnxn(self, **kwargs):
          """ Here we define the connection properties that we will
          use in the sql call.
          sql
          """
          try:
               self.server = server
               self.database = database
               self.password = password
               self.user = user
               log.info('Overloading SQL connection variables')
          except:
               pass
               #print('No overload of SQL Connection variables.')

        connection_string = 'Driver={SQL Server};Server=' + server + ';Database=' + database + ';UID=' + user + ';PWD=' + password + ';'
        self.cnxn = pypyodbc.connect(connection_string)

        return

    def open_cnxn(self,**kwargs):
          # Explicitly Opens the connection

          #if not self.cnxn:
          self.set_cnxn(**kwargs)
          self.cur = self.cnxn.cursor()  #sets up the cursor
          return

    def close_cnxn(self):
          # Close the SQL connection

          self.cur.close()
          return


