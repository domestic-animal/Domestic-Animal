import os
from Engines.gameState import gameState
from filepath import ROOT_DIR
import pickle


class GameStateSaver:
    __dir = os.path.join(ROOT_DIR, "profiles")
    __game_mode = {1: ("story_autosave.pkl", "story_backup.pkl"),
                   -1: ("endless_autosave.pkl", "endless_backup.pkl")}

    def __init__(self):
        pass

    def save_story(self, user_name, game_state: gameState):
        """
        Save story game state to user profile.

        :param user_name: string of user_name
        :param game_state: gameState object.
        :return: True if saved, False otherwise.
        """
        game_state_path = os.path.join(self.__dir, user_name, "story_progress.pkl")
        return self.__write_pickle_file(game_state, game_state_path)

    def load_saved_story(self, user_name):
        """
        load story game state.
        :param user_name: string of user_name
        :return: gameState if loaded correctly , None otherwise.
        """
        game_state_path = os.path.join(self.__dir, user_name, "story_progress.pkl")
        return self.__read_pickle_file(game_state_path)

    def autosave_game_state(self, game_state, user_name, mode):
        """
        Auto-save game state to user profile.

        :param game_state: gameState object.
        :param user_name: string of user_name
        :param mode: game mode 1 for story , -1 for endless
        """
        autosave_path = os.path.join(self.__dir, user_name, self.__game_mode[mode][0])
        backup_path = os.path.join(self.__dir, user_name, self.__game_mode[mode][1])
        prev_state = self.__read_pickle_file(autosave_path)
        if prev_state is not None:
            self.__write_pickle_file(prev_state, backup_path)
            self.__write_pickle_file(game_state, autosave_path)
        else:
            self.__write_pickle_file(game_state, autosave_path)
            self.__write_pickle_file(game_state, backup_path)

    def load_autosaved_state(self, user_name, mode):
        """
        load auto-saved game state.

        :param user_name: string of user_name
        :param mode: game mode 1 for story , -1 for endless
        :return: gameState if loaded correctly , None otherwise.
        """
        autosave_path = os.path.join(self.__dir, user_name, self.__game_mode[mode][0])
        backup_path = os.path.join(self.__dir, user_name, self.__game_mode[mode][1])
        autosave = self.__read_pickle_file(autosave_path)
        if autosave is not None:
            return autosave
        # autosave is corrupted or deleted check back up.
        return self.__read_pickle_file(backup_path)

    def delete_autosaved_state(self, user_name, mode):
        """
        delete auto-saved game state.

        :param user_name: string of user_name
        :param mode: game mode 1 for story , -1 for endless
        :return: True if deleted, False otherwise.
        """
        autosave_path = os.path.join(self.__dir, user_name, self.__game_mode[mode][0])
        backup_path = os.path.join(self.__dir, user_name, self.__game_mode[mode][1])
        try:
            if os.path.exists(autosave_path):
                os.remove(autosave_path)
            if os.path.exists(backup_path):
                os.remove(backup_path)
            return True
        except OSError:
            return False

    def __write_pickle_file(self, object, path):
        """
        helper function for writing pickle file.

        :param object: object to write.
        :param path: string of path for saving file.
        :return: True if wrote correctly, False otherwise.
        """
        try:
            with open(path, 'wb') as pickle_file:
                pickle.dump(object, pickle_file)
                return True
        except (IOError, OSError, pickle.PickleError, pickle.UnpicklingError):
            return False

    def __read_pickle_file(self, path):
        """
        helper function for loading  pickled object.

        :param path: string of the path of file.
        :return: gameState if loaded correctly , None otherwise.
        """
        try:
            with open(path, 'rb') as pickle_file:
                return pickle.load(pickle_file)
        except (IOError, OSError, EOFError, pickle.PickleError, pickle.UnpicklingError):
            return None

