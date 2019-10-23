import random
from pathlib import Path
import os

import pytest

from mega import Mega

TEST_CONTACT = 'test@mega.co.nz'
TEST_PUBLIC_URL = (
    'https://mega.nz/#!hYVmXKqL!r0d0-WRnFwulR_shhuEDwrY1Vo103-am1MyUy8oV6Ps'
)
TEST_FILE = os.path.basename(__file__)


@pytest.fixture
def folder_name():
    return 'mega.py_testfolder_{0}'.format(random.random())


@pytest.fixture
def mega(folder_name):
    mega_ = Mega()
    mega_.login(email=os.environ['EMAIL'], password=os.environ['PASS'])
    created_nodes = mega_.create_folder(folder_name)
    yield mega_
    node_id = next(iter(created_nodes.values()))
    mega_.destroy(node_id)


def test_mega(mega):
    assert isinstance(mega, Mega)


def test_login(mega):
    assert isinstance(mega, Mega)


def test_get_user(mega):
    resp = mega.get_user()
    assert isinstance(resp, dict)


def test_get_quota(mega):
    resp = mega.get_quota()
    assert isinstance(int(resp), int)


def test_get_storage_space(mega):
    resp = mega.get_storage_space(mega=True)
    assert isinstance(resp, dict)


def test_get_files(mega):
    files = mega.get_files()
    assert isinstance(files, dict)


def test_get_link(mega):
    file = mega.find(TEST_FILE)
    if file:
        link = mega.get_link(file)
        assert isinstance(link, str)


class TestExport:

    def test_export_folder(self, mega, folder_name):
        public_url = None
        for _ in range(2):
            result_public_share_url = mega.export(folder_name)

            if not public_url:
                public_url = result_public_share_url
            assert result_public_share_url.startswith('https://mega.co.nz/#F!')
            assert result_public_share_url == public_url

    def test_export_folder_within_folder(self, mega, folder_name):
        folder_path = Path(folder_name) / 'subdir' / 'anothersubdir'
        mega.create_folder(name=folder_path)

        result_public_share_url = mega.export(path=folder_path)

        assert result_public_share_url.startswith('https://mega.co.nz/#F!')

    def test_export_folder_using_node_id(self, mega, folder_name):
        node_id = mega.find(folder_name)[0]

        result_public_share_url = mega.export(node_id=node_id)

        assert result_public_share_url.startswith('https://mega.co.nz/#F!')

    def test_export_single_file(self, mega, folder_name):
        # Upload a single file into a folder
        folder = mega.find(folder_name)
        dest_node_id = folder[1]['h']
        mega.upload(
            __file__, dest=dest_node_id, dest_filename='test.py'
        )
        path = '{}/test.py'.format(folder_name)
        assert mega.find(path)

        for _ in range(2):
            result_public_share_url = mega.export(path)

            assert result_public_share_url.startswith('https://mega.co.nz/#!')


def test_import_public_url(mega):
    resp = mega.import_public_url(TEST_PUBLIC_URL)
    file_handle = mega.get_id_from_obj(resp)
    resp = mega.destroy(file_handle)
    assert isinstance(resp, int)


class TestCreateFolder:
    def test_create_folder(self, mega, folder_name):
        folder_names_and_node_ids = mega.create_folder(folder_name)

        assert isinstance(folder_names_and_node_ids, dict)
        assert len(folder_names_and_node_ids) == 1

    def test_create_folder_with_sub_folders(self, mega, folder_name, mocker):
        folder_names_and_node_ids = mega.create_folder(
            name=(Path(folder_name) / 'subdir' / 'anothersubdir')
        )

        assert len(folder_names_and_node_ids) == 3
        assert folder_names_and_node_ids == {
            folder_name: mocker.ANY,
            'subdir': mocker.ANY,
            'anothersubdir': mocker.ANY,
        }


def test_rename(mega, folder_name):
    file = mega.find(folder_name)
    if file:
        resp = mega.rename(file, folder_name)
        assert isinstance(resp, int)


def test_delete_folder(mega, folder_name):
    folder_node = mega.find(folder_name)[0]
    resp = mega.delete(folder_node)
    assert isinstance(resp, int)


def test_delete(mega):
    file = mega.find(TEST_FILE)
    if file:
        resp = mega.delete(file[0])
        assert isinstance(resp, int)


def test_destroy(mega):
    file = mega.find(TEST_FILE)
    if file:
        resp = mega.destroy(file[0])
        assert isinstance(resp, int)


def test_empty_trash(mega):
    # resp None if already empty, else int
    resp = mega.empty_trash()
    if resp is not None:
        assert isinstance(resp, int)


def test_add_contact(mega):
    resp = mega.add_contact(TEST_CONTACT)
    assert isinstance(resp, int)


def test_remove_contact(mega):
    resp = mega.remove_contact(TEST_CONTACT)
    assert isinstance(resp, int)
