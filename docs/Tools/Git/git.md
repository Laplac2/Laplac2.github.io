# Git

- [1 简介](#1-简介)
- [2 命令](#2-命令)
  - [2.1 git clone](#21-git-clone)
  - [2.2 git add](#22-git-add)
  - [2.3 git commit](#23-git-commit)
  - [2.4 git pull](#24-git-pull)
  - [2.5 git push](#25-git-push)
  - [2.6 git fetch](#26-git-fetch)
  - [2.7 git rebase](#27-git-rebase)
  - [2.8 git remote](#28-git-remote)
  - [2.9 git cherry-pick](#29-git-cherry-pick)
  - [2.10 git diff](#210-git-diff)
  - [2.11 git log](#211-git-log)
  - [2.12 git show](#212-git-show)
  - [2.13 git branch](#213-git-branch)
- [3 进阶操作](#3-进阶操作)
  - [3.1 Git global setup](#31-git-global-setup)
  - [3.2 Create a new repository](#32-create-a-new-repository)
  - [3.3 Push an existing folder](#33-push-an-existing-folder)
  - [3.4 Push an existing Git repository](#34-push-an-existing-git-repository)
  - [3.5 忽略更改](#35-忽略更改)
  - [3.6 设置跟踪关系](#36-设置跟踪关系)
  - [3.7 通过哈希值查找提交](#37-通过哈希值查找提交)
  - [3.8 修改分支名](#38-修改分支名)
- [4 Reference](#4-reference)

## 1 简介

## 2 命令

### 2.1 git clone

```bash
git clone url directory-name # 将拉下来的仓库文件夹重命名
```

### 2.2 git add

```bash
git add .
git add file-path-name
git add --patch file-path-name  #
```

### 2.3 git commit

```bash
git commit --amend
git commit --no-edit
git commit --amend --edit
git commit --fixup=<Hash>
```

### 2.4 git pull

```bash
git pull origin --rebase # 拉取远程分支并 rebase
```

### 2.5 git push

```bash
git push -f origin
git push --delete origin <branch> # 删除远程分支
```

### 2.6 git fetch

```bash
git fetch orgin
```

### 2.7 git rebase

```bash
git rebase -i <Hash>
git rebase --autosquash -i <Hash>
```

### 2.8 git remote

```bash
git remote -v
git remote show origin
git remote prune origin
```

### 2.9 git cherry-pick

### 2.10 git diff

commit_A: 前一次提交的 hash 值。
commit_B: 需要导出位置的提交的 hash 值。
`git diff commit_A commit_B > pach.pach`
注：导出的 pach 文件是两个提交信息之间所有的差异。

### 2.11 git log

### 2.12 git show

### 2.13 git branch

```bash
git branch -m <old name> <new name> # 修改本地分支名
```

## 3 进阶操作

### 3.1 Git global setup

```bash
git config --global user.name "xxx"
git config --global user.email "xxx@zzz.com"
```

### 3.2 Create a new repository

```bash
git clone git@github.com:xxx/xyz.git
cd xyz
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

### 3.3 Push an existing folder

```bash
cd existing_folder
git init
git remote add origin git@github.com:xxx/xyz.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

### 3.4 Push an existing Git repository

```bash
cd existing_repo
git remote rename origin old-origin
git remote add origin git@github.com:xxx/xyz.git
git push -u origin --all
git push -u origin --tags
```

### 3.5 忽略更改

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

### 3.6 设置跟踪关系

- 新建一个分支并设置跟踪关系

  ```bash
  git checkout -b new_branch_name [--track] origin/remote_branch_name # --track 选项可以省略
  ```

- 设置已有分支和远端分支的跟踪关系

  ```bash
  git branch -u origin/remote_branch_name local_branch_name
  # or
  git branch --set-upstream-to=origin/branch_name local_branch_name
  ```

  > -u 选项是 --set-upstream-to 的简写；
  > local_branch_name 可以省略，默认值为当前分支。

### 3.7 通过哈希值查找提交

```bash
git log <Hash>
git show <Hash>
```

### 3.8 修改分支名

```bash
git push --delete origin <branch>   # 删除远程分支
git branch -m <old name> <new name> # 修改本地分支名
git push origin <new branch>        # 推送本地分支
```

## 4 Reference

- [git 思维导图](git思维导图.pdf)
- [Git 小技巧 - 忽略不想要提交的本地修改](https://mengqi92.github.io/2020/07/17/hide-files-from-git/)
- [设置 git 分支的跟踪关系](https://blog.csdn.net/big_thinker/article/details/52664710)
