import sqlite3


class SpatialiteDatabase:
    """The SpatialiteDatabase class represents a Spatialite database. It manages the
    database connection and cursor. Upon connection, the Spatialite extension is loaded.

    Args:
        database_filepath (str):
            File path for the Spatialite database file.
        spatialite_filepath (str):
            File path of the Spatialite extension.

    Attributes:
        database_filepath (str):
            Spatialite database file path.
        spatialite_filepath (str):
            File path to the Spatialite extension.
        connection (sqlite3.Connection):
            Database connection
        cursor (sqlite3.Cursor):
            Database cursor
    """

    def __init__(self, database_filepath, spatialite_filepath="mod_spatialite"):
        self.database_filepath = database_filepath
        self.spatialite_filepath = spatialite_filepath

        self.connection = None
        self.cursor = None

    def connect(self, init_spatial_metadata=True):
        """Connects to a database, loads the Spatialite extension and
        initializes it if requested. If the database file does not exist,
        it will be automatically created.

        Args:
            init_spatial_metadata (Bool):
                Defines if the spatial metadata should be initialized. This is not
                necessary if an existing Spatialite database is opened.
        """

        # Connect (if exists) or create SQLite database
        print("Connecting to database at %s" % self.database_filepath)
        try:
            self.connection = sqlite3.connect(self.database_filepath)
        except Exception:
            print("Error connecting to the database file")
            raise
        print("Connection to database established")

        # Load and initialize the Spatialite extension
        self.connection.enable_load_extension(True)
        sql_statement = "SELECT load_extension('%s');" % self.spatialite_filepath
        try:
            self.connection.execute(sql_statement)
        except sqlite3.OperationalError:
            print("Error loading spatial extension")
            raise
        print("Spatialite extension loaded")

        if init_spatial_metadata:
            try:
                self.connection.execute("SELECT InitSpatialMetaData(1);")
            except Exception:
                print("Error initializing spatial metadata")
                raise
            print("Spatial metadata initialized")

        # Debug output
        try:
            versions = self.connection.execute("SELECT sqlite_version(), spatialite_version()")
        except Exception:
            print("Error querying database versions")
            raise
        for row in versions:
            print("SQLite version: %s" % row[0])
            print("Spatialite version: %s" % row[1])

        self.cursor = self.connection.cursor()
