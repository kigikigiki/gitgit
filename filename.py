print('Hello World!!')

print('dsfmklsdfnbdfonvlkfdmvkladfkv')

# 1. 최초 파일 지정 : git init
# 2. 파일 add : git add <fileName>
#   <fileName> 대신 . 을 넣으면 모든 파일
# 3. 커밋 취소 (cached 안쓰면 파일이 아예 사라지는 경우가 발생된다.) : git rm --cached <fileName>
# 4. 내가 수정하다가 수정된걸 전체 취소 하고 싶으면
#     git checkout -- <fileName>
# 5. add, commit 합친게 : git commit -am "your message"
# 6. commit 취소 HEAD~<depth> or <commit id>
#   마지막 commit 1 개를 되돌리는데... 이 때 상태를 unstaged 상태로 만든다. : git reset --mixed HEAD~1
#   마지막 commit 1 개를 되돌리는데... 이 때 상태를 staged 상태로 만든다. : git reset --soft HEAD~1

#   git reflog로 commit된 내용들 보}
#   (주의)새로운 브랜치 만들어서 실행하면 됨 마지막 commit 1 개를 되돌리는데... 변경사항은 모두 버린다. : git reset --hard HEAD~1

# 7. coomit 취소 이건 새로 commit되어서 기록으로 남는다. : git revert HEAD or git revert --no-edit <commit id>
#   --no-edit 옵션은 revert하고 commit을 자동으로 메시지를 작성해서 해준다. 예. Revert "기존 커밋 내용"
# 8. 내 현재 브랜치 확인 : git branch
# 9. git pull origin master
# 10. merge는 받는 쪽에서 땡겨온다 마스터에서 떙겨서 가져온다.
# 11. git merge <데이터 땡겨올 branch Name>
# 12. merge한걸 취소하고 싶으면(conflict났을 경우) : git merge --abort
# 13. 충돌을 수정하고 5번을 다시 실행 (add 후 commit)
# 14. 가지치기 하는 모습이 싫고 일자로 마스터와 브랜치를 만들고 싶은 경우  : git rebase <데이터 땡겨올 branch Name>
# 15. rebase한걸 취소하고 싶으면(conflict났을 경우) : git rebase --abort
# 16. rebase로 땡겨와 충돌이난걸 수정하고 (add 후 git rebase --continue)
# 17. commit id가 너무 랜덤이여서 좀 더 보기 쉽게 태그로 쓸 수 있음. : git tag <tag Name ex.v1.0.0> (현재 커밋된곳에서 해야함.)
# 18. 깃 repository에 있는걸 이름을 줘서 가지고 있기 : git remote <name> <url>
# 19. push : git push <remote한 이름> <branch>
# 20. pull : git pull <remote한 이름> <branch>
# 21. HEAD@{70}
# 22. untracked까지 stash 하는 명령어 git stash --include-untracked
# 23. 새로운 브랜치 만들기와 동시에 체크 아웃 git checkout -b <branch>
# 24. git cherry-pick {commit id}
