from fabric.api import local, settings
from fabric.context_managers import hide

from bright_fabric.fab import abs_path, find_files, jslint_file


def pylint():
    flake8_command = 'flake8 --ignore=E501'

    all_files = \
        find_files(abs_path('.'), ['py'], exclude_dirs=['migrations'])
    all_files_for_cmd = "'" + "' '".join(all_files) + "'"
    with settings(hide('aborts', 'running')):
        local('%s %s' % (flake8_command, all_files_for_cmd))


def jslint():
    """
    We're using jslint-reporter:
        https://github.com/FND/jslint-reporter

    You'll need to install Node.js to run `fab jslint`:
        https://github.com/joyent/node/wiki/Installation

    To updgrade jslint use:
        `node tool/jslint-wrapper.js --upgrade`
    """

    with settings(warn_only=True):
        JS_ROOT = abs_path('static/js')
        SNIPPETS_ROOT = abs_path('templates/snippets')

        for filename in find_files(JS_ROOT, ['js'], exclude_dirs=['lib']):
            jslint_file(filename)
        # There are some JavaScript snippets in that get included into the
        # template HTML, so they have to be under templates/ not static/js/
        for filename in find_files(SNIPPETS_ROOT, ['js']):
            jslint_file(filename)
