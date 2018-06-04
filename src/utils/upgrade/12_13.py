from django.db.models.signals import post_save

from journal import models as journal_models
from submission import models as submission_models
from core import models as core_models, workflow

from utils import setting_handler


SETTINGS_TO_CHANGE = [
    {'group': 'email', 'name': 'copyeditor_reopen_task', 'action': 'update'},
    {'group': 'email', 'name': 'author_copyedit_complete', 'action': 'update'},
    {'group': 'general', 'name': 'submission_competing_interests', 'action': 'drop'},
]


def run_journal_signals():
    """
    Gets and saves all journal objects forcing them to fire signals, 1.2 -> 1.3 introduced a couple of signales
    so we want them to be fired on upgrade.
    :return: None
    """
    print('Processing journal signals')
    journals = journal_models.Journal.objects.all()

    for journal in journals:
        print('Firing signals for {journal_code}'.format(journal_code=journal.code), end='...')

        post_save.send(journal_models.Journal, instance=journal, created=True)

        print(' [OK]')


def add_workflow_log_entries(article, stage_log_objects):
    """
    Adds a workflow log entry for each stage log entry
    :param article: Article object
    :param stage_log_objects: QuerySet of ArticleStageLog objects
    :return: None
    """

    non_workflow_stages = ['Published', 'Assigned', 'Under Revision',
                           'Author Copyediting', 'Final Copyediting', 'Rejected']

    for entry in stage_log_objects:

        if entry.stage_to == 'Under Review':
            stage = 'Unassigned'
        else:
            stage = entry.stage_to

        if entry.stage_to not in non_workflow_stages:
            workflow_element = core_models.WorkflowElement.objects.get(journal=article.journal,
                                                                       stage=stage)
            core_models.WorkflowLog.objects.get_or_create(article=article,
                                                          element=workflow_element,
                                                          defaults={'timestamp': entry.date_time})


def process_article_workflow():
    """
    Processes an article and adds workflow history objects for it.
    :return: None
    """
    print('Processing workflow migration')
    for journal in journal_models.Journal.objects.all():
        print('Working on {journal_code}'.format(journal_code=journal.code))
        for article in submission_models.Article.objects.filter(journal=journal):
            stage_log_objects = submission_models.ArticleStageLog.objects.filter(article=article).order_by('date_time')

            if article.is_import:
                print('Article is import and has no workflow records.')
            else:
                add_workflow_log_entries(article, stage_log_objects)


def execute():
    run_journal_signals()
    process_article_workflow()
    setting_handler.update_settings(SETTINGS_TO_CHANGE, journal)