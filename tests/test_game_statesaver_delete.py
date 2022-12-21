import os
import shutil
from file.gamestatesaver import GameStateSaver
from tests.gamestatechecker import check_game_state, create_random_game_state , create_profiles_path
from filepath import ROOT_DIR
state_saver = GameStateSaver()


def test_delete_autosaved_story():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_story("test", game_state_old)
    game_state_recent = create_random_game_state()
    state_saver.autosave_story("test", game_state_recent)
    autosave_path = os.path.join(test_path, "story_autosave.pkl")
    back_up_path = os.path.join(test_path, "story_backup.pkl")
    is_deleted = state_saver.delete_autosaved_story("test")
    assert is_deleted and not os.path.exists(autosave_path) and not os.path.exists(back_up_path)
    shutil.rmtree(test_path, ignore_errors=True)


def test_delete_autosaved_story_non_existed_user():
    assert state_saver.delete_autosaved_story("test")


def test_delete_endless_story():
    create_profiles_path()
    test_path = os.path.join(ROOT_DIR, "profiles", "test")
    os.mkdir(test_path)
    game_state_old = create_random_game_state()
    state_saver.autosave_endless("test", game_state_old)
    game_state_recent = create_random_game_state()
    state_saver.autosave_endless("test", game_state_recent)
    autosave_path = os.path.join(test_path, "endless_autosave.pkl")
    back_up_path = os.path.join(test_path, "endless_backup.pkl")
    is_deleted = state_saver.delete_autosaved_endless("test")
    assert is_deleted and not os.path.exists(autosave_path) and not os.path.exists(back_up_path)
    shutil.rmtree(test_path, ignore_errors=True)


def test_delete_autosaved_endless_non_existed_user():
    assert state_saver.delete_autosaved_endless("test")