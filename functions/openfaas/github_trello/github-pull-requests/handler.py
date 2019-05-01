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

    logger.info("Getting pull requests ...")
    pull_requests = get_assigned_prs(user)
    logger.info("Getting trello lists ...")
    dev_board = get_board(client, "Development")
    label_names = [l.name for l in dev_board.get_labels()]
    pr_list = get_list(dev_board, "Pull Requests")
    progress_list = get_list(dev_board, "In Progress")
    logger.info("Appending cards ...")
    logger.info("Appending pull requests ...")
    for pr in pull_requests:
        label = get_pull_label(dev_board, pr, label_names)
        desc = get_description(pr)
        if not is_card_in_lists([pr_list, progress_list], pr.title):
            pr_list.add_card(pr.title, labels=[label], desc=desc)
    logger.info("Pull Requests appended!")
    logger.info("Done!")
    return "Done!"


def get_assigned_prs(user):
    pull_reviews = []
    for repo in user.get_repos():
        for pull in repo.get_pulls():
            reviewers = pull.get_reviews().get_page(0)
            if user.login in get_pr_reviewers(reviewers):
                pull_reviews.append(pull)
    return pull_reviews


def get_pr_reviewers(reviewers):
    return [r.user.login for r in reviewers]


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


def get_pull_label(board, pull, label_names):
    pr_name = pull.base.repo.name
    if pr_name not in label_names:
        return board.add_label(pr_name, "green")
    else:
        return get_label(board, pr_name)


def get_description(issue):
    return f"{issue.body}\n\nGithub URL: {issue.html_url}"


def is_card_in_lists(lists, card_name):
    for l in lists:
        for card in l.list_cards():
            if card.name == card_name:
                return True
    return False
