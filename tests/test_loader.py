import pytest, os
from src.loaders.loader import Loader
from src.pipelines.text_processor import TextProcessor

path = "tests/fixtures/temp_directory/"


@pytest.fixture
def loader():
    test_loader = Loader()
    yield test_loader
    del test_loader


def test_get_files_from_directory(loader):
    filelist = loader.get_files_from_directory(path)
    expected = set([f"{path}file1.txt", f"{path}file2.md", f"{path}file3.md"])
    assert not set(filelist) ^ expected


def test_read_files(loader):
    #! does not yet deal with newline chars
    filelist = loader.get_files_from_directory(path)
    doc_index = loader.read_files(filelist)
    assert doc_index == {
        f"{path}file1.txt": """I am file 1\n\nSense of beauty and state space reduction\n\nI have been teaching myself reinforcement learning and have made some interesting connections that I want to share. In reinforcement learning (RL), you use games as a substrate to teach an AI how to learn the optimal strategy to win. You craft an algorithm that the RL agent, given enough computing power, can theoretically converge to the optimal strategy to play the game.""",
        f"{path}file2.md": """Now we have a sense of the essential components of an RL algorithm. As we start with simple games, we can encounter every state and create an entry in the "value function" table. For example, in the game of tic-tac-toe, there are 3^9 (or 19,683 possibilities) which a computer can easily work with. Note that this number includes illegal states, so the actual number is smaller. A minor upgrade to a game like (Connect-4)[https://en.wikipedia.org/wiki/Connect_Four] where you drop a coin and aim to make the longest sequence of 4 coins, the number of states explodes to 3^42 (or 1.09418989E20)! The total bytes of information humanity has produced so far in totality is estimated to be 1E22 bytes. This is comparable to the state space of a simple children\'s game! It is a wonder we are able to play it at all.""",
        f"{path}file3.md": "I am file 3",
    }


def test_textprocessor(loader):
    tp = TextProcessor()
    doc_index = loader.extract_text(path)
    cleaned_index = tp.remove_newline(doc_index)
    assert cleaned_index == {
        f"{path}file1.txt": """I am file 1. Sense of beauty and state space reduction. I have been teaching myself reinforcement learning and have made some interesting connections that I want to share. In reinforcement learning (RL), you use games as a substrate to teach an AI how to learn the optimal strategy to win. You craft an algorithm that the RL agent, given enough computing power, can theoretically converge to the optimal strategy to play the game.""",
        f"{path}file2.md": """Now we have a sense of the essential components of an RL algorithm. As we start with simple games, we can encounter every state and create an entry in the "value function" table. For example, in the game of tic-tac-toe, there are 3^9 (or 19,683 possibilities) which a computer can easily work with. Note that this number includes illegal states, so the actual number is smaller. A minor upgrade to a game like (Connect-4)[https://en.wikipedia.org/wiki/Connect_Four] where you drop a coin and aim to make the longest sequence of 4 coins, the number of states explodes to 3^42 (or 1.09418989E20)! The total bytes of information humanity has produced so far in totality is estimated to be 1E22 bytes. This is comparable to the state space of a simple children\'s game! It is a wonder we are able to play it at all.""",
        f"{path}file3.md": "I am file 3",
    }
