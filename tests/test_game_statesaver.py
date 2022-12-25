import os
import pickle
import shutil
from file.gamestatesaver import GameStateSaver
from tests.gamestatechecker import check_game_state, create_random_game_state , create_profiles_path
from filepath import ROOT_DIR
state_saver = GameStateSaver()


def test_save_story():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    is_saved = state_saver.save_story("test", game_state)
    file_path = os.path.join(test_path, "story_progress.pkl")
    assert os.path.exists(file_path) and is_saved
    shutil.rmtree(test_path, ignore_errors=True)


def test_save_story_non_existed_user():
    create_profiles_path()
    #non exist path
    game_state = create_random_game_state()
    is_saved = state_saver.save_story("test", game_state)
    assert not is_saved



def test_auto_save_first_time():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    state_saver.autosave_game_state(game_state, "test", 1)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    back_up_path = os.path.join(test_path, "story_backup.pkl")
    with open(autosave_path, 'rb') as pickle_file:
        autosave_state = pickle.load(pickle_file)
    with open(back_up_path, 'rb') as pickle_file:
        back_up_state = pickle.load(pickle_file)
    assert check_game_state(game_state, back_up_state) and check_game_state(game_state, autosave_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_auto_save_back_up_data_is_last_autosaved_data():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_game_state(game_state_old, "test", 1)
    game_state_recent = create_random_game_state()
    state_saver.autosave_game_state(game_state_recent, "test", 1)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    back_up_path = os.path.join(test_path, "story_backup.pkl")
    with open(autosave_path, 'rb') as pickle_file:
        autosave_state = pickle.load(pickle_file)
    with open(back_up_path, 'rb') as pickle_file:
        back_up_state = pickle.load(pickle_file)
    assert check_game_state(game_state_recent, autosave_state) \
           and check_game_state(game_state_old, back_up_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_autosave_autosave_file_corrupted():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    with open(autosave_path, "w") as file:
        file.write("corrupted data")
    game_state = create_random_game_state()
    state_saver.autosave_game_state(game_state, "test", 1)
    with open(autosave_path, 'rb') as pickle_file:
        autosave_state = pickle.load(pickle_file)
    assert check_game_state(game_state, autosave_state)
    shutil.rmtree(test_path, ignore_errors=True)

def test_load_story():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    state_saver.save_story("test", game_state)
    loaded_state = state_saver.load_saved_story("test")
    assert check_game_state(game_state, loaded_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_load_story_non_existed_user():
    create_profiles_path()
    loaded_state = state_saver.load_saved_story("test")
    assert loaded_state is None


def test_load_autosaved():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    state_saver.autosave_game_state(game_state, "test", 1)
    loaded_state = state_saver.load_autosaved_state("test", 1)
    assert check_game_state(game_state, loaded_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_load_autosaved_autosave_file_corrupted():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_game_state(game_state_old, "test", 1)
    game_state_recent = create_random_game_state()
    state_saver.autosave_game_state(game_state_recent, "test", 1)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    with open(autosave_path, "w") as file:
        file.write("corrupted data")
    game_state = state_saver.load_autosaved_state("test", 1)
    assert check_game_state(game_state_old, game_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_load_autosaved_both_autosave_and_backup_files_corrupted():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_game_state(game_state_old, "test", 1)
    game_state_recent = create_random_game_state()
    state_saver.autosave_game_state(game_state_recent, "test", 1)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    back_up_path = os.path.join(test_path, "story_backup.pkl")
    with open(autosave_path, "w") as file:
        file.write("corrupted data")
    with open(back_up_path, "w") as file:
        file.write("corrupted data")
    game_state = state_saver.load_autosaved_state("test", 1)
    assert game_state is None
    shutil.rmtree(test_path, ignore_errors=True)
def test_delete_autosaved():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    state_saver.autosave_game_state(game_state, "test", -1)
    autosave_path = os.path.join(test_path, "endless_autosave.pkl")
    back_up_path = os.path.join(test_path, "endless_backup.pkl")
    is_deleted = state_saver.delete_autosaved_state("test", -1)
    assert is_deleted and not os.path.exists(autosave_path) and not os.path.exists(back_up_path)
    shutil.rmtree(test_path, ignore_errors=True)


def test_delete_autosaved_non_existed_user():
    assert state_saver.delete_autosaved_state("test", 1)

