import datetime
import os

import pytz

# Format of GreenPiThumb image files.
_FILENAME_FORMAT = '%Y-%m-%dT%H%MZ.jpg'


def _files_in_directory(directory, resolution_type):
    paths = os.listdir(directory)
    all_files = [f for f in paths if os.path.isfile(os.path.join(directory, f))]
    filtered_files = []

    if(resolution_type == 'full_res'):        
        full_res_files = []
        for f in all_files:
            if(f.startswith("full_")):
                full_res_files.append(f)
        filtered_files = full_res_files
    elif (resolution_type == 'reduced_res'):
        reduced_res_files = []
        for f in all_files:
            if(f.startswith("reduced_")):
                reduced_res_files.append(f)
        filtered_files = reduced_res_files
        
    return filtered_files


def _timestamp_from_filename(filename):
    filename_without_res_type_prefix = filename.split('_', 1)[-1]
    return datetime.datetime.strptime(filename_without_res_type_prefix, _FILENAME_FORMAT).replace(
        tzinfo=pytz.utc)


def _filename_to_index_entry(filename):
    return {
        'timestamp': _timestamp_from_filename(filename),
        'filename': filename,
    }


class Indexer(object):
    """Creates an index of GreenPiThumb image files."""

    def __init__(self, images_path, resolution_type):
        """Creates a new Indexer instance.

        Args:
            images_path: Path to the GreenPiThumb images directory.
            resolution_type: Can be either [reduced] or [full]
        """
        self._images_path = images_path
        self._resolution_type = resolution_type

    def index(self):
        """Generates an index of the GreenPiThumb image files.

        Creates an index of all the GreenPiThumb image files in the specified
        images path. If there are non-image files in the directory, these are
        ignored. Any GreenPiThumb image files in subdirectories are also
        ignored.

        Returns:
            A list of dictionaries, one for each GreenPiThumb image file, where
            the dictionary has keys 'timestamp' with the datetime when the file
            was created and 'filename' of the image's filename (without path
            prefix).
        """
        file_index = []
        for filename in _files_in_directory(self._images_path, self._resolution_type):
            try:
                file_index.append(_filename_to_index_entry(filename))
            except ValueError:
                # Ignore filenames that can't be parsed as GreenPiThumb images.
                pass

        return file_index
