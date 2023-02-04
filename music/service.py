import hashlib
import os
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from typing import Union


class FileCheck:
    @staticmethod
    def file_exist_check(path: str) -> Union[bool, str]:
        """
        Check if a file already exists in the given path.

        Parameters:
            path (str): The file path.

        Returns:
            bool : False if the file already exists at the given path,
            str : The path if the file does not exist.
        """
        if os.path.isfile(path):
            return False
        return path

    @staticmethod
    def check_file_size(file_object) -> ValidationError or None:
        """
        Check if the file size of the file_object is within the limit.

        Parameters:
            file_object: django.db.models.fields.files.ImageFieldFile.

        Returns:
            ValidationError: if file size exceeds the file_limit
            None: if file size is within limit
        """
        file_limit = 3  # field is a Byte
        if file_object.size > file_limit * 1024 * 1024:
            raise ValidationError(f"Max size file {file_limit}MB")


class FileModify:
    @staticmethod
    def file_hashing(instance, fieldname: str) -> str:
        """
        Hashes a file's name and returns the hash as a string.
        Parameters:
            instance (class): A class model instance.
            fieldname (str): The field name on the class model instance.
        Returns:
            str: The hashed file name.
        """
        hash256 = hashlib.sha256()
        field_file = getattr(instance, fieldname)
        for byte_chunk in field_file.chunks():
            hash256.update(byte_chunk)
        hashed_name_of_the_anime = hash256.hexdigest()
        return f"{hashed_name_of_the_anime}"


class FilePath:
    @staticmethod
    def get_path_to_image(instance, filename) -> str:
        """
        Returns the path for storing the anime movie.

        Parameters:
            instance (class): A class model instance.
            filename (str): The file's name.

        Returns:
            str: The path where the anime movie should be stored.
        """
        format_file = os.path.splitext(filename)[1].lower()
        path_to_image = "images/"
        hashed_filename = FileModify.file_hashing(instance, 'image')
        end_path = FileCheck.file_exist_check(
            path_to_image + hashed_filename + format_file
        )
        if end_path:
            return end_path
        return ''

    @staticmethod
    def get_path_to_album_cover(instance, filename) -> str:
        """
        Returns the path for storing the anime movie.

        Parameters:
            instance (class): A class model instance.
            filename (str): The file's name.

        Returns:
            str: The path where the anime movie should be stored.
        """
        format_file = os.path.splitext(filename)[1].lower()
        path_to_image = "images/"
        hashed_filename = FileModify.file_hashing(instance, 'cover')
        end_path = FileCheck.file_exist_check(
            path_to_image + hashed_filename + format_file
        )
        if end_path:
            return end_path
        return ''

    @staticmethod
    def get_path_to_audio_file(instance: classmethod, filename: str) -> str:
        """
        Returns the path for storing the anime movie.

        Parameters:
            instance (class): A class model instance.
            filename (str): The file's name.

        Returns:
            str: The path where the anime movie should be stored.
        """
        format_file = os.path.splitext(filename)[1].lower()
        path_to_song = "songs/"
        hashed_filename = FileModify.file_hashing(instance, 'audio_file')
        end_path = FileCheck.file_exist_check(
            path_to_song + hashed_filename + format_file
        )
        if end_path:
            return end_path
        return ''


class OverWriteStorage(FileSystemStorage):
    """
    A storage class that overwrites files with the same name when uploading new files.
    """
    def __init__(self):
        """
        Initializes the storage by calling the parent class's __init__ method.
        """
        super(OverWriteStorage, self).__init__()

    def get_available_name(self, name: str, max_length: int = 100) -> str:
        """
        Determines the available name for a file being stored.

        Parameters:
            - name (str): The desired name of the file being stored.
            - max_length (int): The maximum length of the file name. Defaults to 100.

        Returns:
            str: The final name of the file.
        """
        if self.exists(name):
            os.remove(os.path.join(self.location, name))
        return name
