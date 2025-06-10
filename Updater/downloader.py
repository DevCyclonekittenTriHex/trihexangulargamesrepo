import os
import urllib.request
import zipfile
import shutil
import subprocess
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def install_github_link(url,zip_path,extract_path):

    try:
        home_dir = os.path.expanduser("~")
        if home_dir:
            project_path = os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Updater")
        else:
            print("Could Not FInd LocalLow")
        launcher_path = project_path = os.path.join(home_dir, "AppData", "LocalLow","Trihexangular Studios","Trihexangular Launcher")
        download_path = os.path.join(project_path, "Downloading")
        


        os.makedirs(download_path, exist_ok=True)
        os.makedirs(extract_path, exist_ok=True)

        if os.path.exists(zip_path):
            try:
                os.remove(zip_path)
                logging.info("Deleted existing zip file.")
            except Exception as e:
                logging.error(f"Error deleting existing zip: {e}")
                return False  # Indicate failure
        try:
            urllib.request.urlretrieve(url, zip_path)
            #logging.info(f"File downloaded and saved to: {zip_path}")
        except Exception as e:
            logging.error(f"Download Error: {e}")
            return False
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            #logging.info("File extracted successfully.")
        except zipfile.BadZipFile as e:
            logging.error(f"Extraction failed: Invalid zip file - {e}")
            return False
        except Exception as e:
            logging.error(f"Extraction failed with an unexpected error: {e}")
            return False
        try:
            os.remove(zip_path)
            #logging.info("Deleted zip file after extraction.")
        except Exception as e:
            logging.error(f"Error deleting zip after extraction: {e}")
        return True
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return False


