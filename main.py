from config.config import ProjectConfig
from src.classifiers.classifier import Classifier
from src.preprocessors.image_processor import ImageProcessor
from src.database.database_manager import DatabaseManager
from src.handlers.file_handler import FileHandler
from src.history.history_manager import HistoryManager

if __name__ == "__main__":
    # Load configuration
    config = ProjectConfig()
    config.load_config()

    # Initialize database
    db_manager = DatabaseManager(config.database_path)
    db_manager.connect()
    db_manager.close_connection()

    # Test image processing
    processor = ImageProcessor()
    processor.resize_image("sample_image.jpg")
    processor.normalize_image("sample_image.jpg")
    processor.augment_image("sample_image.jpg")

    # Test classifier
    classifier = Classifier()
    classifier.load_model(config.model_path)
    classifier.train_model("data/train_dataset/")

    # Test file handling
    file_handler = FileHandler()
    file_handler.upload_file("sample_image.jpg")
    file_handler.validate_file("sample_image.jpg")

    # Test history management
    history_manager = HistoryManager()
    history_manager.fetch_user_history()
    history_manager.store_classification_result("Example Result")
