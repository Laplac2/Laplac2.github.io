# Git

- [简介](#简介)
- [命令](#命令)
  - [git clone](#git-clone)
  - [git add](#git-add)
  - [git commit](#git-commit)
  - [git pull](#git-pull)
  - [git push](#git-push)
  - [git fetch](#git-fetch)
  - [git rebase](#git-rebase)
  - [git remote](#git-remote)
  - [git cherry-pick](#git-cherry-pick)
  - [git diff](#git-diff)
- [进阶操作](#进阶操作)
  - [忽略更改](#忽略更改)
  - [设置跟踪关系](#设置跟踪关系)
- [Reference](#reference)

## 简介

## 命令

### git clone

```bash
git clone url directory-name # 将拉下来的仓库文件夹重命名
```

### git add

```bash
git add .
git add file-path-name
git add --patch file-path-name  #
```

### git commit

```bash
git commit --amend
git commit --no-edit
```

### git pull

```bash
git pull origin --rebase
```

### git push

```bash
git push -f origin
```

### git fetch

```bash
git fetch orgin
```

### git rebase

```bash
git rebase -i hash
git rebase --autosquash -i hash
```

### git remote

```bash
git remote -v
git remote show origin
git remote prune origin
```

### git cherry-pick

### git diff

commit_A: 前一次提交的 hash 值。
commit_B: 需要导出位置的提交的 hash 值。
`git diff commit_A commit_B > pach.pach`
注：导出的 pach 文件是两个提交信息之间所有的差异。

## 进阶操作

### 忽略更改

- `.gitignore`
  - 说明：显式地阻止提交文件。
  - 优势：.gitignore 文件本身提交至远程仓库，全组共享忽略文件配置。
  - 局限：如果项目已经存在远程仓库，即使被加入 .gitignore，仍然可以进行修改并提交。本地的修改会显示在 git status 结果中。
- `.git/info/exclude`
  - 说明：显式地阻止提交文件。
  - 优势：exclude 文件本身不会提交至远程仓库，因此适合放一些个人定制的 「gitignore」 项目。
  - 局限：和 .gitignore 存在同样地局限。文件若已存在远程仓库，则本地修改仍可以提交至远程仓库。本地的修改会显示在 git status 结果中。
- `assume-unchanged`

  - 说明：声明本地远程都不会修改这个文件。
  - 优势：git 直接跳过这些文件的处理以提升性能。文件不会出现在 git status。
  - 局限：不适合本地或远程需要修改的文件。本地会忽略掉之后远程文件的修改。

  ```bash
  git update-index --assume-unchanged
  ```

- `skip-worktree`

  - 说明：声明忽略文件的本地修改。
  - 优势：本地可以对文件做一些个人定制。文件不会出现在 git status。
  - 局限：拉取远程文件更新，或切换分支时有可能出现冲突，需要撤销忽略后手动解决冲突。

  ```bash
  git update-index --assume-unchanged
  ```

### 设置跟踪关系

- 新建一个分支并设置跟踪关系

  ```bash
  git checkout -b new_branch_name [--track] origin/remote_branch_name # --track 选项可以省略
  ```

- 设置已有分支和远端分支的跟踪关系

  ```bash
  git branch -u origin/remote_branch_name local_branch_name
  ```

  > -u 选项是 --set-upstream-to 的简写；
  > local_branch_name 可以省略，默认值为当前分支。

## Reference

- [git 思维导图](git思维导图.pdf)
- [Git 小技巧 - 忽略不想要提交的本地修改](https://mengqi92.github.io/2020/07/17/hide-files-from-git/)
- [设置 git 分支的跟踪关系](https://blog.csdn.net/big_thinker/article/details/52664710)
