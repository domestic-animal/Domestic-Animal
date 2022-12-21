import os
import pickle
import shutil
from file.gamestatesaver import GameStateSaver
from tests.gamestatechecker import check_game_state, create_random_game_state , create_profiles_path
from filepath import ROOT_DIR
state_saver = GameStateSaver()


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


def test_load_autosaved_story():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    state_saver.autosave_story("test", game_state)
    loaded_state = state_saver.load_autosaved_story("test")
    assert check_game_state(game_state, loaded_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_load_autosaved_story_autosave_file_corrupted():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_story("test", game_state_old)
    game_state_recent = create_random_game_state()
    state_saver.autosave_story("test", game_state_recent)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    with open(autosave_path, "w") as file:
        file.write("corrupted data")
    game_state = state_saver.load_autosaved_story("test")
    assert check_game_state(game_state_old, game_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_load_autosaved_story_both_autosave_and_backup_files_corrupted():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_story("test", game_state_old)
    game_state_recent = create_random_game_state()
    state_saver.autosave_story("test", game_state_recent)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    back_up_path = os.path.join(test_path, "story_backup.pkl")
    with open(autosave_path, "w") as file:
        file.write("corrupted data")
    with open(back_up_path, "w") as file:
        file.write("corrupted data")
    game_state = state_saver.load_autosaved_story("test")
    assert game_state is None
    shutil.rmtree(test_path, ignore_errors=True)


def test_load_autosaved_endless():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state = create_random_game_state()
    state_saver.autosave_endless("test", game_state)
    loaded_state = state_saver.load_autosaved_endless("test")
    assert check_game_state(game_state, loaded_state)
    shutil.rmtree(test_path, ignore_errors=True)


def test_load_autosaved_endless_autosave_file_corrupted():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_endless("test", game_state_old)
    game_state_recent = create_random_game_state()
    state_saver.autosave_endless("test", game_state_recent)
    autosave_path = os.path.join(test_path, "endless_autosave.pkl")
    with open(autosave_path, "w") as file:
        file.write("corrupted data")
    game_state = state_saver.load_autosaved_endless("test")
    assert check_game_state(game_state_old, game_state)
    shutil.rmtree(test_path, ignore_errors=True)

def test_load_autosaved_endless_both_autosave_and_backup_files_corrupted():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_endless("test", game_state_old)
    game_state_recent = create_random_game_state()
    state_saver.autosave_endless("test", game_state_recent)
    autosave_path = os.path.join(test_path, "endless_autosave.pkl")
    back_up_path = os.path.join(test_path, "endless_backup.pkl")
    with open(autosave_path, "w") as file:
        file.write("corrupted data")
    with open(back_up_path, "w") as file:
        file.write("corrupted data")
    game_state = state_saver.load_autosaved_endless("test")
    assert game_state is None
    shutil.rmtree(test_path, ignore_errors=True)

