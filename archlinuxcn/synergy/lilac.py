from lilaclib import (
    edit_file,
    git_pkgbuild_commit,
    update_aur_repo,
)

def pre_build():
    tag = _G.newver

    for line in edit_file('PKGBUILD'):
        if line.startswith('_tag'):
            line = f'_tag={tag}'
        print(line)

def post_build():
    git_pkgbuild_commit()
    update_aur_repo()