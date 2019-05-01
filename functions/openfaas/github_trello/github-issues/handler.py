from environs import Env
from github import Github
from loguru import logger
from trello import TrelloClient


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    env = Env()
    env.read_env()

    g = Github(env("username"), env("password"))
    user = g.get_user()

    client = TrelloClient(
        api_key=env("api_key"),
        api_secret=env("api_secret"),
        token=env("token"),
        token_secret=env("token_secret")
    )

    logger.info("Getting issues ...")
    issues = get_assigned_issues(user)
    logger.info("Getting trello lists ...")
    dev_board = get_board(client, "Development")
    label_names = [l.name for l in dev_board.get_labels()]
    issues_list = get_list(dev_board, "Issues")
    progress_list = get_list(dev_board, "In Progress")
    logger.info("Appending cards ...")
    logger.info("Appending issues ...")
    for i in issues:
        label = get_issue_label(dev_board, i, label_names)
        desc = get_description(i)
        if not is_card_in_lists([issues_list, progress_list], i.title):
            issues_list.add_card(i.title, labels=[label], desc=desc)
    logger.info("Issues appended!")
    logger.info("Done!")
    return "Done!"


def get_assigned_issues(user):
    issues = []
    for repo in user.get_repos():
        for issue in repo.get_issues():
            if user.login in get_login_assignees(issue.assignees):
                issues.append(issue)
    return issues


def get_login_assignees(assignees):
    return [a.login for a in assignees]


def get_board(client, name):
    board = [b for b in client.list_boards() if b.name == name]
    if board:
        return board[0]


def get_list(board, name):
    trello_list = [l for l in board.all_lists() if l.name == name]
    if trello_list:
        return trello_list[0]


def get_label(board, name):
    label = [l for l in board.get_labels() if l.name == name]
    if label:
        return label[0]


def get_issue_label(board, issue, label_names):
    if issue.repository.name not in label_names:
        return board.add_label(issue.repository.name, "green")
    else:
        return get_label(board, issue.repository.name)


def get_description(issue):
    return f"{issue.body}\n\nGithub URL: {issue.html_url}"


def is_card_in_lists(lists, card_name):
    for l in lists:
        for card in l.list_cards():
            if card.name == card_name:
                return True
    return False
