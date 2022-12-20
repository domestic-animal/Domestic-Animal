import os
import pickle
import shutil
from gamestatesaver import GameStateSaver
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



def test_auto_save_story_first_time():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    state_saver.autosave_story("test", game_state)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    back_up_path = os.path.join(test_path, "story_backup.pkl")
    with open(autosave_path, 'rb') as pickle_file:
        autosave_state = pickle.load(pickle_file)
    with open(back_up_path, 'rb') as pickle_file:
        back_up_state = pickle.load(pickle_file)
    assert check_game_state(game_state, back_up_state) and check_game_state(game_state, autosave_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_auto_save_story_back_up():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    state_saver.autosave_story("test", game_state)
    game_state_2 = create_random_game_state()
    state_saver.autosave_story("test", game_state_2)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    back_up_path = os.path.join(test_path, "story_backup.pkl")
    assert os.path.exists(autosave_path) and os.path.exists(back_up_path)
    shutil.rmtree(test_path, ignore_errors=True)


def test_auto_save_story_back_up_data():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_story("test", game_state_old)
    game_state_recent = create_random_game_state()
    state_saver.autosave_story("test", game_state_recent)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    back_up_path = os.path.join(test_path, "story_backup.pkl")
    with open(autosave_path, 'rb') as pickle_file:
        autosave_state = pickle.load(pickle_file)
    with open(back_up_path, 'rb') as pickle_file:
        back_up_state = pickle.load(pickle_file)
    assert check_game_state(game_state_recent, autosave_state) \
           and check_game_state(game_state_old, back_up_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_autosave_story_autosave_file_corrupted():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    with open(autosave_path, "w") as file:
        file.write("corrupted data")
    game_state = create_random_game_state()
    state_saver.autosave_story("test", game_state)
    with open(autosave_path, 'rb') as pickle_file:
        autosave_state = pickle.load(pickle_file)
    assert check_game_state(game_state, autosave_state)
    shutil.rmtree(test_path, ignore_errors=True)

def test_auto_save_endless_first_time():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    state_saver.autosave_endless("test", game_state)
    autosave_path = os.path.join(test_path, "endless_autosave.pkl")
    back_up_path = os.path.join(test_path, "endless_backup.pkl")
    with open(autosave_path, 'rb') as pickle_file:
        autosave_state = pickle.load(pickle_file)
    with open(back_up_path, 'rb') as pickle_file:
        back_up_state = pickle.load(pickle_file)
    assert check_game_state(game_state, back_up_state) and check_game_state(game_state, autosave_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_auto_save_endless_back_up():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    state_saver.autosave_endless("test", game_state)
    game_state_2 = create_random_game_state()
    state_saver.autosave_endless("test", game_state_2)
    autosave_path = os.path.join(test_path, "endless_autosave.pkl")
    back_up_path = os.path.join(test_path, "endless_backup.pkl")
    assert os.path.exists(autosave_path) and os.path.exists(back_up_path)
    shutil.rmtree(test_path, ignore_errors=True)


def test_auto_save_endless_back_up_data():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_endless("test", game_state_old)
    game_state_recent = create_random_game_state()
    state_saver.autosave_endless("test", game_state_recent)
    autosave_path = os.path.join(test_path, "endless_autosave.pkl")
    back_up_path = os.path.join(test_path, "endless_backup.pkl")
    with open(autosave_path, 'rb') as pickle_file:
        autosave_state = pickle.load(pickle_file)
    with open(back_up_path, 'rb') as pickle_file:
        back_up_state = pickle.load(pickle_file)
    assert check_game_state(game_state_recent, autosave_state) \
           and check_game_state(game_state_old, back_up_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_autosave_endless_autosave_file_corrupted():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    autosave_path = os.path.join(test_path, "endless_autosave.pkl")
    with open(autosave_path, "w") as file:
        file.write("corrupted data")
    game_state = create_random_game_state()
    state_saver.autosave_endless("test", game_state)
    with open(autosave_path, 'rb') as pickle_file:
        autosave_state = pickle.load(pickle_file)
    assert check_game_state(game_state, autosave_state)
    shutil.rmtree(test_path, ignore_errors=True)
