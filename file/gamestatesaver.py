import os
from Engines.gameState import gameState
from filepath import ROOT_DIR
import pickle


class GameStateSaver:
    __dir = os.path.join(ROOT_DIR, "profiles")

    def __init__(self):
        pass

    def save_story(self, user_name, game_state: gameState):
        game_state_path = os.path.join(self.__dir, user_name, "story_progress.pkl")
        return self.__write_pickle_file(game_state, game_state_path)


    def autosave_endless(self, user_name, game_state: gameState):
        autosave_path = os.path.join(self.__dir, user_name, "endless_autosave.pkl")
        backup_path = os.path.join(self.__dir, user_name, "endless_backup.pkl")
        self.__autosave_game_state(game_state, autosave_path, backup_path)

    def autosave_story(self, user_name, game_state: gameState):
        autosave_path = os.path.join(self.__dir, user_name, "story_autosave.pkl")
        backup_path = os.path.join(self.__dir, user_name, "story_backup.pkl")
        self.__autosave_game_state(game_state, autosave_path, backup_path)

    def load_saved_story(self, user_name):
        game_state_path = os.path.join(self.__dir, user_name, "story_progress.pkl")
        return self.__read_pickle_file(game_state_path)

    def load_autosaved_story(self, user_name):
        autosave_path = os.path.join(self.__dir, user_name, "story_autosave.pkl")
        backup_path = os.path.join(self.__dir, user_name, "story_backup.pkl")
        return self.__load_autosaved_state(autosave_path, backup_path)

    def load_autosaved_endless(self, user_name):
        autosave_path = os.path.join(self.__dir, user_name, "endless_autosave.pkl")
        backup_path = os.path.join(self.__dir, user_name, "endless_backup.pkl")
        return self.__load_autosaved_state(autosave_path, backup_path)

    def __autosave_game_state(self, game_state, autosave_path, backup_path):
        if not os.path.exists(autosave_path):
            self.__write_pickle_file(game_state, autosave_path)
        else:
            prev_state = self.__read_pickle_file(autosave_path)

            if prev_state is not None:
                self.__write_pickle_file(prev_state, backup_path)
                self.__write_pickle_file(game_state, autosave_path)

            else:
                self.__write_pickle_file(game_state, autosave_path)

    def __load_autosaved_state(self, autosave_path, backup_path):
        autosave = self.__read_pickle_file(autosave_path)
        if autosave is not None:
            return autosave
        # autosave is corrupted or deleted check back up.
        return self.__read_pickle_file(backup_path)

    def delete_autosaved_story(self, user_name):
        autosave_path = os.path.join(self.__dir, user_name, "story_autosave.pkl")
        backup_path = os.path.join(self.__dir, user_name, "story_backup.pkl")
        return self.__delete_autosaved(autosave_path, backup_path)

    def delete_autosaved_endless(self, user_name):
        autosave_path = os.path.join(self.__dir, user_name, "endless_autosave.pkl")
        backup_path = os.path.join(self.__dir, user_name, "endless_backup.pkl")
        return self.__delete_autosaved(autosave_path, backup_path)


    def __delete_autosaved(self, autosave_path, backup_path):
        try:
            if os.path.exists(autosave_path):
                os.remove(autosave_path)
            if os.path.exists(backup_path):
                os.remove(backup_path)
            return True
        except OSError:
            return False


    def __write_pickle_file(self, object, path):
        try:
            with open(path, 'wb') as pickle_file:
                pickle.dump(object, pickle_file)
                return True
        except (IOError, OSError, pickle.PickleError, pickle.UnpicklingError):
            return False

    def __read_pickle_file(self, path):
        try:
            with open(path, 'rb') as pickle_file:
                return pickle.load(pickle_file)

        except (IOError, OSError, EOFError, pickle.PickleError, pickle.UnpicklingError):
            return None

