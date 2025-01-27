# config/config.py

class ProjectConfig:
    """
    A class to manage configuration settings for the project.
    """
    def __init__(self):
        # Path to the database file
        self.database_path = "data/database.db"
        # Path to the trained model file
        self.model_path = "models/trained_model.h5"
        # Path for storing uploaded files
        self.upload_path = "data/uploads/"

    def load_config(self):
        """
        Placeholder for loading configuration from an external file.
        """
        print("Loading configuration...")

    def save_config(self):
        """
        Placeholder for saving configuration to an external file.
        """
        print("Saving configuration...")
