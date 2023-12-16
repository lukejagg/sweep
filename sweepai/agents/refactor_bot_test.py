import os

from sweepai.agents.refactor_bot import RefactorBot
from sweepai.core.entities import Message
from sweepai.utils.chat_logger import ChatLogger
from sweepai.utils.github_utils import ClonedRepo

if __name__ == "__main__":
    installation_id = os.environ["INSTALLATION_ID"]
    cloned_repo = ClonedRepo("sweepai/sweep", installation_id, "main")

    additional_messages = [
        Message(
            role="user",
            content="""Repo: sweep: Sweep: AI-powered Junior Developer for small features and bug fixes.
    Issue Title: Sweep: Refactor modify_bot.py to be more modular.
    Issue Description: ### Details

    _No response_""",
            key="user",
        )
    ]
    file_path = "sweepai/agents/modify_bot.py"
    request = "Refactor modify_bot.py to be more modular."
    changes_made = ""
    chat_logger = ChatLogger({"username": "wwzeng1"})
    bot = RefactorBot()
    bot.chat_logger = chat_logger
    bot.model = "gpt-4-0613"
    new_code = bot.refactor_snippets(
        additional_messages=additional_messages,
        file_path=file_path,
        request=request,
        changes_made=changes_made,
        cloned_repo=cloned_repo,
    )
    import pdb

    pdb.set_trace()
    refactor_bot = RefactorBot()
